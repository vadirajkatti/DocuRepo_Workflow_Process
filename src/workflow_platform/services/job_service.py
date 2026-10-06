from workflow_platform.models.domain import DocumentJob, Status

class JobService:
    def __init__(self):
        self.jobs: dict[str, DocumentJob] = {}

    def submit(self, job: DocumentJob):
        if job.job_id in self.jobs:
            return self.jobs[job.job_id]
        self.jobs[job.job_id] = job
        return job

    def process(self, job_id: str, succeed: bool = True):
        job = self.jobs[job_id]
        if job.status == Status.COMPLETED:
            return job
        job.status = Status.PROCESSING
        job.attempts += 1
        if succeed:
            job.status = Status.COMPLETED
            job.error = None
        else:
            job.status = Status.FAILED
            job.error = "processor failure"
        return job
