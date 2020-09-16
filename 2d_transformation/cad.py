import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.lines import Line2D
from matplotlib.ticker import LinearLocator
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

def scale(matrix, sx=1, sy=1):
	sm = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
	if SHOW_TRANFORM_MATRIX:
		print("\nScaling Matrix")
		print(sm)
	return np.dot(sm, matrix)

def reflect_x(matrix):
	rm = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
	return np.dot(rm, matrix)

def reflect_y(matrix):
	rm = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
	return np.dot(rm, matrix)

def rotate(matrix, theta=0):
	ang = math.radians(theta)
	c = math.cos(ang)
	s = math.sin(ang)
	rm = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
	if SHOW_TRANFORM_MATRIX:
		print("\nRotation Matrix")
		print(rm)
	return np.dot(rm, matrix)

def shear(matrix, sx, sy):
	sm = np.array([[1, sx, 0], [sy, 0, 1], [0, 0, 1]])	
	return np.dot(sm, matrix)

def revert(matrix):
	return matrix[:-1].transpose()



def plot(ax, points):
	ax.clear()
	ax.add_patch(Polygon(points))
	xs, ys = list(zip(*points))
	ax.scatter(xs, ys)
	
	ax.add_line(Line2D([min(xs)-5, max(xs)+5], [0,0], color='r'))
	ax.add_line(Line2D([0,0], [min(ys)-5, max(ys)+4], color='r'))
	ax.set_xticks(np.arange(min(xs)-5, max(xs)+6, 1))
	ax.set_yticks(np.arange(min(ys)-5, max(ys)+6, 1))

	ax.set_aspect('equal')
	return ax



