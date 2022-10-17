import cv2
import numpy as np
start_point = (0, 0)
end_point = (220, 220)
color = (255, 0, 0)
thickness = 2


def circleFind():
    global frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                            minRadius=1, maxRadius=30)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center check the colors of the circle
            cv2.circle(frame, center, 1, (0, 0, 255), 3)
            # circle outline
            radius = i[2]
            cv2.circle(frame, center, radius, (0, 0, 255), 3)  
            
            #figure out which player the piece belongs to by color of middle pixel, hijack i3 radius to do this cause lazy for now
            if(gray[i[1]][i[0]] > 160):
                i[2] = 1
                cv2.circle(frame, center, radius, (0, 255, 0), 3)  
            else:
                i[2] = 2
                cv2.circle(frame, center, radius, (0, 0, 255), 3)  
        #print(circles)
    
  
    
def createGrid(corner, width, height):
    global frame
    homecorner_x =  corner[0]
    homecorner_y =  corner[1]
    #generate grid from corners
    stepx = width/8 #length of each box
    stepy = height/8
    for i in range(8):
        for j in range(8):
          #calc top left corner
            topleft_x = int(stepx * i + homecorner_x)
            topleft_y = int(stepy * j + homecorner_y)
          #calc bottom right corner
            bottomright_x = int(stepx * (i+1) + homecorner_x)
            bottomright_y = int(stepy * (j+1) + homecorner_y)
            start_point = (topleft_x,topleft_y)
            end_point = (bottomright_x, bottomright_y)
            cv2.rectangle(frame, start_point, end_point, color, thickness)   
            
            
            
#TODO Finds out which players pieces occupy what squares
rows, cols = (8, 8)
boardpos = [[0]*cols]*rows
def getCurPositions(corner,width,height, circles):
    global boardpos
    global frame
    print(circles)
    homecorner_x =  corner[0]
    homecorner_y =  corner[1]
    #generate grid from corners
    stepx = width/8 #length of each box
    stepy = height/8
    for i in range(8):
        for j in range(8):
          #calc top left corner
            topleft_x = int(stepx * i + homecorner_x)
            topleft_y = int(stepy * j + homecorner_y)
          #calc bottom right corner
            bottomright_x = int(stepx * (i+1) + homecorner_x)
            bottomright_y = int(stepy * (j+1) + homecorner_y)
            start_point = (topleft_x,topleft_y)
            end_point = (bottomright_x, bottomright_y)
            if circles is not None:
                print("blah")
                for circle in circles:
                    circle_x = circle[0][0]
                    circle_y = circle[0][1]
                    circle_player = circle[0][2]
                    if(circle_x > topleft_x  and circle_x < bottomright_x and circle_y > topleft_y and circle_y < bottomright_y):
                        boardpos[i][j] = circle_player
                        if(circle_player == 1):
                            cv2.rectangle(frame, start_point, end_point, (120,120,0), 2) 
                        else:
                            cv2.rectangle(frame, start_point, end_point, (0,120,120), 2) 
 







def checkMove():
    #calculate user move based on prev positions and current positions send to checkers api
    #make sure a valid move occured, need to run this at each jump for multi-jumps
    return 0





            
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    else:
        circles = circleFind()
        createGrid((40,40), 420, 420)
        #getCurPositions((40,40), 420, 420, circles)
        
vc.release()
cv2.destroyWindow("preview")  

