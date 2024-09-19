import numpy as np


def kronPrdct(mtrx1, mtrx2):
    mtrx1 = np.array(mtrx1)  # convert the lists taken as arguments to the function into a Numpy array
    mtrx2 = np.array(mtrx2)

    kronProduct = []  # create an empty array(list)
    # # it was not converted to a Numpy array to be able to use the append() method later

    for itr in range(mtrx1.shape[0] * mtrx2.shape[0]):  # convert the array created above into an array consisting of 0's of the same size as the array that will be created as a result of multiplication
        kronProduct.append([0] * mtrx1.shape[1] * mtrx2.shape[1])

    for i in range(0, np.array(kronProduct).shape[0], mtrx2.shape[0]):  # an intermittent 'for loop' so we can do slicing
        for j in range(0, np.array(kronProduct).shape[1], mtrx2.shape[1]):
            mtrx1_row = i // mtrx2.shape[0]  # corresponding mtrx1 indices
            mtrx1_col = j // mtrx2.shape[1]

            for k in range(mtrx2.shape[0]):  # 'for loop' that must continuously loop mtrx2 from start to finish
                for l in range(mtrx2.shape[1]):
                    kronProduct[i + k][j + l] = mtrx1[mtrx1_row][mtrx1_col] * mtrx2[k][l]  # multiply the mtrx2 elements by the corresponding mtrx1 element and add them to the relevant kronProduct index

    return np.array(kronProduct)


mt1 = [[1], [2], [3]]
mt2 = [[1, 2, 3]]
result = kronPrdct(kronPrdct(mt1, mt2), mt2)
# comparing the accuracy of the results (the function above and the function 'kron' from Numpy library)
np_result = np.kron(np.kron(mt1, mt2), mt2)
print(result)
print()
print(np_result)
print()
print(np.array_equal(result, np_result))
# if the arrays consist of float values, you can run the code below to compare the accuracy of the results
# print(np.allclose(result, np_result))
