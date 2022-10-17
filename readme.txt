Our idea for the project is to simulate a robot that can play a game of checkers against 
itself/human opponent. The basis for the project is pick and place with the robot arm to move the 
pieces, and camera vision to determine the current position of pieces on the checkerboard. The project 
will use OpenCV library along with gazebo to calculate the positions of various pieces on the virtual 
board. This will interface with an open-source Python checkers library that will be used to determine 
what moves the computer should make on the gameboard. These moves will be translated into a series 
of movements the robot must make to get the pieces to the correct spots. 
The robot arm will base its movement off a home position determined by one of the corner 
squares. The robot can figure out the position of all the other squares by referencing the home square 
and board dimensions without manually programming them all in. The robot will try to place pieces in 
the center of the squares but can pick up pieces that aren’t exactly centered in the squares. Since the 
checker pieces will be modeled as pucks, the sucker will be used to move pieces around the board. 
We will use image processing techniques to detect the checker pieces center/positions using 
Hough Circle Transformation and we will detect the colors using RGB pixel thresholding. The playing grid 
can be pixel-wise defined in software to an expected position and the virtual camera/board can be 
moved so it aligns with the expected board distance/position relative to the camera. 
For the basic project, the checkerboard must remain at the same coordinates and orientation in 
the configuration space every time. If there is extra time, the robot will also feature a mode where it can 
setup the game pieces in any arbitrary positions so that user can practice playing out of certain 
positions