import threading

class Leprechaun:
    def __init__(self):
        self._task_queue = []
        self._stopped = False
        self._lock = threading.Lock()

    def run_until_complete(self, coroutine):
        with self._lock:
            task = Task(coroutine)
            self._task_queue.append(task)

        while not self._stopped:
            with self._lock:
                ready_tasks = [t for t in self._task_queue if t.ready()]
                for task in ready_tasks:
                    self._task_queue.remove(task)
                    task.step()
                    if not task.done():
                        self._task_queue.append(task)

class Task:
    def __init__(self, coroutine):
        self._coroutine = coroutine
        self._step()

    def step(self):
        try:
            result = self._coroutine.send(self._result)
            if isinstance(result, Awaitable):
                self._result = result._wait()
            else:
                self._result = result
                self._step()
        except StopIteration:
            self._done = True

    def ready(self):
        if not hasattr(self, '_result'):
            return False
        return isinstance(self._result, Awaitable) and self._result.ready()

    def done(self):
        return hasattr(self, '_done') and self._done

class Awaitable:
    def __init__(self, leprechaun):
        self._leprechaun = leprechaun
        self._result = None
        self._done = False
        self._lock = threading.Lock()
        self._condition = threading.Condition(self._lock)

    def _wait(self):
        with self._lock:
            if not self._done:
                self._condition.wait()
            return self._result

    def set_result(self, result):
        with self._lock:
            self._result = result
            self._done = True
            self._condition.notify_all()

    def ready(self):
        with self._lock:
            return self._done

def sleep(leprechaun, seconds):
    awaitable = Awaitable(leprechaun)
    timer = threading.Timer(seconds, awaitable.set_result, [None])
    timer.start()
    return awaitable

def create_task(leprechaun, coroutine):
    return Task(coroutine)
