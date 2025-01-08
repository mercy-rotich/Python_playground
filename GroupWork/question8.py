import random
import numpy as np

def generate_random_data(size, lower_bound, upper_bound):
    """Generate a list of random integers."""
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def calculate_covariance(data1, data2):
    """Calculate covariance between two datasets."""
    if len(data1) != len(data2):
        raise ValueError("Datasets must have the same length.")

    # Using numpy to calculate covariance
    covariance_matrix = np.cov(data1, data2)
    covariance = covariance_matrix[0][1]  # Covariance value from the matrix
    return covariance

# Main program
def main():
    # Generate two random datasets
    size = 10  # Number of data points
    lower_bound = 1
    upper_bound = 100

    dataset1 = generate_random_data(size, lower_bound, upper_bound)
    dataset2 = generate_random_data(size, lower_bound, upper_bound)

    print("Dataset 1:", dataset1)
    print("Dataset 2:", dataset2)

    # Calculate and display the covariance
    covariance = calculate_covariance(dataset1, dataset2)
    print("\nCovariance between Dataset 1 and Dataset 2:", covariance)

if __name__ == "__main__":
    main()
