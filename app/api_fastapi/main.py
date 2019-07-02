import memory
import threading

from fastapi import FastAPI
from tariffs_modules import Factory
from api_fastapi.tasks import *
import api_fastapi.routers.benchmarks
import api_fastapi.routers.darwin

app = FastAPI()
app.include_router(api_fastapi.routers.benchmarks.router)
app.include_router(api_fastapi.routers.darwin.router)

# Create and init all modules
names = Factory.list_modules()
modules = [Factory.create(n) for n in names]
app.modules = modules

# Init benchmark async tasks
app.task_manager = TaskManager(app)

# current_app.memory = memory.Redis(configuration={"host": "localhost", "port": 6379, "db": 0})
app.memory = memory.InMemory()

threading.Thread(target=do_tasks, args=[app]).start()

