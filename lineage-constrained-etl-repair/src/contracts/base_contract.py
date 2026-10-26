class BaseContract:
    def __init__(self, name: str, field_name: str):
        self.name = name
        self.field_name = field_name
    def evaluate(self, df) -> dict:
        raise NotImplementedError
