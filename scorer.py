class Scorer:

    # assigning scores to items
    def rank(self, candidates, similarity_scores):

        if len(candidates) == 0:
            return []

        result = []

        for item in candidates:
            score = 0

            # if score not present, default 0
            if item in similarity_scores:
                score = similarity_scores[item]

            result.append((item, score))

        # sorting based on score
        result.sort(key=lambda x: x[1], reverse=True)

        return result

    def top_k(self, ranked_list, k=3):
        return ranked_list[:k]