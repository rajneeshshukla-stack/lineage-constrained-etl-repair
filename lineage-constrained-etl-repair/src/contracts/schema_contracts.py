from .base_contract import BaseContract
class SchemaExistenceContract(BaseContract):
    def evaluate(self, df) -> dict:
        passed = self.field_name in df.columns
        return {'contract': self.name, 'field': self.field_name, 'passed': passed, 'score': 1.0 if passed else 0.0}
