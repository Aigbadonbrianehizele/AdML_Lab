## [Week 4 / Monday] Broadcasting failure — case 1: leading axis mismatch
**Code:**
a = np.random.randn(4, 3, 32, 32)
b = np.random.randn(5, 32, 32)
result = a + b

**Exact output (verbatim):**
ValueError: operands could not be broadcast together with shapes (4,3,32,32) (5,32,32) 

**Causal WHY:**
If you notice one of the two shapes an column breaks the conditions of broadcasting
               (4, 3, 32, 32)
               (   5, 32, 32)
if you notice the third column from the right (since the broadcasting is right alignment focused) it violates the conditions of broacasting
Conditions of Broadcasting
1. In a each column broadcasting is possible if values are the same or one of the values is equal to 1(stretch).
2. For a column on the left most side(pay attention to left most) if the one of the columns is empty it has the same effect as the empty space being a value of 1 it will stretch 

Our code violates condition number 1 the third column where the values are 3 and 5 hence the traceback


## [Week 4 / Monday] Broadcasting failure — case 2: Middle axis mismatch
**Code:**
a = np.random.randn(4, 3, 32, 32)
b = np.random.randn(3, 12, 32)
result = a + b
**Exact output (verbatim):**
ValueError: operands could not be broadcast together with shapes (4,3,32,32) (3,12,32) 
**Causal WHY:**
               (4, 3, 32, 32)
               (   3, 12, 32)
If you notice the shape one of the axis doesn't obey the conditions that is the middle axis it violates condition number 1 comparing 32 and 12

## [Week 4 / Monday] Broadcasting failure — case 3: Two axis mismatch
**Code:**
a = np.random.randn(4, 3, 32, 32)
b = np.random.randn(5,7,32,32)
result = a + b
**Exact output (verbatim):**
ValueError: operands could not be broadcast together with shapes (4,3,32,32) (5,7,32,32)

**Causal WHY:**
(4, 3, 32, 32)
(5, 7, 32, 32)
Actually here two axis the axis zero and the second axis both violate the condition number 1 comparing 4 to 5, 3,7

## [Week 4 / Tuesday] SYNTHESIS
## Injection 1 — Learning Rate Too High (lr=10.0)

**Prediction (pre-run):**
For our loss function stability requires 'lr < 2/λ_max(A)', For a matrix A = [[2,2], [2,5]], its eigenvalues are `λ=1, λ=6`, so the stability has a range 2 > lr.λ > 0 or 2/λ > lr > 0, but the lr.λ is greater than 2 because lr = 10.0 and either value of lambda (1 or 6) will cause a it violate the stabilty function hence it diverges. so effectively lr.λ for both λ = 1, λ = 6 is equal to 10 and 60 respectively which is 5x to 30x the maximum constraint. For the the stability constant to be violated lr.λ must exceed the constraint 2 > lr.λ > 0  

**Command:**
A = np.array([[2.,2.],[2.,5.]]) + 1e-5
w_init = np.array([1.,3.]) + 1e-5
b = np.array([1.,5.]) + 1e-5
##trajectory = gradient_descent(lambda w: quadratic_loss(w, A, b), lambda w: quadratic_gradient(w, A, b), w_init, lr = 10.0, n_steps = 100)
print(trajectory[0][0], trajectory[1][0], trajectory[5][0], trajectory[-1][0])

**Verbatim output:**
[1.00001 3.00001] [ -69.00069 -117.00099] [-7.38819667e+08 -1.47751680e+09] [-2.13169133e+175 -4.26336987e+175]

**Causal WHY:**
The error `e_t = w_t - w*` is equivalent to `e_t = (I - lr·A)^t · e_0`. e_0 can broken down into 'c_1.v_1 + c_2.v_2' giving = 'e_0 = 0.4.v_1 + 1.03333.v_2'. Each component (c_1.v_1, c_2.v_2) is scaled by `(1-lr·λ_i)^t`, At lr = 10.0 : '(1-10.1) = -9' and '(1-10.6) = -59', absolute value of '-9' and '-59' give '9' and '59' respectively which are > 1 hence divergence, hence both component grow. The component λ=6 dominates, at t=99  using ('log10(1-lr·λ_i)xtotal_steps') which is (log10(59)*99) is ~10^175

