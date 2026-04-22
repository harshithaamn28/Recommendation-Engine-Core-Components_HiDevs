class CandidateGenerator:

    def collaborative_candidates(self, user_id):
        # dummy logic (simulating similar users)
        return ["movie3", "movie4"]

    def content_based_candidates(self, user_id):
        # dummy logic (based on user history)
        return ["movie4", "movie5"]

    def popularity_candidates(self):
        return ["movie3", "movie5"]

    def hybrid_candidates(self, user_id):
        candidates = (
            self.collaborative_candidates(user_id) +
            self.content_based_candidates(user_id) +
            self.popularity_candidates()
        )

        # remove duplicates + limit size
        return list(set(candidates))[:20]