class CandidateRepairGenerator:
    def generate_candidates(self, violation: dict) -> list:
        f = violation.get('field', 'column')
        return [{'id': 'R1', 'type': 'COLUMN_ALIAS', 'code': f'ALTER TABLE rename {f}_old TO {f}'}]
