from .base_contract import BaseContract
class ReferentialIntegrityContract(BaseContract):
    def __init__(self, name: str, field_name: str, parent_df, parent_key: str):
        super().__init__(name, field_name)
        self.parent_df = parent_df
        self.parent_key = parent_key
    def evaluate(self, df) -> dict:
        orphans = ~df[self.field_name].isin(self.parent_df[self.parent_key]) if self.field_name in df.columns else []
        orphan_ratio = orphans.mean() if len(orphans) > 0 else 1.0
        return {'contract': self.name, 'passed': orphan_ratio == 0.0, 'score': 1.0 - orphan_ratio}
