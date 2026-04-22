import math

class SimilarityCalculator:

    def cosine_similarity(self, v1, v2):
        if not v1 or not v2:
            return 0
        
        dot = sum(a*b for a, b in zip(v1, v2))
        mag1 = math.sqrt(sum(a*a for a in v1))
        mag2 = math.sqrt(sum(b*b for b in v2))

        if mag1 == 0 or mag2 == 0:
            return 0

        return dot / (mag1 * mag2)

    def jaccard_similarity(self, s1, s2):
        if not s1 or not s2:
            return 0
        
        return len(s1 & s2) / len(s1 | s2)

    def pearson_correlation(self, r1, r2):
        if not r1 or not r2 or len(r1) != len(r2):
            return 0

        n = len(r1)
        sum1 = sum(r1)
        sum2 = sum(r2)

        sum1_sq = sum(x*x for x in r1)
        sum2_sq = sum(x*x for x in r2)

        product_sum = sum(r1[i]*r2[i] for i in range(n))

        num = product_sum - (sum1 * sum2 / n)
        den = ((sum1_sq - (sum1**2)/n) * (sum2_sq - (sum2**2)/n)) ** 0.5

        if den == 0:
            return 0

        return num / den