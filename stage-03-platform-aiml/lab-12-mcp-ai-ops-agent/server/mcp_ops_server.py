"""Minimal MCP-style JSON-RPC 2.0 AI Ops server exposing safe read-only ops tools."""
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]


def _list_labs() -> dict:
    labs = []
    for stage_dir in sorted(REPO_ROOT.glob("stage-*")):
        for lab_dir in sorted(stage_dir.glob("lab-*")):
            labs.append({"stage": stage_dir.name, "lab": lab_dir.name})
    return {"repo_root": str(REPO_ROOT), "lab_count": len(labs), "labs": labs}


def _calc_error_budget(slo: float, total: int, failed: int) -> dict:
    allowed_failures = total * (1.0 - slo / 100.0)
    consumed_pct = (failed / allowed_failures * 100.0) if allowed_failures > 0 else 100.0
    return {
        "slo_target_pct": slo,
        "total_requests": total,
        "failed_requests": failed,
        "error_budget_requests": round(allowed_failures, 2),
        "budget_consumed_pct": round(consumed_pct, 2),
        "status": "HEALTHY" if consumed_pct <= 100.0 else "EXHAUSTED",
    }


TOOLS = {
    "list_roadmap_labs": {
        "description": "List all stages and labs present in the repository.",
        "handler": lambda args: _list_labs(),
    },
    "check_error_budget": {
        "description": "Calculate remaining SRE error budget from SLO, total requests, and failed requests.",
        "handler": lambda args: _calc_error_budget(
            float(args.get("slo", 99.9)),
            int(args.get("total", 100000)),
            int(args.get("failed", 25)),
        ),
    },
}


def handle_message(msg: dict) -> dict:
    msg_id = msg.get("id")
    method = msg.get("method", "")
    params = msg.get("params") or {}

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "serverInfo": {"name": "devops-mcp-ops-server", "version": "1.0.0"},
                "capabilities": {"tools": {}},
            },
        }

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "tools": [
                    {"name": name, "description": spec["description"]}
                    for name, spec in TOOLS.items()
                ]
            },
        }

    if method == "tools/call":
        tool_name = params.get("name", "")
        arguments = params.get("arguments") or {}
        if tool_name not in TOOLS:
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32601, "message": f"Unknown tool: {tool_name}"},
            }
        output = TOOLS[tool_name]["handler"](arguments)
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {"content": [{"type": "text", "text": json.dumps(output, indent=2)}]},
        }

    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "error": {"code": -32601, "message": f"Unsupported method: {method}"},
    }


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        request = json.loads(line)
        response = handle_message(request)
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
