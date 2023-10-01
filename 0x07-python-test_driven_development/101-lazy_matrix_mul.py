import numpy as np

def lazy_matrix_mul(m_a, m_b):
    # Convert the input lists to NumPy arrays
    a = np.array(m_a)
    b = np.array(m_b)
    
    # Perform matrix multiplication
    result = np.dot(a, b)
    
    return result.tolist()
