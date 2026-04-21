class Evaluator:

    # precision = relevant recommended / total recommended
    def precision(self, recommended, relevant):

        if len(recommended) == 0:
            return 0

        rec_items = set()
        for item, score in recommended:
            rec_items.add(item)

        rel_items = set(relevant)

        count = 0

        for item in rec_items:
            if item in rel_items:
                count += 1

        return count / len(rec_items)