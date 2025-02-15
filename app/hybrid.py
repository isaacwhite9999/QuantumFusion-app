# app/hybrid.py

import logging
from app.spsa_optimizer import spsa_optimize
from app.quantum import quantum_objective

logger = logging.getLogger(__name__)

def run_hybrid_optimization_spsa(initial_params: list[float]) -> dict:
    """
    Run the hybrid quantum-classical optimization pipeline using SPSA.
    
    Args:
        initial_params (list[float]): Initial parameters for the quantum ansatz.
        
    Returns:
        dict: Optimization results including optimal parameters and the objective value.
    """
    logger.info("Starting hybrid quantum-classical optimization using SPSA.")
    result = spsa_optimize(quantum_objective, initial_params)
    logger.info("SPSA optimization complete.")
    return result
