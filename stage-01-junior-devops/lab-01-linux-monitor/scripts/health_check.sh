#!/usr/bin/env bash
set -euo pipefail

DISK_THRESHOLD="${1:-85}"
RAW_LOG_DIR="$(dirname "${BASH_SOURCE[0]}")/../logs"
mkdir -p "$RAW_LOG_DIR"
LOG_DIR="$(cd "$RAW_LOG_DIR" && pwd)"
LOG_FILE="${LOG_DIR}/health.log"
TIMESTAMP="$(date '+%Y-%m-%d %H:%M:%S %Z')"

DISK_USAGE="$(df -P / | awk 'NR==2 {gsub("%", "", $5); print $5}')"
MEM_USAGE="$(free -m 2>/dev/null | awk '/^Mem:/ {printf "%.0f", ($3/$2)*100}' || true)"

if [ -z "$MEM_USAGE" ]; then
  MEM_USAGE="$(vm_stat | awk '/Pages active/ {active=$3} /Pages wired/ {wired=$4} /Pages free/ {free=$3} END {gsub(/\./,"",active); gsub(/\./,"",wired); gsub(/\./,"",free); total=active+wired+free; if (total>0) printf "%.0f", ((active+wired)/total)*100; else print 0}')"
fi

STATUS="OK"
EXIT_CODE=0

if [ "$DISK_USAGE" -ge "$DISK_THRESHOLD" ]; then
  STATUS="WARN: Disk usage (${DISK_USAGE}%) >= ${DISK_THRESHOLD}%"
  EXIT_CODE=1
fi

REPORT="[${TIMESTAMP}] status=\"${STATUS}\" disk_pct=${DISK_USAGE}% mem_pct=${MEM_USAGE}%"
echo "$REPORT" | tee -a "$LOG_FILE"
exit "$EXIT_CODE"
