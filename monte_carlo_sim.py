import numpy as np
import random

def run_simulation(simulation_type, iterations=10000):
    """
    Run Monte Carlo simulation for different Islamic concepts
    
    Args:
    - simulation_type (str): Type of simulation to run
    - iterations (int): Number of simulation iterations
    
    Returns:
    - dict: Simulation results
    """
    if simulation_type == 'quran_scientific_accuracy':
        return quran_scientific_accuracy_simulation(iterations)
    elif simulation_type == 'prophet_truthfulness':
        return prophet_truthfulness_simulation(iterations)
    elif simulation_type == 'tawheed_probability':
        return tawheed_probability_simulation(iterations)
    elif simulation_type == 'quran_preservation':
        return quran_preservation_simulation(iterations)
    elif simulation_type == 'dawah_timing':
        return dawah_timing_simulation(iterations)
    else:
        return {"error": "Invalid simulation type"}

def quran_scientific_accuracy_simulation(iterations):
    """Simulate scientific accuracy of Quranic claims"""
    accurate_predictions = sum(
        1 for _ in range(iterations) 
        if random.random() < 0.95  # 95% accuracy assumption
    )
    return {
        "total_iterations": iterations,
        "accurate_predictions": accurate_predictions,
        "accuracy_percentage": (accurate_predictions / iterations) * 100
    }

def prophet_truthfulness_simulation(iterations):
    """Simulate probability of Prophet Muhammad's truthfulness"""
    truthful_instances = sum(
        1 for _ in range(iterations) 
        if random.random() < 0.99  # 99% likelihood of truthfulness
    )
    return {
        "total_iterations": iterations,
        "truthful_instances": truthful_instances,
        "truthfulness_probability": (truthful_instances / iterations) * 100
    }

def tawheed_probability_simulation(iterations):
    """Simulate monotheism probability"""
    monotheism_instances = sum(
        1 for _ in range(iterations) 
        if random.random() < 0.97  # 97% monotheism likelihood
    )
    return {
        "total_iterations": iterations,
        "monotheism_instances": monotheism_instances,
        "monotheism_probability": (monotheism_instances / iterations) * 100
    }

def quran_preservation_simulation(iterations):
    """Simulate Quran preservation probability"""
    preservation_instances = sum(
        1 for _ in range(iterations) 
        if random.random() < 0.999  # 99.9% preservation likelihood
    )
    return {
        "total_iterations": iterations,
        "preservation_instances": preservation_instances,
        "preservation_probability": (preservation_instances / iterations) * 100
    }

def dawah_timing_simulation(iterations):
    """Simulate best time for Islamic invitation"""
    optimal_times = ['morning', 'evening', 'afternoon']
    timing_results = {time: 0 for time in optimal_times}
    
    for _ in range(iterations):
        chosen_time = random.choice(optimal_times)
        timing_results[chosen_time] += 1
    
    return {
        "total_iterations": iterations,
        "timing_distribution": {
            time: (count / iterations) * 100 
            for time, count in timing_results.items()
        }
    }