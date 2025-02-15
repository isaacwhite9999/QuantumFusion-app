# app/spsa_optimizer.py

import numpy as np
from typing import Callable, List, Dict

def spsa_optimize(
    objective: Callable[[List[float]], float],
    initial_params: List[float],
    max_iterations: int = 100,
    a: float = 0.1,
    c: float = 0.1,
    A: float = 10.0,
    alpha: float = 0.602,
    gamma: float = 0.101,
) -> Dict[str, object]:
    """
    Optimize the given objective function using the Simultaneous Perturbation Stochastic Approximation (SPSA) algorithm.
    
    Args:
        objective (Callable[[List[float]], float]): The objective function to minimize.
        initial_params (List[float]): Initial guess for the parameters.
        max_iterations (int): Maximum number of iterations.
        a (float): Learning rate coefficient.
        c (float): Perturbation coefficient.
        A (float): Stability constant for learning rate.
        alpha (float): Exponent for learning rate decay.
        gamma (float): Exponent for perturbation decay.
        
    Returns:
        Dict[str, object]: A dictionary containing the optimal parameters and the corresponding objective value.
    """
    params = np.array(initial_params, dtype=float)
    dim = len(params)
    
    for k in range(max_iterations):
        ak = a / ((k + 1 + A) ** alpha)
        ck = c / ((k + 1) ** gamma)
        # Generate a random perturbation vector with entries +1 or -1
        delta = np.random.choice([-1, 1], size=dim)
        params_plus = params + ck * delta
        params_minus = params - ck * delta
        
        # Evaluate the objective function at perturbed points
        y_plus = objective(params_plus.tolist())
        y_minus = objective(params_minus.tolist())
        
        # Estimate the gradient using the two measurements
        gk = (y_plus - y_minus) / (2.0 * ck) * delta
        
        # Update the parameters
        params = params - ak * gk
        
    optimal_value = objective(params.tolist())
    return {"optimal_params": params.tolist(), "optimal_value": optimal_value}
