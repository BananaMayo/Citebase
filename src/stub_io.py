class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def print(self, value):
        #pylint: disable=unnecessary-dunder-call
        self.outputs.append(value.__repr__())

    def input(self, prompt):
        self.print(prompt)
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        return ""

    def add_input(self, value):
        self.inputs.append(value)
