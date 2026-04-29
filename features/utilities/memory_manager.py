class MemoryManager:
    """
    Utility class for storing and retrieving scenario-specific data in Behave tests.
    Automatically cleared after each scenario.
    """
    def __init__(self):
        self._memory = {}

    def set(self, key, value):
        self._memory[key] = value

    def get(self, key, default=None):
        return self._memory.get(key, default)

    def clear(self):
        self._memory.clear()
