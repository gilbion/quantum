from IPython.display import Image, display
from qiskit import *
from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import Unroller

# create a logical function to perform the NOT operator against a single qubit
def Lnot(qCircuit, qc, qbit):
   qCircuit.x(qc[qbit])
   qCircuit.barrier(qc);

# create a logical function to perform the AND operator against two input bits and one output bit
def Land(qCircuit, qc, qbit1, qbit2, qbit3):
   qCircuit.ccx(qc[qbit1], qc[qbit2], qc[qbit3])
   qCircuit.barrier(qc);

# create a logical function to perform the NAND operator against two input bits and one output bit
def Lnand(qCircuit, qc, qbit1, qbit2, qbit3):
   qCircuit.ccx(qc[qbit1], qc[qbit2], qc[qbit3])
   qCircuit.x(qc[qbit3])
   qCircuit.barrier(qc);

# create a logical function to perform the OR operator against two input bits and one output bit
def Lor(qCircuit, qc, qbit1, qbit2, qbit3):
   qCircuit.cx(qc[qbit1], qc[qbit3])
   qCircuit.cx(qc[qbit2], qc[qbit3])
   qCircuit.ccx(qc[qbit1], qc[qbit2], qc[qbit3])
   qCircuit.barrier(qc);

# create a logical function to perform the XOR operator against two input bits and one output bit
def Lxor(qCircuit, qc, qbit1, qbit2, qbit3):
   qCircuit.cx(qc[qbit1], qc[qbit3])
   qCircuit.cx(qc[qbit2], qc[qbit3])
   qCircuit.barrier(qc);

# create a logical function to perform the NOR operator against two input bits and one output bit
def Lnor(qCircuit, qc, qbit1, qbit2, qbit3):
   qCircuit.cx(qc[qbit1], qc[qbit3])
   qCircuit.cx(qc[qbit2], qc[qbit3])
   qCircuit.ccx(qc[qbit1], qc[qbit2], qc[qbit3])
   qCircuit.x(qc[qbit3])
   qCircuit.barrier(qc);



def QSum(qCircuit, qc, qbit1, qbit2, qbit3, qbitr1, qbitr2):
   result1 = Lxor(qCircuit, qc, qbit1, qbit2, qbitr1)
   qCircuit.cx(qc[qbit3], qbitr1)
   result2 = Land(qCircuit, qc, qbit1, qbit2, qbitr2)
   result2 = Land(qCircuit, qc, qbit1, qbit3, qbitr2)
   result2 = Land(qCircuit, qc, qbit2, qbit3, qbitr2)
   qCircuit.barrier(qc);

q = QuantumRegister(5)
c = ClassicalRegister(2)
qc = QuantumCircuit(q,c)
# qc.x(q[1])
qc.x(q[0])
qc.x(q[2])
result1 = QSum(qc, q, 0, 1, 2, 3, 4)
qc.measure(q[3], c[0])
qc.measure(q[4], c[1])


backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1000)
result = job.result()
count =result.get_counts()
print(count)


pass_ = Unroller(['u3', 'cx'])
pm = PassManager(pass_)
new_circuit = pm.run(qc) 
print(new_circuit.count_ops())