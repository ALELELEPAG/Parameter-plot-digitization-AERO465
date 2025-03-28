import numpy as np 
from scipy.interpolate import interp1d 
 
# Define equations for each constant value curve 

coefficients = { 
0: [-2.24e-06, 0.000262, -0.01594, 1.325348], 
10: [-3.85e-06, 0.00050763, -0.02748, 1.467223], 
20: [-4.06e-06, 0.00051671, -0.025974, 1.36122], 
30: [-5.38e-06, 0.00071815, -0.035623, 1.467063], 
40: [-3.93e-06, 0.0004637, -0.020132, 1.103268], 
50: [-7.18e-06, 0.00104492, -0.05510034, 1.779647], 
60: [-3.26e-05, 0.00597975, -0.3728655, 8.5531459] 
} 

# calculating with the coefficients

def calculate_y(x, coeffs): 
     
    return coeffs[0]*(x**3) + coeffs[1]*(x**2) + (coeffs[2]*x) + coeffs[3] 
 
# Function to interpolate between curves 
 
def interpolate_curves(x, input_value): 
     
    keys = sorted(coefficients.keys()) 
    closest_key = min(keys, key=lambda k: abs(k - input_value)) 
 
    if closest_key == input_value: 
        return calculate_y(x, coefficients[closest_key]) 
    else: 
        lower_key = max(k for k in keys if k < input_value) 
        upper_key = min(k for k in keys if k > input_value) 
         
        y_lower = calculate_y(x, coefficients[lower_key]) 
        y_upper = calculate_y(x, coefficients[upper_key]) 

        f = interp1d([lower_key, upper_key], [y_lower, y_upper], axis=0) 
 
    return f(input_value)

x=60
a2=40

result = interpolate_curves(x, a2)
print(f"The result of interpolate_curves is: {result}")

