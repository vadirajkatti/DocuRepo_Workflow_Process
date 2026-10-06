# Reliability

## Idempotency
A job ID acts as an idempotency key. Duplicate submissions do not create duplicate work.

## Retries
Production workers should use bounded exponential backoff and move exhausted work to a dead-letter queue.

## Observability
Recommended metrics include processing latency, success rate, retry count, queue depth and failure rate. Track P50/P95/P99 latency for user-visible operations.
