from similarity import SimilarityCalculator
from candidate_generator import CandidateGenerator
from scorer import Scorer
from evaluator import Evaluator


def main():

    # available items
    all_items = ["movie1", "movie2", "movie3", "movie4", "movie5"]

    print("Available movies:", all_items)

    # taking user input
    user_input = input("Enter movies you like (comma separated): ")

    # convert to set and clean spaces
    user_items = set(user_input.split(","))
    user_items = {item.strip() for item in user_items if item.strip() != ""}

    # simple validation (extra improvement)
    valid_user_items = set()
    for item in user_items:
        if item in all_items:
            valid_user_items.add(item)

    if not valid_user_items:
        print("No valid items entered. Using default preferences.")
        valid_user_items = {"movie1", "movie2"}

    # similarity scores (dummy data)
    similarity_scores = {
        "movie3": 0.9,
        "movie4": 0.7,
        "movie5": 0.5
    }

    relevant_items = {"movie3", "movie5"}

    # creating objects
    gen = CandidateGenerator()
    scorer = Scorer()
    eval = Evaluator()

    # pipeline
    candidates = gen.generate(valid_user_items, all_items)
    ranked = scorer.rank(candidates, similarity_scores)
    top_items = scorer.top_k(ranked, 3)
    prec = eval.precision(top_items, relevant_items)

    # output
    print("\n--- Recommendation Results ---")
    print("Candidates:", candidates)
    print("Top recommendations:", top_items)
    print("Precision:", round(prec, 2))


if __name__ == "__main__":
    main()