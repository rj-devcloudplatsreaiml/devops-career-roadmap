#!/usr/bin/env python3
"""Calculate 30-day SLO error budget, burn rate, and remaining runway."""
import argparse


def evaluate_slo(slo_target: float, total_requests: int, failed_requests: int, window_hours: float) -> None:
    allowed_error_rate = (100.0 - slo_target) / 100.0
    budget_requests = total_requests * allowed_error_rate
    actual_error_rate = (failed_requests / total_requests) if total_requests else 0.0
    budget_consumed_pct = (failed_requests / budget_requests * 100.0) if budget_requests else 0.0
    burn_rate = (actual_error_rate / allowed_error_rate) if allowed_error_rate else 0.0

    print(f"SLO Target          : {slo_target:.3f}%")
    print(f"Total Requests      : {total_requests:,}")
    print(f"Failed Requests     : {failed_requests:,}")
    print(f"Error Budget (reqs) : {budget_requests:,.1f}")
    print(f"Budget Consumed     : {budget_consumed_pct:.2f}%")
    print(f"Observed Burn Rate  : {burn_rate:.2f}x (over {window_hours}h)")

    if burn_rate >= 14.4:
        print("Status              : PAGE NOW — Fast burn (exhausts 30d budget in < 2 days)")
    elif burn_rate >= 6.0:
        print("Status              : TICKET / WARN — Elevated burn (exhausts 30d budget in ~5 days)")
    elif budget_consumed_pct >= 100.0:
        print("Status              : FREEZE RELEASES — Monthly error budget exhausted")
    else:
        print("Status              : HEALTHY — Within error budget")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SRE Error Budget & Burn Rate Calculator")
    parser.add_argument("--slo", type=float, default=99.9, help="SLO target percentage (default: 99.9)")
    parser.add_argument("--total", type=int, required=True, help="Total requests in observation window")
    parser.add_argument("--failed", type=int, required=True, help="Failed (5xx) requests in window")
    parser.add_argument("--hours", type=float, default=1.0, help="Observation window in hours (default: 1.0)")
    args = parser.parse_args()
    evaluate_slo(args.slo, args.total, args.failed, args.hours)
