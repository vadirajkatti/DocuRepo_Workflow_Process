from fastapi import FastAPI
from pydantic import BaseModel
from workflow_platform.models.domain import DocumentJob
from workflow_platform.services.job_service import JobService

app = FastAPI(title="Document Workflow Platform")
service = JobService()

class SubmitRequest(BaseModel):
    job_id: str
    document_id: str

@app.post("/jobs")
def submit(request: SubmitRequest):
    return service.submit(DocumentJob(request.job_id, request.document_id)).__dict__

@app.post("/jobs/{job_id}/process")
def process(job_id: str):
    return service.process(job_id).__dict__

@app.get("/jobs/{job_id}")
def status(job_id: str):
    return service.jobs[job_id].__dict__
