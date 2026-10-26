class ColumnLineageTracker:
    def __init__(self, dag: dict):
        self.dag = dag
    def trace_column(self, col: str) -> list:
        return [e['src'] for e in self.dag.get('edges', []) if e.get('tgt') == col]
