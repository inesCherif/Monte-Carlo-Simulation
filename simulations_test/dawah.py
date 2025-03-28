import random
num_simulations = 10000  # Number of individuals simulated
time_slots = ["Morning", "Afternoon", "Evening", "Night"]
life_events = ["Normal Day", "Personal Loss", "Major Reflection", "Life Success"]
# Probabilities of being receptive based on time and events
receptiveness_base = {"Morning": 0.2, "Afternoon": 0.3, "Evening": 0.4, "Night": 0.35}
receptiveness_life_event = {"Normal Day": 0, "Personal Loss": 0.5, "Major Reflection": 0.6, "Life Success": 0.3}
# Count for each category
receptive_counts = {key: 0 for key in time_slots + list(receptiveness_life_event.keys())}
# Running Monte Carlo simulation
for i in range(num_simulations):
    time = random.choice(time_slots)
    event = random.choices(list(receptiveness_life_event.keys()), weights=[0.7, 0.1, 0.15, 0.05])[0]
    # Calculate receptiveness
    receptive_probability = receptiveness_base[time] + receptiveness_life_event[event]
    if random.random() < receptive_probability:
        receptive_counts[time] += 1
        receptive_counts[event] += 1
# Normalize results
for key in receptive_counts:
    receptive_counts[key] /= num_simulations
# Output results
print("Receptiveness Probability by Time of Day:")
for time in time_slots:
    print(f"{time}: {receptive_counts[time]:.2%}")
print("\nReceptiveness Probability by Life Event:")
for event in life_events:
    print(f"{event}: {receptive_counts[event]:.2%}")
