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

print(flatten_batch(x).shape)      # expect (2, 12)
print(channel_mean(x))             # expect [2.25, 4.75, 7.25]
