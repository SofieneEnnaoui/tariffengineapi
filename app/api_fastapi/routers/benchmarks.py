import uuid
import datetime

from fastapi import APIRouter
from starlette.requests import Request
from tariffs_modules import Factory
from api_fastapi.models.tasks import *

router = APIRouter()


@router.get("/benchmarks", tags=["Benchmark general API"])
def get_list():
    """
    This function responds to a request for /api_connexion/benchmark
    with the complete lists modules

    :return: list of modules with ids
    """
    # Create the list of people from our data
    return list(enumerate(Factory.list_modules()))


@router.get("/benchmarks/{benchmark_id}", tags=["Benchmark synchronous API"])
def get_result(benchmark_id: int, request: Request, iterations: int = 10000):
    """
    This function responds to a request for /api_connexion/benchmarks/{benchmark_id}
    with the module loop benchmark informations
    in a synchronous way

    :return: unsorted list of modules
    """
    module = request.app.modules[benchmark_id]
    return module.loop(iterations)


def create_task(props, fn, args, request: Request):
    return {"task_id":  request.app.task_manager.create_task(props, fn, args)}


@router.post("/benchmarks/create", tags=["Benchmark asynchronous API"])
def create_benchmark_task(request: Request, props: TaskModel = task_model_example):
    args = {
        "benchmark_id": props.benchmark_id,
        "request": request,
        "iterations": props.iterations
    }
    return create_task(dict(props), get_result, args, request)


@router.get("/benchmarks/status/{unique_id}", tags=["Benchmark asynchronous API"])
def get_status_task(unique_id: str, request: Request):
    if request.app.memory.get(uuid.UUID(unique_id))[1] is None:
        return {"status": "InProgress"}
    return {"status": "Completed"}


@router.get("/benchmarks/result/{unique_id}", tags=["Benchmark asynchronous API"])
def get_task_result(unique_id: str, request: Request):
    uid = uuid.UUID(unique_id)
    if request.app.memory.get(uid)[1] is not None:
        task = request.app.memory.pop(uid)[1]
        task["return_date"] = datetime.datetime.now().timestamp()
        return task
    return {"status": "InProgress"}
