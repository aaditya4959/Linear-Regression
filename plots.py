import numpy as np
import matplotlib.pyplot as plt

# Defining the training dataset.
x_train = np.array([1.0, 1.7, 2.0, 2.5, 3.0, 3.2])
y_train = np.array([250, 300, 480,  430,   630, 730,])


# Now we will make a function that will compute the cost function.
def costComputer(x, y ,w, b):
    m = x.shape[0]
    cost_sum = 0
    for i in range(m):
        f_wb = w * x[i] + b
        cost = (f_wb-y[i])**2
        cost_sum = cost_sum+cost
    
    total_cost = (1/(2*m))*cost_sum

    return total_cost




