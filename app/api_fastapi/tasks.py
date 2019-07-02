import datetime
from queue import Queue
import uuid


class Task:
    def __init__(self, unique_id, props, fn, args):
        self.unique_id = unique_id
        self.props = props
        self.fn = fn
        self.args = args
        self.props["creation_date"] = datetime.datetime.now().timestamp()


class TaskManager:
    def __init__(self, app):
        self.app = app
        self.queue = Queue()

    def create_task(self, props, fn, args):
        unique_id = uuid.uuid4()
        new_task = Task(unique_id, props, fn, args)
        self.app.memory.set(unique_id, (new_task.props, None))
        self.queue.put(new_task)
        return unique_id


def do_tasks(app):
    while True:
        task_manager = app.task_manager
        task = task_manager.queue.get()

        state = app.memory.get(task.unique_id)

        task.props["compute_start_date"] = datetime.datetime.now().timestamp()
        task.props["result"] = task.fn(**task.args)
        task.props["compute_end_date"] = datetime.datetime.now().timestamp()

        app.memory.set(task.unique_id, (state[0], task.props))
        print(app.memory.keys())
