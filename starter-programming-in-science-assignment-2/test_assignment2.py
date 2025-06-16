import unittest
from Assignment2 import *

# Test case for max_two_in_list() function
def test_max_two_in_list():
    assert max_two_in_list([1, 3, 2, 5, 4]) == (5, 4)
    assert max_two_in_list([10, 10, 9, 8, 7]) == (10, 9)
    assert max_two_in_list([5]) == (5, None)

# Test case for remove_duplicates_and_sort() function
def test_remove_duplicates_and_sort():
    assert remove_duplicates_and_sort([3, 1, 2, 3, 1]) == [1, 2, 3]
    assert remove_duplicates_and_sort([10, 5, 5, 10, 2]) == [2, 5, 10]

# Test case for cumulative_sum() function
def test_cumulative_sum():
    assert cumulative_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert cumulative_sum([5, 10, 15]) == [5, 15, 30]

# Test case for transpose_matrix() function
def test_transpose_matrix():
    assert transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transpose_matrix([[7, 8], [9, 10], [11, 12]]) == [[7, 9, 11], [8, 10, 12]]

# Test case for slice_every_nth() function
def test_slice_every_nth():
    assert slice_every_nth([1, 2, 3, 4, 5, 6], 2) == [1, 3, 5]
    assert slice_every_nth([10, 20, 30, 40, 50], 3) == [10, 40]

# Test case for dot_product() function
def test_dot_product():
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32
    assert dot_product([2, 3, 4], [5, 6, 7]) == 56

# Test case for matrix_multiplication() function
def test_matrix_multiplication():
    assert matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]]
    assert matrix_multiplication([[2, 4], [6, 8]], [[1, 3], [5, 7]]) == [[22, 34], [46, 74]]  

if __name__ == '__main__':
    unittest.main()
