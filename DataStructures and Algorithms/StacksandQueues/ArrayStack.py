class ArrayStack:
    """Lifo stack implementation using a python list as underlying storage."""

    def __init__(self):
        """Empty stack"""
        self._data = [] #nonpublic list instance
    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)
    
    def is_empty(self):
        """Return true if the stack is empty"""
        return len(self._data) == 0
    
    def push(self,e):
        self._data.append(e)

    def top(self):
        """Return (but not remove) the element at the top of the stack.
            raise empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        """Remove and return the element from the top of the stack(LIFO).
        Raise exception if stack is empty"""

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()



