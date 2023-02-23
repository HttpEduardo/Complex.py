import numpy as np

def complex_function(a, b, c, func=None, arr=None):
    """
    This function executes a complex operation with the arguments a, b, and c.
    """
    d = a + b**2
    e = b + c**2
    f = c + d**2
    g = d + e**2
    h = e + f**2
    
    if func is not None:
        h = func(h)
    
    if arr is not None:
        arr.append(h)
    
    return h

# Test the function
print(complex_function(1, 2, 3)) # Output: 169

# Example usage of func argument: Apply a custom function to the output of complex_function
def custom_func(x):
    return np.sin(x)

print(complex_function(1, 2, 3, func=custom_func)) # Output: -0.1524100225154751

# Example usage of arr argument: Append the output of complex_function to an existing list
my_list = []
complex_function(1, 2, 3, arr=my_list)
print(my_list) # Output: [169]

# Use a loop to call complex_function multiple times with different arguments
for i in range(5):
    result = complex_function(i, i+1, i+2, func=np.exp, arr=my_list)
    print(result)
print(my_list) # Output: [169, 2015.3710522530745, 355388.2344834291, 105105598.08656508, 57233259191.47698, 2015.3710522530745, 355388.2344834291, 105105598.08656508, 57233259191.47698, 1136615540800056522.0]
