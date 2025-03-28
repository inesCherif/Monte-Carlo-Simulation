import random

num_simulations = 10000  # Number of book histories simulated
num_generations = 50  # Approximate number of generations in 1400 years
change_prob_other_books = 0.02  # Probability of change per generation for other books
change_prob_quran = 0.00001  # Probability of change per generation for Quran (due to memorization)

unchanged_other_books = 0  # Counter for unchanged texts (other books)
unchanged_quran = 0  # Counter for unchanged Quran

# Running Monte Carlo simulation
for i in range(num_simulations):
    # Simulate other books
    book_changed = any(random.random() < change_prob_other_books for i in range(num_generations))
    if not book_changed:
        unchanged_other_books += 1

    # Simulate Quran preservation
    quran_changed = any(random.random() < change_prob_quran for i in range(num_generations))
    if not quran_changed:
        unchanged_quran += 1

# probabilities
prob_other_books = unchanged_other_books / num_simulations
prob_quran = unchanged_quran / num_simulations

print(f"Probability of a book being perfectly preserved: {prob_other_books:.5f}")
print(f"Probability of the Quran being perfectly preserved: {prob_quran:.5f}")
