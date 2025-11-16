import numpy as np
from alance import Array, Simulator, H
from alance.autodiff import Variable

def test_array_add():
    a = Array([1,2])
    b = Array([3,4])
    c = a + b
    assert (c.to_numpy() == np.array([4,6])).all()

def test_hadamard_superposition():
    sim = Simulator(1)
    sim.apply_single_qubit_gate(H, target=0)
    probs = np.abs(sim.state)**2
    assert np.isclose(probs[0], 0.5, atol=1e-6)
    assert np.isclose(probs[1], 0.5, atol=1e-6)

def test_autodiff_mul():
    x = Variable(4.0)
    y = Variable(5.0)
    z = x * y
    z.backward()
    assert abs(x.grad - 5.0) < 1e-8
    assert abs(y.grad - 4.0) < 1e-8
