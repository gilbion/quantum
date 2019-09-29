from qiskit import *

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