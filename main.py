from candidate_generator import CandidateGenerator
from scorer import RecommendationScorer
from evaluator import RecommendationEvaluator


# scoring functions
def relevance_score(user_id, item_id, context):
    return {"movie3": 0.9, "movie4": 0.7, "movie5": 0.5}.get(item_id, 0)

def popularity_score(user_id, item_id, context):
    return {"movie3": 0.8, "movie4": 0.6, "movie5": 0.9}.get(item_id, 0)


def main():
    user_id = "user1"

    # candidate generation
    gen = CandidateGenerator()
    candidates = gen.hybrid_candidates(user_id)

    # scoring
    scorer = RecommendationScorer()
    scorer.add_scorer("relevance", relevance_score, 0.7)
    scorer.add_scorer("popularity", popularity_score, 0.3)

    ranked = scorer.rank_candidates(user_id, candidates)

    # evaluation
    evaluator = RecommendationEvaluator()
    relevant = ["movie3", "movie5"]

    metrics = evaluator.evaluate_all(ranked, relevant)

    # output
    print("\n--- Final Output ---")
    print("Candidates:", candidates)
    print("Ranked:", ranked)
    print("Metrics:", metrics)


if __name__ == "__main__":
    main()