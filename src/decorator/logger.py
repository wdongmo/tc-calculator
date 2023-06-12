# calculator/decorator/logger.py
import time


def log_operations(func):
    """
    A decorator that logs the operations performed by the decorated function.
    Parameters:
    func (function): The function to be decorated.
    Returns:
    function: The decorated function that logs the operation performed and returns its output.
    """

    def wrapper(self, x=None):
        """
        Executes the input function and logs the operation name and parameter.
        :param self: the class instance
        :param x: the input parameter for the function
        :return: the return value of the executed input function
        """
        start_time = time.time()
        operation_name = func.__name__
        if x or x == 0:
            result = func(self, x)
        else:
            result = func(self)
        end_time = time.time()
        execution_time = end_time - start_time
        print(
            f"Performing {operation_name}({x}) in {execution_time} {execution_time > 1 and 'seconds' or 'second'}."
        )
        return result

    return wrapper
