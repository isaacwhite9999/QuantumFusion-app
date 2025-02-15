# app/pipeline.py

import argparse
import asyncio
import logging
from typing import List

from app.config import settings
from app.hybrid import run_hybrid_optimization_spsa

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

async def main_async(args: argparse.Namespace) -> None:
    """
    Asynchronous entrypoint to run the hybrid optimization pipeline using SPSA.
    """
    # Parse initial parameters from comma-separated string
    initial_params: List[float] = [float(x) for x in args.initial_params.split(",")]
    result = run_hybrid_optimization_spsa(initial_params)
    print("Optimization Result (SPSA):")
    print("Optimal Parameters:", result["optimal_params"])
    print("Optimal Value:", result["optimal_value"])

def main() -> None:
    parser = argparse.ArgumentParser(
        description="QuantumFusion: Hybrid Quantum-Classical Optimization Platform (SPSA)"
    )
    parser.add_argument(
        "--initial_params",
        type=str,
        required=False,
        default=settings.INITIAL_PARAMETERS,
        help="Comma-separated initial parameters (e.g., '0.1,0.1,0.1')"
    )
    args = parser.parse_args()
    asyncio.run(main_async(args))

if __name__ == "__main__":
    main()
