import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon 

SHOW_TRANFORM_MATRIX = False
points = np.array([(0.5,-0.5), (0.5, 0.5), (-0.5, 0.5), (-0.5, -0.5)])

def translate(matrix, x=0, y=0):	
	tm = np.array([[1, 0, x], [0, 1, y], [0, 0, 1]])
	if SHOW_TRANFORM_MATRIX:
		print("\nTranslation Matrix")
		print(tm)
	return np.dot(tm, matrix)

def create_homogenous(matrix):
	matrix = matrix.transpose()
	return	np.concatenate([matrix, np.ones((1,matrix.shape[1]))])

def scale(matrix, x=1, y=1):
	sm = np.array([[x, 0, 0], [0, y, 0], [0, 0, 1]])
	if SHOW_TRANFORM_MATRIX:
		print("\nScaling Matrix")
		print(sm)
	return np.dot(sm, matrix)

def rotate(matrix, theta=0):
	ang = math.radians(theta)
	c = math.cos(ang)
	s = math.sin(ang)
	rm = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
	if SHOW_TRANFORM_MATRIX:
		print("\nRotation Matrix")
		print(rm)
	return np.dot(rm, matrix)

def revert(matrix):
	return matrix[:-1].transpose()

def plot(ax, points):
	ax.clear()
	ax.add_patch(Polygon(points))
	ax.scatter(*list(zip(*points)))
	ax.set_xticks(np.arange(-5, 5+1, 1))
	ax.set_yticks(np.arange(-5, 5+1, 1))
	ax.set_aspect('equal')
#	ax.grid(True, which='both')
	return ax



