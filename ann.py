import numpy as np

# Input data (features)
X = np.array([[2, 9], [1, 5], [3, 6]], dtype=float)

# Output data (labels)
y = np.array([[92], [86], [89]], dtype=float)

# Normalize input data
X = X / np.amax(X, axis=0)

# Normalize output data
y = y / 100

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid function
def dersig(x):
    return x * (1 - x)

# Neural network parameters
e = 7000  # Number of epochs
lr = 0.1  # Learning rate
iln, hln, oln = 2, 3, 1  # Input, hidden, and output layer sizes

# Initialize weights and biases
wh = np.random.uniform(size=(iln, hln))
bh = np.random.uniform(size=(1, hln))
wout = np.random.uniform(size=(hln, oln))
bout = np.random.uniform(size=(1, oln))

# Training the neural network
for i in range(e):
    # Forward pass
    h1 = np.dot(X, wh)
    h = h1 + bh
    hla = sigmoid(h)
    oi1 = np.dot(hla, wout)
    oi = oi1 + bout
    op = sigmoid(oi)

    # Backpropagation
    EO = y - op
    og = dersig(op)
    dop = EO * og
    EH = dop.dot(wout.T)
    hg = dersig(hla)
    dhl = EH * hg

    # Update weights and biases
    wout += hla.T.dot(dop) * lr
    wh += X.T.dot(dhl) * lr

# Display results
print("Input: \n" + str(X))
print("Actual Output: \n" + str(y))
print("Predicted Output: \n", op)