Verified numerically 'w_1 = e_1 + w* = [-68.9998, -116.9996]' matches 'trajectory[1][0] which = [-69.00069, -117.00099]'(Rounded w* early, before deriving e_0, so the error propagated through c_1/c_2 and got amplified ~59x by t=1 — should carry exact fractions until the final numeric step.)


**Fix:**
For the gradient loss to be stable ' 0 < lr.λ < 2', but for this function lr = 10.0 and λ = 6, for this equation to be stable when lr = 10.0, '0.2 > λ > 0', or 'if λ = 6',  '1/3 > lr > 0'. But since λ is a fixed property of A only the the second half of my deduction is applicable i.e '1/3 > lr > 0'\

**Transferable principle:**
Stability of gradient descent is governed by the constraint '0 < lr·λ < 2', so its a function of lr.λ, not lr alone, as the eigenvalues of 'A' set binding constraint, so all eigenvalues must be satisfied before stability of gradient descent is met.

**Injection 2: Non-positive-definite A**
**Prediction (pre-run):**
For the loss function to be stable A must be a positive definite square matrix, hence

**Command:**
A = np.array([[-1., 0.], [0., 1.]])+ 1e-5
w_init =  np.array([1., 1.]) + 1e-5
b = np.array([0., 0.]) + 1e-5
trajectory2 = gradient_descent(lambda w: quadratic_loss(w, A, b), lambda w: quadratic_gradient(w, A, b), w_init, lr=0.1, n_steps=20)
for i, (w, loss) in enumerate(trajectory2):
    print(i, w, loss)

**Verbatim output:**
0 [1.00001 1.00001] 2.0000205149729613e-10
1 [1.10001  0.900008] -0.20000379983399896
2 [1.21001   0.8100062] -0.4040068758462995
3 [1.33100998 0.72900456] -0.6200693409805828
4 [1.46410992 0.65610304] -0.8565720493545476
5 [1.61051979 0.59049162] -1.1225446077884558
6 [1.77157057 0.53144126] -1.4280127440082366
7 [1.94872632 0.47829583] -1.7843785060300652
8 [2.14359753 0.43046482] -2.204847809196128
9 [2.3579557  0.38741676] -2.704921447565438
10 [2.59374953 0.34867334] -3.302967897802595
11 [2.85312254 0.31380406] -4.02089914242209
12 [3.13843263 0.28242149] -4.884974427215478
13 [3.45227347 0.25417692] -5.926761476353722
14 [3.79749811 0.22875652] -7.184290383577625
15 [4.17724489 0.20587784] -8.70344238467146
16 [4.594966   0.18528668] -10.539624248118376
17 [5.05445882 0.16675423] -12.759789407124819
18 [5.55990048 0.15007458] -15.444879574574585
19 [6.11588582 0.13506242] -18.692775891976122

**Causal WHY:**
[eigen-decomposition of A_bad, what happens per-eigendirection, why one direction behaves differently from the other]
A has eigenvalues 'λ = -1' and 'λ = +1'. For each eigenvalue the per step scaling factor is (1-lr·λ_i), when you plug in the negative eigenvalue 'λ = -1' into '|1-lr·λ_i| < 1' the result is '1.1 < 1', which  is false forcing the scaling factor to be greater than 1 meaning it causes divergence, plugging in the positive eigenvalue 'λ = +1' into '|1-lr·λ_i| < 1' the result is '0.9 < 1' which is true so this obeys the constraint for convergence, but for true convergence both eigenvalues must obey the constraint or else the entire loss function diverges.

**Fix:**
This isn't a bug to patch in the code as the input is the violating the pre condition gradient_descent assumes.

**Transferable principle:**
When analyzing this is specific instance on a graph you notice the loss function continues to decrease, the two components of w move in opposite direction for each loss function on the graph. This behaviour is not decided by the loss trend, its described by the eigenvalues of A, as there are postive and negative values for eigenvalues hence the '|1-lr·λ_i| < 1' converges at point 'λ = 1', and diverges at the point 'λ = -1' , so the net effect is divergence and this cause the corresponding weight components to travel in opposing direction whilst loss function tends to negative infinity.

## Injection 2 — Non-Positive-Definite A

**Prediction (pre-run):**
I expected the value of difference between w components of numerical_gradients and quadratic_gradient to be within range of O(h²) 
**Command:**
A = np.array([[2,2],[2,5]])
w = np.array([2., -3.])
b = np.array([1,5])

