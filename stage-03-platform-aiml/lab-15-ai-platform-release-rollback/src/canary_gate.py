"""Evaluate canary release metrics against baseline SLO guardrails."""
import json
import sys


def evaluate_canary(
    baseline_err_pct: float,
    canary_err_pct: float,
    baseline_p95_ms: float,
    canary_p95_ms: float,
    max_err_delta_pct: float = 0.5,
    max_p95_multiplier: float = 1.25,
) -> dict:
    err_delta = round(canary_err_pct - baseline_err_pct, 3)
    p95_ratio = round(canary_p95_ms / baseline_p95_ms, 2) if baseline_p95_ms > 0 else 999.0
    promote = (err_delta <= max_err_delta_pct) and (p95_ratio <= max_p95_multiplier)
    return {
        "err_delta_pct": err_delta,
        "max_err_delta_pct": max_err_delta_pct,
        "p95_ratio": p95_ratio,
        "max_p95_multiplier": max_p95_multiplier,
        "decision": "PROMOTE" if promote else "ROLLBACK",
    }


def main() -> None:
    print("Healthy canary:", json.dumps(evaluate_canary(0.2, 0.35, 400.0, 450.0)))
    print("Degraded canary:", json.dumps(evaluate_canary(0.2, 1.4, 400.0, 680.0)))


if __name__ == "__main__":
    main()
    sys.exit(0)
