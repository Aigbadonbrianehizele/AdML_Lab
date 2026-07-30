import numpy as np
from week_04.gradients import numerical_gradient
def quadratic_loss(w: np.ndarray, A: np.ndarray, b: np.ndarray) -> float:
    L_w = 0.5 * (w.T @ A @ w) - b.T @ w
    return L_w 

def quadratic_gradient(w: np.ndarray, A: np.ndarray, b: np.ndarray) -> np.ndarray:
    grad_L_w = A @ w - b
    return grad_L_w

def gradient_descent(loss_fn, grad_fn, w_init, lr=0.1, n_steps=100) -> list:
    w = w_init
    descent = []
    for i in range(n_steps):
        loss = loss_fn(w)
        grad = grad_fn(w)
        descent.append((w, loss))
        w = w - lr*grad
    return descent

def sgd_with_momentum(loss_fn, grad_fn, w_init, lr=0.1, momentum=0.9, n_steps=400000) -> list:
    w = w_init
    speedometer = []
    v = 0
    for i in range(n_steps):
        loss = loss_fn(w)
        grad = grad_fn(w)
        speedometer.append((w, loss))
        v = momentum*v + grad
        w = w - lr*v
    return speedometer

#A = np.array([[2.,2.],[2.,5.]])
#w_init = np.array([1.,3.]) 
#b = np.array([1.,5.]) 
#trajectory1 = gradient_descent(lambda w: quadratic_loss(w, A, b), lambda w: quadratic_gradient(w,A,b), w_init, lr=10.0)      
##trajectory = sgd_with_momentum(lambda w: quadratic_loss(w, A, b), lambda w: quadratic_gradient(w,A,b), w_init, lr = 0.1, momentum = 0.9, n_steps = 100)
##print(trajectory[0])
#w_star = np.linalg.solve(A ,b)
##print(w_star)
#final_momentum = trajectory[-1][0]
##print(final_momentum)
##print("converged within 1e-4:", np.allclose(final_momentum, w_star, atol=1e-4))
##print(trajectory[-5:])

##print(trajectory1[-1][0])
A = np.array([[2,2],[2,5]])
w = np.array([2., -3.])

b = np.array([1,5])

##trajectory = gradient_descent(lambda w: quadratic_loss(w, A, b), lambda w: quadratic_gradient(w, A, b), w_init, lr = 0.01, n_steps = 100000)
##print(trajectory)
#w_star = np.linalg.solve(A,b)
#print("analytical:", w_star)
#print("final w:", trajectory[-1][0])
#print(np.allclose(trajectory[-1][0], w_star, atol=1e-4))
##trajectory2 = gradient_descent(lambda w: quadratic_loss(w, A, b), lambda w: quadratic_gradient(w, A, b), w_init, lr=0.1, n_steps=20)
##for i, (w, loss) in enumerate(trajectory2):
##    print(i, w, loss)

##analytical = quadratic_gradient(w, A, b)
##wrapped = lambda w: quadratic_loss(w, A, b)
##numerical = numerical_gradient(wrapped, w)
##diff = analytical - numerical
##fahh =  np.max(np.abs(diff))
##fahhhhh = np.allclose(analytical, numerical, rtol= 0 , atol= 1e-4)

##print("MAXIMUM:",fahh)
##print('Difference:',diff)
##print('CHECK:',fahhhhh)
#trajectory3 = sgd_with_momentum(lambda w: quadratic_loss(w, A, b), lambda w: quadratic_gradient(w, A, b), w_init = w, momentum=0.99)
#print('t = 1',trajectory3[0])
#print('t = 2',trajectory3[1])
#print('t = 25',trajectory3[24])
#print('t = 50',trajectory3[49])
#print('t = 100',trajectory3[99])
#print('t = 10000',trajectory3[99])
#print('t = 4',trajectory3[300000])

