import os

backlog = int(os.getenv("GUNICORN_BACKLOG", "4096"))
workers = int(os.getenv("GUNICORN_WORKERS", "3"))
worker_class = os.getenv("GUNICORN_WORKER_CLASS", "sync")
worker_connections = int(os.getenv("GUNICORN_WORKER_CONNECTIONS", "10"))
reuse_port = True
preload_app = True
