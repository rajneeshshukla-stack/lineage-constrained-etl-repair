from .base_contract import BaseContract
class NullabilityBoundContract(BaseContract):
    def __init__(self, name: str, field_name: str, max_null_ratio: float = 0.05):
        super().__init__(name, field_name)
        self.max_null_ratio = max_null_ratio
    def evaluate(self, df) -> dict:
        null_ratio = df[self.field_name].isnull().mean() if self.field_name in df.columns else 1.0
        passed = null_ratio <= self.max_null_ratio
        return {'contract': self.name, 'passed': passed, 'null_ratio': float(null_ratio), 'score': 1.0 if passed else 0.0}
