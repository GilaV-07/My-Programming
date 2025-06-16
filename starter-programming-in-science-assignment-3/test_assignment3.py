import unittest
import os
import numpy as np
import matplotlib.pyplot as plt
from Assignment3 import *

# Test case for write_and_read_txt() function
def test_write_and_read_txt():
    filename = "test_numbers.txt"
    numbers = [1, 2, 3, 4, 5]
    result = write_and_read_txt(filename, numbers)
    assert result == numbers
    os.remove(filename)

# Test case for write_and_read_csv() function
def test_write_and_read_csv():
    filename = "test_data.csv"
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = write_and_read_csv(filename, data)
    assert result == data
    os.remove(filename)

# Test case for read_array_from_file() function
def test_read_array_from_file():
    filename = "test_array.txt"
    with open(filename, 'w') as file:
        file.write("1.5 2.5 3.5 4.5 5.5")
    
    expected_array = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
    result = read_array_from_file(filename)
    np.testing.assert_array_equal(result, expected_array)
    os.remove(filename)

# Test case for plot_data() function
def test_plot_data():
    numbers = [1, 2, 3, 4, 5]
    plt.figure()
    plot_data(numbers)  # This function only displays the plot, no assertion needed.

# Test case for density_plot() function
def test_density_plot():
    data = np.random.normal(0, 1, 1000)
    plt.figure()
    density_plot(data)  # This function only displays the plot, no assertion needed.

if __name__ == '__main__':
    unittest.main()
