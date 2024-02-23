
import threading

def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, daemon=True, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper