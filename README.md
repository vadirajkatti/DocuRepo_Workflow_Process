# Document Workflow Platform

> A public-safe reference implementation demonstrating scalable, observable and idempotent document-processing workflows.

## Why this project?
Document systems become difficult when processing volume, workflow branching and failures increase. This project demonstrates the core engineering patterns behind reliable document pipelines without using proprietary code or data.

## Architecture
```text
API -> Job Queue / Orchestrator -> Workers -> Result Store
                    |                |
                    +-> Retry        +-> Parse / Validate / Transform
                    +-> DLQ
```

## Key patterns
- idempotent job submission
- explicit workflow state
- retryable processing
- dead-letter queue design
- horizontal worker scaling
- production observability
- separation of orchestration from processing

## Production mapping
| Reference component | Example production implementation |
|---|---|
| API | FastAPI / API Gateway |
| Orchestrator | AWS Step Functions |
| Queue | SQS |
| Workers | Lambda / ECS |
| Object storage | S3 |
| Result store | PostgreSQL |
| Cache | Redis |

## Run
```bash
pip install -e '.[dev]'
PYTHONPATH=src pytest
uvicorn workflow_platform.api.app:app --reload
```

## Public-safe notice
This is an independently implemented reference architecture. It contains no employer-specific source code, data, credentials or internal business rules.
