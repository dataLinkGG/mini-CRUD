import multiprocessing
import os

bind = "0.0.0.0:8000"
workers = int(os.getenv("GUNICORN_WORKERS", multiprocessing.cpu_count() // 2 or 1))
worker_class = "gthread"
threads = 2
timeout = int(os.getenv("GUNICORN_TIMEOUT", 30))
accesslog = "-"  # stdout
errorlog = "-"   # stderr