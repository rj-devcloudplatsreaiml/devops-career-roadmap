"""Estimate AI inference token cost and p95 latency SLO compliance."""
import json
import sys


def summarize_ai_slo(
    daily_requests: int,
    avg_input_tokens: int,
    avg_output_tokens: int,
    input_rate_per_1m_usd: float,
    output_rate_per_1m_usd: float,
    p95_latency_ms: float,
    p95_slo_ms: float = 1200.0,
    usd_to_inr: float = 84.0,
) -> dict:
    daily_in = daily_requests * avg_input_tokens
    daily_out = daily_requests * avg_output_tokens

    daily_cost_usd = (daily_in / 1_000_000) * input_rate_per_1m_usd + (
        daily_out / 1_000_000
    ) * output_rate_per_1m_usd
    monthly_cost_usd = daily_cost_usd * 30

    return {
        "daily_requests": daily_requests,
        "daily_cost_usd": round(daily_cost_usd, 4),
        "monthly_cost_usd": round(monthly_cost_usd, 2),
        "monthly_cost_inr": round(monthly_cost_usd * usd_to_inr, 2),
        "p95_latency_ms": p95_latency_ms,
        "p95_slo_ms": p95_slo_ms,
        "latency_slo_met": p95_latency_ms <= p95_slo_ms,
    }


def main() -> None:
    report = summarize_ai_slo(
        daily_requests=25000,
        avg_input_tokens=800,
        avg_output_tokens=250,
        input_rate_per_1m_usd=0.30,
        output_rate_per_1m_usd=1.20,
        p95_latency_ms=840.0,
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
    sys.exit(0)
