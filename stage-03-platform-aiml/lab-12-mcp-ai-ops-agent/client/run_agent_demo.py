"""Send sample MCP JSON-RPC requests to the local ops server and print responses."""
import json
import subprocess
import sys
from pathlib import Path

SERVER_SCRIPT = Path(__file__).resolve().parent.parent / "server" / "mcp_ops_server.py"

MESSAGES = [
    {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}},
    {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}},
    {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "list_roadmap_labs", "arguments": {}}},
    {
        "jsonrpc": "2.0",
        "id": 4,
        "method": "tools/call",
        "params": {"name": "check_error_budget", "arguments": {"slo": 99.9, "total": 100000, "failed": 40}},
    },
]


def main() -> None:
    proc = subprocess.Popen(
        [sys.executable, str(SERVER_SCRIPT)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
    )
    assert proc.stdin is not None and proc.stdout is not None
    for msg in MESSAGES:
        proc.stdin.write(json.dumps(msg) + "\n")
        proc.stdin.flush()
        resp_line = proc.stdout.readline()
        print(f"--- Response {msg['id']} ({msg['method']}) ---")
        print(resp_line.strip())
    proc.stdin.close()
    proc.wait(timeout=5)


if __name__ == "__main__":
    main()
