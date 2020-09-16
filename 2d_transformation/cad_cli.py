import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import cad

def translate(matrix):
	print("Translating")
	tx = float(input("X: "))
	ty = float(input("Y: "))
	return cad.translate(matrix, x=tx, y=ty)

def rotate(matrix):
	print("Rotating")
	angle = float(input("Angle (deg): "))
	return cad.rotate(matrix, theta=angle)

def scale(matrix):
	print("Scaling")
	sx = float(input("sx = "))
	sy = float(input("sy = "))
	return cad.scale(matrix, x=sx, y=sy)

def do_nothing():
	print("Not an option")

commands = {1: translate, 2: rotate, 3: scale}


def print_menu():
	for key, val in commands.items():
		print(str(key) + ". " + val.__name__)


points = np.array([(0.5,-0.5), (0.5, 0.5), (-0.5, 0.5), (-0.5, -0.5)])

def set_points(arr):
	global points
	points = np.array(arr)

def main():
	global points
	fig, ax = plt.subplots(1)
	cad.plot(ax, points)
	plt.show(block=False)
	while True:
		fig, ax = plt.subplots(1)
		points = cad.create_homogenous(points)
		print_menu()
		option = int(input("Operation no. : "))
		points = commands[option](points)
		points = cad.revert(points)
		print("\nNew Points")
		print(points)
		cad.plot(ax, points)
		plt.show(block=False)

if __name__=="__main__":
	main()

	
