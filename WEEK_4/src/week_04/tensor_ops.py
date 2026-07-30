import numpy as np
x = np.random.randn(4, 3, 32, 32)
delta = np.random.randn(1, 3, 32, 32) * 0.05
x_adv = x + delta 

def flatten_batch(x: np.ndarray) -> np.ndarray:
    flattened_batch = x.reshape(x.shape[0],-1)
    return flattened_batch

def channel_mean(x: np.ndarray) -> np.ndarray:
    mean = x.mean(axis=(0,2,3))
    return mean

def normalize(x, mean, std) -> np.ndarray:
    reshaped_mean = mean.reshape(mean.shape[0],1,1)
    reshaped_std = std.reshape(std.shape[0],1,1)
    normalized = x - reshaped_mean
    division = normalized / reshaped_std
    return division
x = np.array([[[[1,2],[3,4]], [[5,6],[7,8]], [[9,10],[11,12]]],[[[2,2],[2,2]], [[3,3],[3,3]], [[4,4],[4,4]]]])

def batch_matmul_einsum(A, B):
    return np.einsum('bik,bkj->bij', A, B)

def outer_product_einsum(a, b):
    return np.einsum('i,j->ij', a, b)

def trace_einsum(A):
    return np.einsum('ii->', A)

#x_3 = np.random.rand(4,3 ,3)
#x_2 = np.random.rand(4,3 ,5) 
#print(np.allclose(batch_matmul_einsum(x_3,x_2),np.matmul(x_3,x_2)))

#x_1 = np.random.rand(3)
#x_5 = np.random.rand(3)
#print(np.allclose(outer_product_einsum(x_1, x_5),np.outer(x_1,x_5)))

#x_6 = np.random.rand(3 ,3)
#print(np.allclose(trace_einsum(x_6),np.trace(x_6)))

#print(flatten_batch(x).shape)      # expect (2, 12)
#print(channel_mean(x))             # expect [2.25, 4.75, 7.25]
