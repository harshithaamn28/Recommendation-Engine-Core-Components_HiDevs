class CandidateGenerator:

    def generate(self, user_items, all_items):

        if not user_items:
            print("No user data, returning empty list")
            return []

        candidates = []

        for item in all_items:
            if item not in user_items:
                candidates.append(item)

        return candidates