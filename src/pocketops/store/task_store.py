from dataclasses import dataclass, field
from pathlib import Path

from pocketops.dto.task import Task
from pocketops.store.config import StoreProvider

class TaskStore:
    def __init__(self, provider: StoreProvider):
        self.provider = provider

    def add_task(self, task: Task) -> Task:
        return self.provider.create(task)

    def get_by_id(self, id: int) -> Task:
        return self.provider.get(id)

    def list_all(self) -> list[Task] | None:
        return self.provider.list()

    def update_by_id(self, id: int) -> Task:
        return self.provider.update(id)

    def delete_by_id(self, id: int) -> None:
        return self.provider.delete(id)
    
    def initialize_store(self) -> None:
        self.provider.initialize_database()