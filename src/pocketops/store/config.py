from  typing import Protocol

from dto.task import Task

class StoreProvider(Protocol):

    def create(task: Task) -> Task:
        ...

    def get(id: int) -> Task | None:
        ...

    def list() -> list[Task] | None:
        ...

    def update(id: int) -> Task | None:
        ...
    
    def delete(id: int) -> None:
        ...

    def initialize_database() -> None:
        ...

























