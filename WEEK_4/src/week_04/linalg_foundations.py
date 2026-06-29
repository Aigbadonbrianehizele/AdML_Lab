import numpy as np

def vector_add(a,b):
    a = np.array(a)
    b = np.array(b)
    if a.shape != b.shape:
        raise ValueError(f"{a} and {b} are not the same shape")
    else:
        return a + b

def scalar_vector(s, v):
    v = np.array(v)
    return s * v

def dot_product(a, b):
    a = np.array(a)
    b = np.array(b)
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result



def l1_norm(v):
    result = 0
    v = np.array(v)
    for i in range(len(v)):
        result += abs(v[i])
    return result

def l2_norm(v):
    result = 0
    v = np.array(v)
    for i in range(len(v)):
        result += abs(v[i])**2
    return result**0.5

def linf_norm(v):
    v = np.array(v)
    result = max(abs(v))
    return result

def add_bounded_perturbation(x, delta, epsilon, norm='linf') -> np.ndarray :
    norm_map ={'linf':linf_norm, 'l1':l1_norm,'l2':l2_norm}
    x = np.array(x)
    delta = np.array(delta)
    if norm_map[norm](delta) > epsilon:
        raise ValueError(f"the value of {delta} is greater the value of epsilon {epsilon}")
    else:
        x_adv = x + delta
        return x_adv

x = np.array([0.2, 0.4, 0.6, 0.8])
delta = np.array([0.05, -0.05, 0.05, -0.05])
print('L1:', l1_norm(delta))
print('L2:', l2_norm(delta))
print('Linf:', linf_norm(delta))
print('x_adv:', add_bounded_perturbation(x, delta, epsilon=0.01, norm='linf'))
    






    