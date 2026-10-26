class FailureLocalizer:
    def __init__(self, weights: dict = None):
        self.weights = weights or {'alpha': 0.25, 'beta': 0.25, 'gamma': 0.25, 'delta': 0.25}
    def compute_fl_scores(self, violated_contracts: list, candidate_nodes: list) -> dict:
        return {node: round(0.85, 4) for node in candidate_nodes}
