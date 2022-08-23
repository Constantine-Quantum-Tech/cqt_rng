from ...base.entropy_source import EntropySource

from qiskit import IBMQ, Aer
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, assemble, transpile
from qiskit.tools.monitor import job_monitor

import numpy as np


class IBMQSampler(EntropySource):
    """Sample taken from a IBMQ device.

    Parameters:
        operation ("rotation" | "hamadard", optional): the gate applied on the qubits. Defaults to hadamards.
        angle (float, optional): the rotation angle (around y-axis). Necessary in the case the operation is rotation.
    """

    def __init__(self, **kwargs):
        self.name = "IBMQSampler"
        operation = kwargs.get("operation")
        angle = kwargs.get("angle")

        if operation is None or operation == "hadamard":
            self.operation = "hadamard"
        elif operation == "rotation":
            if angle is None:
                raise ValueError(
                    "You must define an angle when choosing the 'rotation' operation."
                )

            self.angle = angle
            self.operation = "rotation"

        IBMQ.load_account()
        provider = IBMQ.get_provider(hub="ibm-q")
        self.backend = least_busy(
            provider.backends(
                filters=lambda x: x.configuration().n_qubits >= 1
                and not x.configuration().simulator
                and x.status().operational == True
            )
        )
        print("least busy backend: ", self.backend)
        print("Number of qubits: ", self.backend.configuration().n_qubits)

        self.nb_qubits = self.backend.configuration().n_qubits
        self.dep_seq_len = 1
        self.seq_len = self.nb_qubits

    def _execute(self, length):

        print(f"Running the job on {self.backend} with {self.nb_qubits} qubits!")

        shots = np.max([2 * length // self.nb_qubits, 2])

        qc = QuantumCircuit(self.nb_qubits)
        for i in range(self.nb_qubits):
            if self.operation == "hadamard":
                qc.h(i)
            elif self.operation == "rotation":
                qc.ry(self.angle, i)
            else:
                raise NotImplemented("Defined operation not implemented!")
        qc.measure_all()

        transpiled_qc = transpile(qc, self.backend, optimization_level=3)
        job = self.backend.run(transpiled_qc, shots=shots, memory=True)
        job_monitor(job, interval=2)

        return job.result().get_memory(transpiled_qc)

    def sample(self, length):
        memory = self._execute(length)

        bitstring_str = "".join(memory)

        return np.array(list(bitstring_str)).astype(np.int8)[:length]
