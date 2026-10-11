from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class Task:
    id: int
    title: str
    description: str | None = field(default_factory=None)
    resolved: bool = field(default_factory=False)
    created_at: datetime = field(default_factory=datetime.now())
    updated_at: datetime = field(default_factory=datetime.now())

    def __init__(self, title: str, des: str | None = None) -> None:
        self.id = int(uuid4())
        self.title = title
        self.description = des

        if self.title == "":
            raise ValueError("Title must not be empty")