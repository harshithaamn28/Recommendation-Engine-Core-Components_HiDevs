import math

class SimilarityCalculator:

    # cosine similarity between two vectors
    def cosine_similarity(self, v1, v2):
        # checking edge cases
        if len(v1) == 0 or len(v2) == 0:
            return 0

        dot = 0
        for i in range(min(len(v1), len(v2))):
            dot += v1[i] * v2[i]

        mag1 = math.sqrt(sum([x*x for x in v1]))
        mag2 = math.sqrt(sum([x*x for x in v2]))

        if mag1 == 0 or mag2 == 0:
            return 0

        return dot / (mag1 * mag2)

    # jaccard similarity for sets
    def jaccard_similarity(self, s1, s2):
        if len(s1) == 0 or len(s2) == 0:
            return 0

        inter = len(s1.intersection(s2))
        union = len(s1.union(s2))

        if union == 0:
            return 0

        return inter / union