from qiskit_experiments.library import T1
from qiskit.providers.fake_provider import FakePerth
from qiskit_aer import AerSimulator
import numpy as np

backend = AerSimulator.from_backend(FakePerth())

qubit0_t1 = FakePerth().qubit_properties(0).t1
delays = np.arange(1e-6, 3 * qubit0_t1, 3e-5)

exp = T1(physical_qubits=(0,), delays=delays)

print(delays)
exp.circuits()[0].draw(output="mpl", style="iqp")

#exp.circuits()[-1].draw(output="mpl", style="iqp")
