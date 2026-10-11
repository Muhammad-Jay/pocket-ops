from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4

class TaskType(Enum):
    NOTE = "note"
    REMINDER = "reminder"


@dataclass
class Task:
    id: int
    title: str
    description: str | None = field(default_factory=None)
    resolved: bool = field(default_factory=False)
    type: TaskType = field(default_factory=TaskType.NOTE)
    created_at: datetime = field(default_factory=datetime.now().isoformat())
    updated_at: datetime = field(default_factory=datetime.now().isoformat())

    def __init__(
        self, 
         title: str, 
         des: str | None = None,
         resolved: bool = False,
         task_type: TaskType = TaskType.NOTE,
         created_at: datetime = datetime.now().isoformat(),
         updated_at: datetime = datetime.now().isoformat()
         ) -> None:
        self.id = int(uuid4())
        self.title = title
        self.description = des
        self.resolved = resolved
        self.type = task_type
        self.created_at = created_at
        self.updated_at = updated_at

        if self.title == "":
            raise ValueError("Title must not be empty")