analytical = quadratic_gradient(w, A, b)
wrapped = lambda w: quadratic_loss(w, A, b)
numerical = numerical_gradient(wrapped, w)
diff = analytical - numerical
fahh =  np.max(np.abs(diff))
fahhhhh = np.allclose(analytical, numerical, rtol= 0 , atol= 1e-4)

print("MAXIMUM:",fahh)
print('Difference:',diff)
print('CHECK:',fahhhhh)

**Verbatim output:**
MAXIMUM: 1.1357359497310426e-10
Difference: [-1.13573595e-10  1.04819264e-10]
CHECK: True

**Causal WHY:**
The resultant(~1e-10) is the expected O(h²) error of the central difference at h = 1e-5, not a bug - thus the analytical gradient is confirmed correct.

**Fix:**
No bug was found. Analytical gradient matched the Numerical gradient within the O(h²) expected error at h = 1e-5.

**Transferable principle:**
Because numerical_gradient never touches the analytical formula, it only manipulates w and reads the loss function, a bug in the quadratic_gradient can't reproduce itself there, which is why comparing to independent methods catches errors that re-deriving formulas wouldn't. The two methods aren't fully independent, though both ultimately depend on quadratic_loss being correct, so a bug shared upstream would pass this check undetected from both methods.

**M2 connection:**

## Injection 4 — momentum=0.99

**Prediction (pre-run):**
None -  I ran the injection without prior prediction. I should have committed a prediciton in log.md before running the injection.

**Command:**
trajectory3 = sgd_with_momentum(lambda w: quadratic_loss(w, A, b), lambda w: quadratic_gradient(w, A, b), w_init = w, momentum=0.99)
print('t = 1',trajectory3[0])
print('t = 2',trajectory3[1])
print('t = 25',trajectory3[24])
print('t = 50',trajectory3[49])
print('t = 100',trajectory3[99])
print('t = 10000',trajectory3[9999])
print('t = 4',trajectory3[5])

**Verbatim output:**
t = 1 (array([ 2., -3.]), np.float64(27.5))
t = 25 (array([-1.44863149, -0.52948099]), np.float64(8.429490601976584))
t = 50 (array([-3.7947291 ,  3.30470412]), np.float64(3.892936952108352))
t = 100 (array([2.08485036, 1.20478955]), np.float64(4.890209383368752))
t = 10000 (array([-0.83333333,  1.33333333]), np.float64(-2.9166666666666665))
w* (computed): [-0.83333333,  1.33333333]
L(w*) (computed): [-2.9166666666666665]

**Causal WHY:**
Based on the constraints '|1-lr·λ_i| < 1' with both eigenvalues(positive) the constraint is obeyed the injection should converge. However hewe used "v_new = momentum*v_old + grad and w = w - lr*v_new" momentum" update instead 'w = w - lr*grad' standard gradient. Early gradients build up v, causing w to overshoot past w*(the minimum point where grad=0). Once w overshoots, the gradient flips sign but v_new is still dominated by momentum*v_old, so v_new takes several steps to reverse, causing w to swing back past w* the other way
This produces oscillation amplitude (||w-w*||) that's across every step rather than staying constant:
- t=25: w=[-1.449, -0.529], loss=8.43
- t=1001: w=[-0.852, 1.322], loss=-2.9156
- t=3001: w=[-0.8333238, 1.3333238], loss=-2.9166666666653
- t=10000: w=[-0.8333333, 1.3333333], loss=-2.9166666666667

As w_new approaches w*, grad approaches 0, so v_new becomes dominated by momentum*v_old with grad basically adding little as it approaches zero, v decays, oscillation amplitude decays towards zero as 
t→∞, w never reaches w* in a finite step


**Fix:**
No bug was found.

**Transferable principle:**
Momentum can satisfy the same stability condition (|1-lr·λ_i|<1) as plain gradient descent and still converge, but it reaches the minimum through decaying oscillation rather than a direct path, because momentum*v_old dominates v_new near the point of overshoot, delaying the sign reversal by several steps.


(4, 3, 32, 32)
(5, 7, 32, 32)
Actually here two axis the axis zero and the second axis both violate the condition number 1 comparing 4 to 5, 3,7

