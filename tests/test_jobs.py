from workflow_platform.models.domain import DocumentJob, Status
from workflow_platform.services.job_service import JobService

def test_submission_is_idempotent():
    service = JobService()
    first = service.submit(DocumentJob("J1", "D1"))
    second = service.submit(DocumentJob("J1", "D1"))
    assert first is second

def test_successful_processing():
    service = JobService()
    service.submit(DocumentJob("J1", "D1"))
    job = service.process("J1")
    assert job.status == Status.COMPLETED
    assert job.attempts == 1

def test_failure_is_recorded():
    service = JobService()
    service.submit(DocumentJob("J1", "D1"))
    job = service.process("J1", succeed=False)
    assert job.status == Status.FAILED
    assert job.error
