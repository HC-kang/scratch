import numpy as np

def identity_function(x):
    return x

def step_function(x):
    return int(x>0)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def softmax(x):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

def relu(x):
    return np.maximum(0, x)

