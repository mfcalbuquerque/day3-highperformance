import numpy as np

def calc_pi_device(samples):
    x = np.random.random(size=samples)
    y = np.random.random(size=samples)
    within_unit_circle = (x*x + y*y) < 1.0
    return print(4.0 * sum(within_unit_circle)/samples)

calc_pi_device(1000000)
