# app/quantum.py

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.opflow import I, X, Z

# Define a Hamiltonian: H = (I⊗Z) + (Z⊗I) + (X⊗X)
H = (I ^ Z) + (Z ^ I) + (X ^ X)

def build_ansatz(params: list[float]) -> QuantumCircuit:
    """
    Build a parameterized quantum circuit (ansatz) for 2 qubits.
    
    Args:
        params (list[float]): List of circuit parameters.
    
    Returns:
        QuantumCircuit: A 2-qubit variational circuit.
    """
    qc = QuantumCircuit(2)
    qc.rx(params[0], 0)
    qc.rx(params[1], 1)
    qc.cx(0, 1)
    qc.rz(params[2], 0)
    qc.barrier()
    return qc

def quantum_objective(params: list[float]) -> float:
    """
    Evaluate the expectation value of the Hamiltonian H with respect to the
    state prepared by the ansatz.
    
    Args:
        params (list[float]): Parameters for the variational circuit.
    
    Returns:
        float: The expectation value (objective to be minimized).
    """
    qc = build_ansatz(params)
    state = Statevector.from_instruction(qc)
    # Compute expectation value using the operator matrix representation
    expectation = state.expectation_value(H.to_matrix()).real
    return expectation
