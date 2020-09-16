# CAD/CAM/CAE Termwork
Termwork and Assignments for CAD/CAM/CAE subject

### 2D Transformations
Try online at - [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ammaar8/cad_cam_cae_termwork/master?filepath=2d_transformation%2F2D%20transformations%20Notebook.ipynb).

Uses numpy for calculations and matplotlib for visualization.

##### Transformations available
* Translation
* Rotation
* Scaling
* Reflecting about X and Y axes
* Shearing


##### Changing the initial polygon
1. Select `0. Quit` before changing the points.
2. Set points in `cad_cli.set_points([(1,1), (3,1), (3,3), (1,3)])` and run.

  Example 1 - `cad_cli.set_points([(1,1)])` for a single point `(x,y)`.\
  Example 2 - `cad_cli.set_points([(1,1), (2, 1)])` for a line.\
  Example 3 - `cad_cli.set_points([(1,1), (3,1), (3,3)])` for a triangle.
