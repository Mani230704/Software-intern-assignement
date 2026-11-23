from statistics import mean, pstdev
from typing import Iterable, Optional

def smooth(readings: Iterable[Optional[float]], window: int = 5) -> list[float]:
    """
    Forward-fill None, replace >3 population standard deviations from the
    preceding window's mean, then return a trailing moving average.

    Assumptions:
    - Empty input -> [].
    - Leading None values -> first subsequent numeric reading (back-fill);
      if every value is None -> [].
    - Spike baseline uses up to `window` preceding cleaned values, excluding
      the current reading. With no preceding values, retain the reading.
    - Moving average uses available values at the beginning (partial window).
    """
    if window < 1:
        raise ValueError("window must be >= 1")
    values = list(readings)
    if not values:
        return []

    # Find first valid value for leading None values.
    first = next((float(x) for x in values if x is not None), None)
    if first is None:
        return []

    filled = []
    previous = first
    for x in values:
        if x is None:
            x = previous
        else:
            x = float(x)
            previous = x
        filled.append(x)

    cleaned = []
    for i, x in enumerate(filled):
        history = cleaned[max(0, i-window):i]
        if history:
            mu = mean(history)
            sigma = pstdev(history)
            if sigma > 0 and abs(x - mu) > 3 * sigma:
                x = mu
        cleaned.append(x)

    result = []
    for i in range(len(cleaned)):
        segment = cleaned[max(0, i-window+1):i+1]
        result.append(mean(segment))
    return result
