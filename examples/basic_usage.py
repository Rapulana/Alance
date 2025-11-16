from alance import Array, set_device, get_device
from alance import Simulator, Qubit, H, X, CNOT, RX, RZ, measure
from alance.autodiff import Variable

print('Default device:', get_device())
# try GPU if available (optional)
try:
    set_device('cupy')
    print('Switched to device:', get_device())
except Exception as e:
    print('GPU not available, using', get_device())

# Array usage
a = Array([1,2,3])
b = Array([4,5,6])
print('Array add:', a + b)

# Autodiff tiny example
x = Variable(2.0)
y = Variable(3.0)
z = x * y + x
z.backward()
print('z.value=', z.value, 'dx=', x.grad, 'dy=', y.grad)

# Quantum usage
sim = Simulator(2)
sim.apply_single_qubit_gate(H, target=0)
sim.apply_cnot(control=0, target=1)
print('State vector (2-qubit):', sim.state)
m = sim.measure(0)
print('Measured qubit0 =', m)
