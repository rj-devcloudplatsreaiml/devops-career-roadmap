"""Detect feature distribution drift and decide whether to trigger retraining."""
import json
import sys


def check_drift(
    baseline_means: dict[str, float],
    live_means: dict[str, float],
    max_rel_shift: float = 0.20,
) -> dict:
    drifted = {}
    for feat, base_val in baseline_means.items():
        live_val = live_means.get(feat, base_val)
        rel_shift = abs(live_val - base_val) / abs(base_val) if base_val != 0 else 0.0
        if rel_shift > max_rel_shift:
            drifted[feat] = {
                "baseline": base_val,
                "live": live_val,
                "rel_shift": round(rel_shift, 3),
            }
    return {
        "drifted_features": drifted,
        "retrain_triggered": bool(drifted),
    }


def main() -> None:
    base = {"sepal_len": 5.84, "petal_len": 3.76}
    stable_live = {"sepal_len": 5.90, "petal_len": 3.85}
    shifted_live = {"sepal_len": 5.88, "petal_len": 5.10}

    print("Stable window:", json.dumps(check_drift(base, stable_live)))
    print("Shifted window:", json.dumps(check_drift(base, shifted_live)))


if __name__ == "__main__":
    main()
    sys.exit(0)
