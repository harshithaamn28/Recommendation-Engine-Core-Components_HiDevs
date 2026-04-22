import math

class RecommendationEvaluator:

    def precision_at_k(self, recs, relevant, k):
        recs = recs[:k]
        if not recs:
            return 0
        
        items = [i for i, _, _ in recs]
        return len(set(items) & set(relevant)) / len(items)

    def recall_at_k(self, recs, relevant, k):
        recs = recs[:k]
        if not relevant:
            return 0
        
        items = [i for i, _, _ in recs]
        return len(set(items) & set(relevant)) / len(relevant)

    def ndcg_at_k(self, recs, relevant, k):
        dcg = 0
        for i, (item, _, _) in enumerate(recs[:k]):
            if item in relevant:
                dcg += 1 / math.log2(i + 2)

        ideal = sum(1 / math.log2(i + 2) for i in range(min(len(relevant), k)))

        return dcg / ideal if ideal != 0 else 0

    def evaluate_all(self, recs, relevant, k=3):
        return {
            "precision": self.precision_at_k(recs, relevant, k),
            "recall": self.recall_at_k(recs, relevant, k),
            "ndcg": self.ndcg_at_k(recs, relevant, k)
        }