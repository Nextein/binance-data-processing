import pandas as pd
import numpy as np
# Create features

# pp.preprocess_candles('2h')
data = pd.read_csv("2h_BTC_candle_shape.csv").values
N = data.shape[0]
F = data.shape[1]


def labels(c1, c2):
    """
    Creates a label (1 or 0) from 2 candles
    :param c1: candle 1
    :param c2: candle 2
    :return: 1 or 0
    """
    if (c2[1] - c1[0]) >= 0:
        return 1    # green bar
    else:
        return 0


X = []
Y = []

for i in range(N-6):
    x = [data[i, :], data[i+1, :], data[i+2, :], data[i+3, :]]
    X.append(x)
    y = labels(data[i+4], data[i+5])
    Y.append(y)

Y = np.array(Y)
print(len(X))
# Deep-Q Learning NN

# TODO -  Q-Learning NN for candle shapes -> Library for this?


def sigmoid(x, deriv=False):
    # if deriv:
    #     return x*(1-x)
    # return 1/(1+np.exp(-x))
    if deriv:
        a = x*(1-x)
        return np.array(a)
    else:
        X = []
        for j in range(len(x)):
            X.append(1/(1+np.exp(-x[j])))
            u = x[j]
        print(u)
        return np.array(X)


# X = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])       4x3
# y = np.array([[0,0,1,1]]).T                           4x1

training_iterations = 100

np.random.seed(1)

# Synapses
syn0 = np.random.random((4,  1)) - 1                  # 3x1
# syn1 = 2*np.random.random((9,  12)) - 1
# syn2 = 2*np.random.random((12, 12)) - 1
# syn3 = 2*np.random.random((12, 9)) - 1
# syn4 = 2*np.random.random((9,  4)) - 1
# syn5 = 2*np.random.random((4,  1)) - 1

l6_error = 0
l6 = 0
for i in range(training_iterations):
    l0 = X
    l6 = sigmoid(np.dot(l0, syn0))
    # l2 = sigmoid(np.dot(l1, syn1))
    # l3 = sigmoid(np.dot(l2, syn2))
    # l4 = sigmoid(np.dot(l3, syn3))
    # l5 = sigmoid(np.dot(l4, syn4))
    # l6 = sigmoid(np.dot(l5, syn5))

    l6_error = Y-l6  # Should get smaller and smaller as we train
    print(Y.shape)
    print(l6.shape)
    print(X)

    l6_delta = l6_error * sigmoid(l6, True)

    # Updates weights in our network
    # syn0 += np.dot(l0,l6_delta)

totalError = np.sum(l6_error)

print(len(Y))
print(Y[0])
print(len(l6))
print(np.column_stack(Y, l6))




