class ETLDAGBuilder:
    def __init__(self):
        self.nodes, self.edges = set(), []
    def add_transformation(self, src, tgt, t_type):
        self.nodes.add(src); self.nodes.add(tgt)
        self.edges.append({'src': src, 'tgt': tgt, 'type': t_type})
    def get_dag(self) -> dict:
        return {'nodes': list(self.nodes), 'edges': self.edges}
