from pydantic import BaseModel
from fastapi import Body


class TaskModel(BaseModel):
    benchmark_id: int
    iterations: int = 10000


task_model_example = Body(
    ...,
    example={
        "benchmark_id": 0,
        "iterations": 10000
    }
)
