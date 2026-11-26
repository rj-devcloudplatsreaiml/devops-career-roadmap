"""Verify model release metadata before approving production deployment."""
import json
import sys

REQUIRED_FIELDS = ("model_name", "version", "owner", "dataset_version", "eval_score")


def audit_release(metadata: dict, min_score: float = 0.80) -> dict:
    missing = [f for f in REQUIRED_FIELDS if not metadata.get(f)]
    score = float(metadata.get("eval_score", 0.0))
    approved = bool(metadata.get("approved", False))
    passed = (not missing) and (score >= min_score) and approved
    return {
        "model": metadata.get("model_name", "unknown"),
        "missing_fields": missing,
        "score_ok": score >= min_score,
        "approved": approved,
        "deployment_allowed": passed,
    }


def main() -> None:
    candidate = {
        "model_name": "iris-classifier",
        "version": "1.2.0",
        "owner": "platform-ml",
        "dataset_version": "v2026.11",
        "eval_score": 0.94,
        "approved": True,
    }
    unapproved = {
        "model_name": "iris-classifier",
        "version": "1.3.0-rc1",
        "owner": "platform-ml",
        "dataset_version": "v2026.11",
        "eval_score": 0.91,
        "approved": False,
    }
    print("Candidate:", json.dumps(audit_release(candidate)))
    print("RC1:", json.dumps(audit_release(unapproved)))


if __name__ == "__main__":
    main()
    sys.exit(0)
