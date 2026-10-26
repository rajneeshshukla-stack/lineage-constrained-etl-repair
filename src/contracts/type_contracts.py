from .base_contract import BaseContract
class DataTypeContract(BaseContract):
    def __init__(self, name: str, field_name: str, expected_type: str):
        super().__init__(name, field_name)
        self.expected_type = expected_type
    def evaluate(self, df) -> dict:
        passed = self.field_name in df.columns and self.expected_type in str(df[self.field_name].dtype)
        return {'contract': self.name, 'passed': passed, 'score': 1.0 if passed else 0.0}
