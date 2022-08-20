from ...base.entropy_source import EntropySource
from qiskit import QuantumCircuit, transpile, Aer
import numpy as np

class UniversalQCSampler(EntropySource):
    
    def __init__(self, **kwargs):
        nb_qubits = kwargs.get("nb_qubits")
        operation = kwargs.get("operation")
        angle = kwargs.get("angle")

        if operation is None or operation == "hadamard":
            self.operation = "hadamard"
        elif operation == "rotation":
            if angle is None:
                raise ValueError("You must define an angle when choosing the 'rotation' operation.")
                
            self.angle = angle
            self.operation = "rotation"
        
        self.nb_qubits = 5 if nb_qubits is None else nb_qubits

        self.dep_seq_len = 1
        self.seq_len = nb_qubits

    def _simulate(self, length):

        shots = np.max([length // self.nb_qubits, 2])

        qc = QuantumCircuit(self.nb_qubits)
        for i in range(self.nb_qubits):
            if self.operation == "hadamard":
                qc.h(i)
            elif self.operation == "rotation":
                qc.ry(self.angle, i)
            else:
                raise NotImplemented("Defined operation not implemented yet!")
        qc.measure_all()

        # Transpile for simulator
        simulator = Aer.get_backend('aer_simulator')
        transpiled_qc = transpile(qc, simulator)
        result = simulator.run(transpiled_qc, shots = shots, memory = True).result()
        return result.get_memory(transpiled_qc)

    def sample(self, length):
        memory = self._simulate(length)

        bitstring_str = "".join(memory)

        return np.array(list(bitstring_str)).astype(np.int8)