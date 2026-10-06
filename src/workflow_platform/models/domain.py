from dataclasses import dataclass
from enum import Enum

class Status(str, Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

@dataclass
class DocumentJob:
    job_id: str
    document_id: str
    status: Status = Status.PENDING
    attempts: int = 0
    error: str | None = None
