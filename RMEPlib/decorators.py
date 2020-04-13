import time
from functools import wraps


def retry(n_retries):
    # A decorator for retrying.
    
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            retry = 0
            while retry < n_retries:
                temp = func(*args, **kwargs)

                if type(temp) == list or type(temp) == tuple:
                    error, response = temp[0], temp[1:]
                else:
                    error, response = temp, None

                if not error: # error != 0
                    return response
                retry += 1
                time.sleep(args[0].retry_interval)
                args[0].log.warn("Retrying %d ..." % retry)
            args[0].log.error("Failed to retry.")
            return None

        return wrapper
    return decorator