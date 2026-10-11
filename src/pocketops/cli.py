import argparse
from dto.task import Task
from store.task_store import TaskStore
from store.provider.sqlite import SqliteRepository

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pocketops",
        description="A command line tool to serve as a little helper to organize task and work in the background.",
        add_help=True
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    create_parser = subparsers.add_parser("create", help="Create a task")

    return parser



def main(args: list[str] | None = None) -> int:
    parser = build_parser()

    args = parser.parse_args(args)

    store_provider = SqliteRepository("task-store.db")

    task_store = TaskStore(store_provider)
    task_store.initialize_store()

    if args.command == "create":
        print("Creating task...")
        task = Task("the title")
        task_store.add_task(task)
        print("Task created!")
    else:
        print(parser.format_help())


if __name__ == "__main__":
    main()