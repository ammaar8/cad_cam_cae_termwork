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
	return cad.scale(matrix, sx=sx, sy=sy)

def reflect_x(matrix):
	print("Mirror/Reflect about X-axis")
	return cad.reflect_x(matrix)

def reflect_y(matrix):
	print("Mirror/Reflect about Y-axis")
	return cad.reflect_y(matrix)

def shear(matrix):
	print("Shearing")
	sx = float(input("sx = "))
	sy = float(input("sy = "))
	return cad.shear(matrix, sx=sx, sy=sy)

def do_nothing(matrix):
	return matrix


commands = {1: translate, 2: rotate, 3: scale, 4: reflect_x, 5: reflect_y, 6: shear}

def print_menu():
	for key, val in commands.items():
		print(str(key) + ". " + val.__name__)
	print('\n')


points = np.array([(0.5,-0.5), (0.5, 0.5), (-0.5, 0.5), (-0.5, -0.5)])

def set_points(arr):
	global points
	points = np.array(arr)

def main():
	global points
	fig, ax = plt.subplots(figsize=(5,5))
	cad.plot(ax, points)
	plt.show(block=False)
	while True:
		fig, ax = plt.subplots(figsize=(5,5))
		print_menu()
		option = int(input("Operation no. : "))
		if option == 0:
			plt.close()
			print("\n\nThank you for trying the script out!\Consider starring the repo on GitHub :D\n\n")
			break
		points = cad.create_homogenous(points)
		points = commands.get(option, do_nothing)(points)
		points = cad.revert(points)
		print("\nNew Points")
		print(points)
		cad.plot(ax, points)
		plt.show(block=False)

if __name__=="__main__":
	main()

	
