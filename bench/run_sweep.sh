#!/bin/sh
# reproducible serving window: 4096 line sweep, stride-heavy mix
set -e
SWEEP_LINES=${SWEEP_LINES:-4096}
WINDOW=${WINDOW:-stride-heavy}
echo "opening window: $WINDOW / $SWEEP_LINES lines"
./sweep --lines "$SWEEP_LINES" --mix "$WINDOW" --report p99_ms
