from celery import Celery

app = Celery("worker_celery", broker="amqp://guest:guest@rabbit//")

app.conf.update(
    result_backend="rpc://",
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

app.conf.task_queues = {
    "worker_queue": {
        "exchange": "default",
        "binding_key": "default",
    }
}
