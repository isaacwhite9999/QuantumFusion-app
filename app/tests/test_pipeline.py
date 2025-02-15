# tests/test_pipeline.py

from typing import Dict
import pytest
from app.hybrid import run_hybrid_optimization_spsa

def test_hybrid_optimization() -> None:
    """
    Test that the hybrid optimization pipeline returns valid results.
    """
    initial_params = [0.1, 0.1, 0.1]
    result: Dict[str, object] = run_hybrid_optimization_spsa(initial_params)
    assert "optimal_params" in result, "Result must contain 'optimal_params'."
    assert "optimal_value" in result, "Result must contain 'optimal_value'."
    assert isinstance(result["optimal_params"], list), "'optimal_params' should be a list."
