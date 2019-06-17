import numpy as np
import pandas as pd
from sklearn import *
import matplotlib.pyplot as plt

n_candles_per_sample = 4


def plot_matrix(matrix, ax=None):
    """
    Displays a given matrix as an image.

    Args:
        - matrix: the matrix to be displayed
        - ax: the matplotlib axis where to overlay the plot.
          If you create the figure with `fig, fig_ax = plt.subplots()` simply pass `ax=fig_ax`.
          If you do not explicitily create a figure, then pass no extra argument.
          In this case the  current axis (i.e. `plt.gca())` will be used
    """
    if ax is None:
        ax = plt.gca()

    handle = ax.imshow(matrix, cmap=plt.get_cmap('summer'))
    plt.colorbar(handle)

    n_rows, n_cols = matrix.shape
    for i in range(0, n_rows):
        for j in range(0, n_cols):
            plt.text(j, i, matrix[i][j])


def calculate_confusion_matrix(gt_labels, pred_labels):
    classes = len(np.unique(gt_labels))
    length = len(gt_labels)

    result = np.zeros((classes, classes))

    for i in range(0, length):
        result[gt_labels[i] - 1][pred_labels[i] - 1] += 1

    for i in range(0, classes):
        result[i, :] /= sum(result[i, :])

    return result


def calculate_accuracy(gt_labels, pred_labels):
    return (gt_labels == pred_labels).sum() / len(gt_labels)


names = ['s-length', 's-width', 'p-length', 'p-width', 'class']
# data = pd.read_csv(path, names=names)
names = ["open", "close", "candle_size", "volume"]
candles = pd.read_csv("2h_BTC_candle_shape.csv", names=names)
names2 = ["open", "high", "low", "close", "volume"]
ticks = pd.read_csv("2h_ohlcv_BTCUSDT.csv", names=names2)

m = 4 # candles
open = ticks['open']
close = ticks['close']
N = close.shape[0]
y = []

for i in range(N-5):
    # y
    diff = close[i+5]-open[i+4]
    if diff > 0:
        y.append(1)
    else:
        y.append(0)
# le = preprocessing.LabelEncoder()
# y = ysa.apply(le.fit_transform)


# x - make each sample a time window of n_candles_per_sample
x = np.ones((N-5,m*n_candles_per_sample))
for i in range(N-5):
    for j in range(n_candles_per_sample):
        for k in range(m):
            x[i, m*j+k] = candles.iloc[i+j, k]


# Feature scaling
scaler = preprocessing.StandardScaler()
scaler.fit(x)
x = scaler.transform(x)

print(np.unique(y, return_counts=True))

train_x, test_x, train_y, test_y = model_selection.train_test_split(x, y, test_size=0.20)

for i in range(1,11):

    h_layers = (8*i,5*i)
    nn = neural_network.MLPClassifier(hidden_layer_sizes=h_layers, max_iter=10000000)
    nn.fit(train_x, train_y)
    print("NN generated - {}").format(h_layers)

    # Predict test data
    pred = nn.predict(test_x)

    # plot_matrix(calculate_confusion_matrix(test_y, pred))
    # plt.show()
    print("#{}  -  {}".format(h_layers, calculate_accuracy(test_y, pred)))
# print(metrics.classification_report(test_y, pred))









