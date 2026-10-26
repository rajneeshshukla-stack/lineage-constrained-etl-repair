class ContractEvaluator:
    def __init__(self, contracts: list):
        self.contracts = contracts
    def evaluate_suite(self, df) -> dict:
        results = [c.evaluate(df) for c in self.contracts]
        violated = [r for r in results if not r['passed']]
        return {'total_contracts': len(results), 'violated_contracts': violated, 'aggregate_score_C': 1.0 if not violated else 0.0, 'passed': len(violated) == 0}
