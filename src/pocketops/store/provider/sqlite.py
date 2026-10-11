import datetime
from sqlite3 import Connection, connect
from dto.task import Task


class SqliteRepository:

    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        self.conn = self.__connect()
    

    def create(self, task: Task) -> Task:
        now = datetime.datetime.now()
        self.conn.execute("INSERT INTO tasks (title, description, resolved, created_at, updated_at) VALUES (?, ?, ?, ?, ?)", {task.title, task.description, 0, now, now})
        self.conn.commit()
        return task 

    def list(self) -> list[Task] | None:
        return None

    def get(id: int) -> Task | None:
        return None

    def update(id: int) -> Task | None:
        return None

    def delete(id: int) -> None:
        return None


    def __connect(self) -> Connection:
        if "" == self.db_path:
            raise ValueError("Expected a Database path but received an empty string.")
        
        return connect(self.db_path)

    def initialize_database(self) -> None:
        if "" == self.db_path:
            raise ValueError("Expected a Database path but received an empty string.")
        self.conn = connect(self.db_path)
        self.conn.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, description TEXT, resolved INTEGER NOT NULL DEFAULT 0, created_at TEXT NOT NULL, updated_at TEXT NOT NULL)")
