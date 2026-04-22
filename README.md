# Recommendation Engine Core Components

This project implements the core components of a recommendation engine. It demonstrates how items can be recommended using similarity, candidate generation, scoring, and evaluation.

---

## Installation

pip install -r requirements.txt

---

## Usage

python main.py

---

## Components

### Similarity Calculator
Implements cosine similarity, jaccard similarity, and pearson correlation to measure similarity between users or items.

### Candidate Generator
Generates recommendation candidates using:
- Collaborative filtering
- Content-based filtering
- Popularity-based method
- Hybrid approach (combination)

### Scorer & Ranker
Assigns scores to items using multiple scoring factors like relevance and popularity. Uses weighted scoring and provides explanation for each recommendation.

### Evaluator
Evaluates recommendations using:
- Precision
- Recall
- NDCG (ranking quality)

---

## Workflow

1. Generate candidate items  
2. Score each item using weighted functions  
3. Rank items based on score  
4. Evaluate recommendations using metrics  

---

## Features

- Modular design  
- Multiple recommendation strategies  
- Weighted scoring system  
- Explanation for recommendations  
- Evaluation using 3 metrics  

---

## Output

The program displays:
- Candidate items  
- Ranked recommendations with scores  
- Explanation of scores  
- Evaluation metrics  

---

## Technologies Used

Python and standard libraries

---

## Conclusion

This project demonstrates how recommendation systems work at a basic level and can be extended to real-world datasets and advanced models.
