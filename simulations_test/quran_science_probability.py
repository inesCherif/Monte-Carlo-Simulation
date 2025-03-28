import random

# Define the number of correct scientific facts in the Quran for example, 10
correct_facts = 10  

# Define the probability of randomly guessing each fact correctly
prob_correct_guess = 0.001  

# Number of Monte Carlo simulations
num_simulations = 10_000  

# Count how many times a book randomly gets all facts correct
success_count = 0

for i in range(num_simulations):
    # Simulate a book making 'correct_facts' number of guesses
    guesses = [random.random() < prob_correct_guess for i in range(correct_facts)]
    
    # If all guesses are correct, count as a success
    if all(guesses):
        success_count += 1

# Calculate the probability of randomly getting all facts correct
estimated_probability = success_count / num_simulations

# Display the result
print(f"After {num_simulations} simulations, the probability of a random book from the 7th century "
      f"guessing all {correct_facts} facts correctly is approximately {estimated_probability:.10f}")
