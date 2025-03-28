import random

num_simulations = 10000  # Number of universes simulated
num_gods = 3  # Number of gods making decisions
num_laws = 5  # Number of fundamental physical laws
stability_threshold = 0.8  # Probability of a stable law agreement
stable_universes = 0  # Counter for stable universes

# Running Monte Carlo simulation
for i in range(num_simulations):
    # Simulate gods choosing different laws
    laws = [[random.choice([0, 1]) for i in range(num_laws)] for i in range(num_gods)]

    # Check for conflicts (instability if gods disagree too much)
    stable_laws = sum(all(law[j] == laws[0][j] for law in laws) for j in range(num_laws))
    
    # If most laws are stable, count as a successful universe
    if stable_laws / num_laws >= stability_threshold:
        stable_universes += 1

# Calculate probability of a stable universe with multiple gods
estimated_probability = stable_universes / num_simulations
print(f"Probability of a stable universe with multiple gods: {estimated_probability:.10f}")
