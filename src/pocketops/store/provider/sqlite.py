import datetime
from sqlite3 import Connection, connect
from pocketops.dto.task import Task


class SqliteRepository:

    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        self.conn = self.__connect()
    

    def create(self, task: Task) -> Task:
        now = datetime.datetime.now().isoformat()
        self.conn.execute("INSERT INTO tasks (title, description, resolved, type, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)", (str(task.title), str(task.description), 0, task.type.value, now, now))
        self.conn.commit()
        return task 

    def list(self) -> list[Task] | None:
        cursor = self.conn.execute("SELECT * FROM tasks")
        return [Task(row[1], row[2], row[3], row[4], row[5]) for row in cursor]
        

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
        self.conn.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, description TEXT, resolved INTEGER NOT NULL DEFAULT 0, type TEXT NOT NULL DEFAULT NOTE, created_at TEXT NOT NULL, updated_at TEXT NOT NULL)")
