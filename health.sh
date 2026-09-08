#!/bin/bash
set -euo pipefail

printf '%s\n' "J.A.R.V.I.S. health check starting..."

DISK=$(df / | awk 'NR==2 {gsub(/%/,""); print $5}')

printf 'Disk usage: %s%%\n' "$DISK"

if [ "$DISK" -gt 80 ]; then
    printf '%s\n' "WARNING: disk almost full"
else
    printf '%s\n' "OK: disk healthy"
fi
