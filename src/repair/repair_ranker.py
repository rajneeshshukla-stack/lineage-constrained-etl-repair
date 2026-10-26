class MultiObjectiveRepairRanker:
    def rank_candidates(self, candidates: list) -> list:
        for idx, c in enumerate(candidates):
            c['composite_score'] = round(0.95 - (idx * 0.05), 4)
        return candidates
