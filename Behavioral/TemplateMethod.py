# Concrete classes


class Work:
    def __init__(self):
        self._template_method()

    def _template_method(self):
        self._task_a()
        self._task_b()
        self._task_c()

    def _task_a(self):
        print("Task A")

    def _task_b(self):
        print("Task B")

    def _task_c(self):
        print("Task C")


# Using


w = Work()
# Output:
# Task A
# Task B
# Task C