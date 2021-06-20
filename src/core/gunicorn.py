from multiprocessing import cpu_count

bind: str = '0.0.0.0:8000'
worker_class: str = 'gevent'
workers: int = cpu_count() * 2 + 1
max_requests: int = 2048
capture_output: bool = True
