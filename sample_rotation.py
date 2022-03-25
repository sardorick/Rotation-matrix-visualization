


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt




y, x = np.indices((5, 4))
y = y.flatten()
x = x.flatten()
xy = np.row_stack((x, y))

def rot_mat(deg):
    theta = deg/180*np.pi
    c = np.cos(theta)
    s = np.sin(theta)
    return np.array([[c, -s], [s, c]])

r = rot_mat(30)
rxy = r@xy

plt.figure(figsize=(10, 8))
plt.scatter(xy[0], xy[1], label = "Original Vector")
plt.scatter(rxy[0], rxy[1], label = "Transformed Vector")
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Rotation Matrix')
plt.legend(loc ='upper left')
plt.grid(True, linewidth = 1)
plt.show()