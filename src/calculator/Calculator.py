# calculator/Calculator.py


class Calculator:
    def __init__(self):
        """
        Initializes an instance of the class with a memory attribute set to zero.
        Args:
            self: The instance of the class.
        Returns:
            None.
        """
        self.memory = 0

    def add(self, value: float) -> float:
        """Add value to the current memory."""
        self.memory += value
        return self.memory

    def subtract(self, value: float) -> float:
        """Subtract value from the current memory."""
        self.memory -= value
        return self.memory

    def multiply(self, value: float) -> float:
        """Multiply the current memory by the value."""
        self.memory *= value
        return self.memory

    def divide(self, value: float) -> float:
        """Divide the current memory by the value."""
        if value == 0:
            raise ValueError("Cannot divide by zero.")
        self.memory /= value
        return self.memory

    def root(self, n: float) -> float:
        """Take the n-th root of the current memory."""
        if self.memory < 0:
            raise ValueError("Cannot take the n-th root of a negative number.")
        self.memory **= 1 / n
        return self.memory

    def reset(self) -> None:
        """Reset the memory to zero."""
        self.memory = 0
        return self.memory
