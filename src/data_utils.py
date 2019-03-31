import numpy as np


def get_train_batches(data_dir='/home/yunhan/batchified'):
    """
        return a list or generator of (large) ndarrays,
        in order to efficiently utilize GPU
    """
    # todo: read in data that is preoprocessed
    # Use batch 1 - 52 as train (60%), 53 - 71 as validation (20%), 72 - 89 as test (20%)
    n = 53
    idx = np.random.permutation(n)
    idx = idx + 1
    for i in range(n):
        X = np.load("%s/X%d.npy" % (data_dir, idx[i]))
        Y = np.load("%s/y%d.npy" % (data_dir, idx[i]))
        yield X, Y


def get_evaluate_batches(data_dir='/home/yunhan/batchified'):
    """
        return a list or generator of (large) ndarrays,
        in order to efficiently utilize GPU
    """
    # train 3 valid 1
    # Use batch 1 - 53 as train (60%), 54 - 71 as validation (20%), 72 - 89 as test (20%)
    n = 18
    idx = np.random.permutation(n)
    idx = idx + 54
    for i in range(n):
        X = np.load("%s/X%d.npy" % (data_dir, idx[i]))
        Y = np.load("%s/y%d.npy" % (data_dir, idx[i]))
        yield X, Y


def get_test_batches(data_dir='/home/yunhan/batchified'):
    """
        return a list or generator of (large) ndarrays,
        in order to efficiently utilize GPU
    """
    # train 3 valid 1
    # Use batch 1 - 53 as train (60%), 54 - 71 as validation (20%), 72 - 89 as test (20%)
    n = 18
    idx = np.random.permutation(n)
    idx = idx + 72
    for i in range(n):
        X = np.load("%s/X%d.npy" % (data_dir, idx[i]))
        Y = np.load("%s/y%d.npy" % (data_dir, idx[i]))
        yield X, Y


def get_batches_mono(data_dir):
    """
        return a list or generator of (large) ndarrays,
        in order to efficiently utilize GPU
    """
    X = np.load('/home/yunhan/data_dir/train_x_224.npy')
    # X = np.load('train_x_sample.npy')
    X = X / 255
    # X = np.load('/home/yunhan/data_dir/train_x_224.npy')
    Y = np.load('/home/yunhan/data_dir/train_y_224.npy')
    # Y = np.load('train_y_sample.npy')
    return [(X, Y, 32, 0.2), ]


def get_test_data(data_dir='/home/yunhan/KaggleDiatetic/src/X_3000.npy'):
    X = np.load(data_dir)
    return X
