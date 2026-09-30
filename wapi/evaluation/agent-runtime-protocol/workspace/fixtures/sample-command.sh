#!/usr/bin/env bash
set -eu

cabal run runtime-agent -- run \
  --api-base "http://127.0.0.1:9000" \
  --cluster-token fixtures/tokens/cluster.key \
  --state-dir .state \
  --agent-info fixtures/payloads/agent-info.json \
  --start-info fixtures/payloads/start-info.json \
  --tasks-in-progress fixtures/payloads/tasks-in-progress.json \
  --request-id sample-request \
  --task-id task-42 \
  --derivation-path drv/example \
  --state-name cache-A \
  --state-upload fixtures/payloads/state-upload.bin \
  --state-download .state/downloaded-state.bin \
  --task-events .state/task-events.jsonl \
  --build-log fixtures/payloads/build-log.bin \
  --log-token fixtures/tokens/log.key \
  --log-payload fixtures/payloads/log.bin \
  --task-status fixtures/payloads/task-status-success.json \
  --task-logs fixtures/payloads/task-logs.json \
  --build-events fixtures/payloads/build-events.json \
  --eval-events fixtures/payloads/eval-events.json \
  --report .state/report.json \
  --schema .state/schema.json
