# Super Demo: Alance SDK
from alance import Array, get_device, set_device
from alance.autodiff import Variable
from alance import Simulator, H, CNOT, RX

# Device
print("Device:", get_device())
try: set_device("cupy"); print("Switched to:", get_device())
except: print("Using:", get_device())

# Arrays
a, b = Array([1,2]), Array([3,4])
print("a+b =", a+b, "a*b =", a*b)

# Autodiff
x, y = Variable(2.0), Variable(5.0)
z = x*y + x; z.backward()
print("z =", z.value, "dz/dx =", x.grad, "dz/dy =", y.grad)

# Quantum
sim = Simulator(2); sim.apply_single_qubit_gate(H,0); sim.apply_cnot(0,1)
sim.apply_param_gate(RX,3.14159/2,0)
print("Quantum state:", sim.state)
print("Measure qubit 0:", sim.measure(0))
