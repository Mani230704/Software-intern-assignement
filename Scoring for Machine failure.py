"""simple scoring helper for machine-failure risk."""

from __future__ import annotations

from pathlib import Path
import json

import pandas as pd


def build_prediction_row(
    air_temp_k: float,
    process_temp_k: float,
    rotational_speed_rpm: float,
    torque_nm: float,
    tool_wear_min: float,
    machine_type: str = "H",
) -> pd.DataFrame:
    """Build a single-row DataFrame aligned to the training features."""
    row = pd.DataFrame(
        [{
            "Air temperature [K]": air_temp_k,
            "Process temperature [K]": process_temp_k,
            "Rotational speed [rpm]": rotational_speed_rpm,
            "Torque [Nm]": torque_nm,
            "Tool wear [min]": tool_wear_min,
            "Type_L": 1 if machine_type == "L" else 0,
            "Type_M": 1 if machine_type == "M" else 0,
        }]
    )
    return row


if __name__ == "__main__":
    sample = build_prediction_row(300, 1500, 40, 20, 100)
    print(json.dumps(sample.to_dict(orient="records"), indent=2))
