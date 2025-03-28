import random

num_simulations = 10000  # Number of simulations to run
predictions = 5  # Number of prophecies to test
prob_correct_prediction = 0.01  # Probability of making a correct prediction
success_count = 0  # Counter for successful simulations

# Running Monte Carlo simulation
for i in range(num_simulations):
    # Simulate random predictions about future events
    guesses = [random.random() < prob_correct_prediction for i in range(predictions)]
    
    # If all predictions are correct, count as a success
    if all(guesses):
        success_count += 1

# Calculate the probability of randomly predicting all events correctly
estimated_probability = success_count / num_simulations
print(f"The probability of a random person predicting all events correctly: {estimated_probability:.10f}")
