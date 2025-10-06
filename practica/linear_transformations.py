import numpy as np
import matplotlib.pyplot as plt

# Define transformation matrix
A = np.array([[0.000, -1.000],
              [1.000, 0.000]])

# Define input vector
v = np.array([1, 1])

# Apply transformation
transformed_v = A @ v

print(f"Original vector: {v}")
print(f"Transformation matrix:\n{A}")

print(f"Transformed vector: {transformed_v}")

# Visualize
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Original vector
ax1.arrow(0, 0, v[0], v[1], head_width=0.1, head_length=0.1, fc='blue', ec='blue')
ax1.set_xlim(-3, 3)
ax1.set_ylim(-3, 3)
ax1.grid(True)
ax1.set_title('Original Vector')
ax1.set_aspect('equal')

# Transformed vector
ax2.arrow(0, 0, transformed_v[0], transformed_v[1], head_width=0.1, head_length=0.1, fc='red', ec='red')
ax2.set_xlim(-5, 5)
ax2.set_ylim(-5, 5)
ax2.grid(True)
ax2.set_title('Transformed Vector')
ax2.set_aspect('equal')

plt.show()