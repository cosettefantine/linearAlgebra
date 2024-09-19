def kronPrdct(mtrx1, mtrx2):
    kronProduct = []  # create an empty array(list)
    # # it was not converted to a Numpy array to be able to use the append() method later

    for itr in range(len(mtrx1) * len(mtrx2)):  # convert the array created above into an array consisting of 0's of the same size as the array that will be created as a result of multiplication
        kronProduct.append([0] * (len(mtrx1[0]) * len(mtrx2[0])))

    for i in range(0, len(kronProduct), len(mtrx2)):  # an intermittent 'for loop' so we can do slicing
        for j in range(0, len(kronProduct[0]), len(mtrx2[0])):
            mtrx1_row = i // len(mtrx2)  # corresponding mtrx1 indices
            mtrx1_col = j // len(mtrx2[0])

            for k in range(len(mtrx2)):  # 'for loop' that must continuously loop mtrx2 from start to finish
                for l in range(len(mtrx2[0])):
                    kronProduct[i + k][j + l] = mtrx1[mtrx1_row][mtrx1_col] * mtrx2[k][l]  # multiply the mtrx2 elements by the corresponding mtrx1 element and add them to the relevant kronProduct index

    return kronProduct


mt1 = [[1], [2], [3]]
mt2 = [[1, 2, 3]]
result = kronPrdct(kronPrdct(mt1, mt2), mt2)
print(result)
