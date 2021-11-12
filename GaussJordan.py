import numpy as np


def gauss_jordan(x, y):
    m, n = x.shape
    augmented_mat = np.zeros(shape=(m, n+1))
    augmented_mat[:m, :n] = x
    augmented_mat[:, m] = y
    np.set_printoptions(precision=2, suppress=True)
    print('# Original augmented matrix')
    print(augmented_mat)
    for i in range(0, m-1):
        for j in range(i+1, m):
            k = (-1) * augmented_mat[j, i] / augmented_mat[i, i]
            temp_row = augmented_mat[i, :]*k
            print('# Use line %2i for line %2i' % (i+1, j+1))
            print('k=%.2f' % k, '*', augmented_mat[i, :], '=', temp_row)
            augmented_mat[j, :] = augmented_mat[j, :] + temp_row
            print(augmented_mat)
    for i in range(m-1, 0, -1):
        for j in range(i-1, -1, -1):
            k = (-1) * augmented_mat[j, i] / augmented_mat[i, i]
            temp_row = augmented_mat[i, :] * k
            print('# Use line %2i for line %2i' % (i+1, j+1))
            print('k=%.2f' % k, '*', augmented_mat[i, :], '=', temp_row)
            augmented_mat[j, :] = augmented_mat[j, :] + temp_row
            print(augmented_mat)
    for i in range(0, m):
        augmented_mat[i, :] = augmented_mat[i, :] / augmented_mat[i, i]
    print('# Normalize the rows')
    print(augmented_mat)
    return augmented_mat[:, n]


if __name__ == "__main__":
    coefficients = np.array([[5, 15, 25],
                             [15, 25, 55],
                             [25, 55, 225]])
    right_hand_side = np.array([15, 25, 225])
    b = gauss_jordan(coefficients, right_hand_side)
    print(b)
