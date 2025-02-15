# app/classical.py

from scipy.optimize import minimize
from app.quantum import quantum_objective

def optimize_parameters(initial_params: list[float]) -> dict:
    """
    Optimize the quantum objective function using classical optimization (COBYLA).
    
    Args:
        initial_params (list[float]): Initial guess for the parameters.
        
    Returns:
        dict: A dictionary with optimal parameters and the corresponding objective value.
    """
    result = minimize(quantum_objective, initial_params, method="COBYLA")
    return {"optimal_params": result.x.tolist(), "optimal_value": result.fun}
