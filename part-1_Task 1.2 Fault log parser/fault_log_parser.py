from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

def parse_fault_log(text: str) -> dict:
    """
    Parse `timestamp | component | fault_type | value` lines.
    Malformed lines are skipped and counted. Returns component counts,
    most common fault type (or None), and components with >3 faults
    in any rolling 10-minute interval.
    """
    faults = []
    skipped = 0
    for line in text.splitlines():
        if not line.strip():
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 4:
            skipped += 1
            continue
        try:
            ts = datetime.strptime(parts[0], TIMESTAMP_FORMAT)
            component, fault_type = parts[1], parts[2]
            float(parts[3])
            if not component or not fault_type:
                raise ValueError
        except (ValueError, TypeError):
            skipped += 1
            continue
        faults.append((ts, component, fault_type))

    per_component = Counter(component for _, component, _ in faults)
    fault_types = Counter(ft for _, _, ft in faults)
    most_common = fault_types.most_common(1)[0][0] if fault_types else None

    # Sliding 10-minute window; >3 means at least 4 faults.
    by_component = defaultdict(list)
    for ts, component, _ in faults:
        by_component[component].append(ts)

    burst_components = set()
    for component, times in by_component.items():
        times.sort()
        left = 0
        for right, current in enumerate(times):
            while current - times[left] > timedelta(minutes=10):
                left += 1
            if right - left + 1 > 3:
                burst_components.add(component)
                break

    return {
        "faults_per_component": dict(sorted(per_component.items())),
        "most_common_fault_type": most_common,
        "components_over_3_faults_in_10_minutes": sorted(burst_components),
        "skipped_lines": skipped,
        "valid_fault_count": len(faults),
    }

def parse_file(path: str | Path) -> dict:
    return parse_fault_log(Path(path).read_text(encoding="utf-8"))

if __name__ == "__main__":
    sample = Path(__file__).with_name("sample_fault.log")
    print(parse_file(sample))
