import numpy as np
def numerical_gradient(f, x: np.ndarray, h=1e-5) -> np.ndarray:
    x =  x.astype(float)
    finite_difference = np.zeros_like(x)
    for i in np.ndindex(x.shape):
        og_value = x[i]
        x[i] = og_value + h
        forward = f(x)
        x[i] = og_value - h
        backward = f(x)
        finite_difference[i] = (forward - backward)/(2 * h)
        x[i] = og_value
    return finite_difference

def mse_loss(y_pred: np.ndarray, y_true: np.ndarray) -> float:
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    n = y_pred.size
    L = (1/n) * np.sum((y_pred - y_true)**2)
    return L

def mse_loss_gradient(y_pred: np.ndarray, y_true: np.ndarray) -> np.ndarray:
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    n = y_pred.size
    L_prime = (2/n) *(y_pred - y_true)
    return L_prime

def jacobian(f, x: np.ndarray, h=1e-5) -> np.ndarray:
    function = f(x)
    m = function.size
    n = x.size
    jacobian_matrix = np.zeros((m,n))
    for i in range(m):
        derivative = lambda x: f(x)[i]
        jacobian_matrix[i] = numerical_gradient(derivative, x)
    return jacobian_matrix

## lamba does the job of creatting a function instead of calling 
##def derivative(x):
##    return f(x)[i] we jusy use lambda x: f(x)[i]




y_pred=[2.1, 0.5, 1.8]
y_true=[2.0, 1.0, 2.0]
W = np.random.randn(3, 4)
f = lambda x: W @ x
x = np.random.randn(4)
J = jacobian(f, x)

if __name__ == "__main__":
    print(mse_loss(y_pred, y_true))
    print(mse_loss_gradient(y_pred, y_true))
    print(J)
    print('Jacobian matches W:', np.allclose(J, W, atol=1e-4))
    







