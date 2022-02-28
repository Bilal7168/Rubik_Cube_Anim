
from Rubik_Cube import Rubik_Cube

import sys

import copy

from PyQt5 import QtWidgets as qtWid
from PyQt5 import QtCore as qtCore
from PyQt5 import QtGui
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSlot

import queue


#the functions that start the array

#the main Solver Function

def check_duplicate(Check_Cube, Cube_Queue):
    for i in range(Cube_Queue.qsize()):
        if(Check_Cube == Cube_Queue.queue[i]):
            return True
    return False

def RCS_Stack_Filler_Utility(Curr_Cube, Cube_Queue):
    for i in range(12):
                if(i == 0):
                    Temp_Cube = Rubik_Cube();
                    Temp_Cube._overloader_self_(Curr_Cube)
                    Temp_Cube.clockwise_rotate_back();
                    Temp_Cube.set_prev_rot("Clockwise Rotate Back");
                    Temp_Cube.set_prev_cube(Curr_Cube);
                    print(Temp_Cube.Get_Cube_Combinations())
                    if(check_duplicate(Temp_Cube, Cube_Queue) is False):
                        Cube_Queue.put(Temp_Cube);
                    if(Temp_Cube.allFacesEqual()):
                        return True
                if(i == 1):
                    Temp_Cube = Rubik_Cube();
                    Temp_Cube._overloader_self_(Curr_Cube)
                    Temp_Cube.anti_clockwise_rotate_back();
                    Temp_Cube.set_prev_rot("Anti Clockwise Rotate Back");
                    Temp_Cube.set_prev_cube(Curr_Cube);
                    print(Temp_Cube.Get_Cube_Combinations())
                    if(check_duplicate(Temp_Cube, Cube_Queue) is False):
                        Cube_Queue.put(Temp_Cube);
                    if(Temp_Cube.allFacesEqual()):
                        return True
                if(i == 2):
                    Temp_Cube = Rubik_Cube();
                    Temp_Cube._overloader_self_(Curr_Cube)
                    Temp_Cube.clockwise_rotate_down();
                    Temp_Cube.set_prev_rot("Clockwise Rotate Down");
                    Temp_Cube.set_prev_cube(Curr_Cube);
                    if(check_duplicate(Temp_Cube, Cube_Queue) is False):
                        Cube_Queue.put(Temp_Cube);
                    if(Temp_Cube.allFacesEqual()):
                        return True
                if(i == 3):
                    Temp_Cube = Rubik_Cube();
                    Temp_Cube._overloader_self_(Curr_Cube)
                    Temp_Cube.anti_clockwise_rotate_down();
                    Temp_Cube.set_prev_rot("Anti Clockwise Rotate Down");
                    Temp_Cube.set_prev_cube(Curr_Cube);
                    print(Temp_Cube.Get_Cube_Combinations())
                    if(check_duplicate(Temp_Cube, Cube_Queue) is False):
                        Cube_Queue.put(Temp_Cube);
                    if(Temp_Cube.allFacesEqual()):
                        return True
                if(i == 4):
                    Temp_Cube = Rubik_Cube();
                    Temp_Cube._overloader_self_(Curr_Cube)
                    Temp_Cube.clockwise_rotate_front();
                    Temp_Cube.set_prev_rot("Clockwise Rotate Front");
                    Temp_Cube.set_prev_cube(Curr_Cube);
                    print(Temp_Cube.Get_Cube_Combinations())
                    if(check_duplicate(Temp_Cube, Cube_Queue) is False):
                        Cube_Queue.put(Temp_Cube);
                    if(Temp_Cube.allFacesEqual()):
                        return True
                if(i == 5):
                    Temp_Cube = Rubik_Cube();
                    Temp_Cube._overloader_self_(Curr_Cube)
                    Temp_Cube.anti_clockwise_rotate_front();
                    Temp_Cube.set_prev_rot("Anti Clockwise Rotate Front");
                    Temp_Cube.set_prev_cube(Curr_Cube);
                    print(Temp_Cube.Get_Cube_Combinations())
                    if(check_duplicate(Temp_Cube, Cube_Queue) is False):
                        Cube_Queue.put(Temp_Cube);
                    if(Temp_Cube.allFacesEqual()):
                        return True
                if(i == 6):
                    Temp_Cube = Rubik_Cube();
                    Temp_Cube._overloader_self_(Curr_Cube)
                    Temp_Cube.clockwise_rotate_left()
                    Temp_Cube.set_prev_rot("Clockwise Rotate Left");
                    Temp_Cube.set_prev_cube(Curr_Cube);
                    print(Temp_Cube.Get_Cube_Combinations())
                    if(check_duplicate(Temp_Cube, Cube_Queue) is False):
                        Cube_Queue.put(Temp_Cube);
                    if(Temp_Cube.allFacesEqual()):
                        return True
                if(i == 7):
                    Temp_Cube = Rubik_Cube();
                    Temp_Cube._overloader_self_(Curr_Cube)
                    Temp_Cube.anti_clockwise_rotate_left()
                    Temp_Cube.set_prev_rot("Anti Clockwise Rotate Left");
                    Temp_Cube.set_prev_cube(Curr_Cube);
                    print(Temp_Cube.Get_Cube_Combinations())
                    if(check_duplicate(Temp_Cube, Cube_Queue) is False):
                        Cube_Queue.put(Temp_Cube);
                    if(Temp_Cube.allFacesEqual()):
                        return True
                if(i == 8):
                    Temp_Cube = Rubik_Cube();
                    Temp_Cube._overloader_self_(Curr_Cube)
                    Temp_Cube.clockwise_rotate_right()
                    Temp_Cube.set_prev_rot("Clockwise Rotate Right");
                    Temp_Cube.set_prev_cube(Curr_Cube);
                    print(Temp_Cube.Get_Cube_Combinations())
                    if(check_duplicate(Temp_Cube, Cube_Queue) is False):
                        Cube_Queue.put(Temp_Cube);
                    if(Temp_Cube.allFacesEqual()):
                        return True
                if(i == 9):
                    Temp_Cube = Rubik_Cube();
                    Temp_Cube._overloader_self_(Curr_Cube)
                    Temp_Cube.anti_clockwise_rotate_right()
                    Temp_Cube.set_prev_rot("Anti Clockwise Rotate Right");
                    Temp_Cube.set_prev_cube(Curr_Cube);
                    print(Temp_Cube.Get_Cube_Combinations())
                    if(check_duplicate(Temp_Cube, Cube_Queue) is False):
                        Cube_Queue.put(Temp_Cube);
                    if(Temp_Cube.allFacesEqual()):
                        return True
                if(i == 10):
                    Temp_Cube = Rubik_Cube();
                    Temp_Cube._overloader_self_(Curr_Cube)
                    Temp_Cube.clockwise_rotate_up();
                    Temp_Cube.set_prev_rot("Clockwise Rotate Up");
                    Temp_Cube.set_prev_cube(Curr_Cube);
                    print(Temp_Cube.Get_Cube_Combinations())
                    if(check_duplicate(Temp_Cube, Cube_Queue) is False):
                        Cube_Queue.put(Temp_Cube);
                    if(Temp_Cube.allFacesEqual()):
                        return True
                if(i == 11):
                    Temp_Cube = Rubik_Cube();
                    Temp_Cube._overloader_self_(Curr_Cube)
                    Temp_Cube.anti_clockwise_rotate_up();
                    Temp_Cube.set_prev_rot("Anti Clockwise Rotate Up");
                    Temp_Cube.set_prev_cube(Curr_Cube);
                    print(Temp_Cube.Get_Cube_Combinations())
                    if(check_duplicate(Temp_Cube, Cube_Queue) is False):
                        Cube_Queue.put(Temp_Cube);
                    if(Temp_Cube.allFacesEqual()):
                        return True
    print(Cube_Queue.qsize())
    return False

def Recursive_Cube_Solver_Utility(Cube_Queue):
    #pop first element from Queue
    Curr_Cube = Cube_Queue.get()

    #Fill Stack with new rotation Cubes
    if(RCS_Stack_Filler_Utility(Curr_Cube, Cube_Queue)):
        return True

    Recursive_Cube_Solver_Utility(Cube_Queue);


def Iterative_Cube_Solver(Cube_Queue): #get the first element from this Cube_Queue
    
    while(Cube_Queue.empty() is False):
        Curr_Cube = Cube_Queue.get(); #get the first element

        if(Curr_Cube.allFacesEqual()):
            Cube_Queue.put(Curr_Cube);
            return True
        else:
            #fill the queue with this cube's all elements
            if(RCS_Stack_Filler_Utility(Curr_Cube, Cube_Queue)):
                return True
            #keep running this iterative loop

Rot_Str = []

def Solve_Rubik_Cube(Curr_Cube): #pass object of Rubik_Cube Class
    correct_rotation = [];
    if(Curr_Cube.allFacesEqual()):
        print("Cube is Solved Already!")
        correct_rotation.append("Cube is Solved Already!")
        return correct_rotation 
    else:
        #make FIFO queue
        Cube_Queue = queue.Queue();

        #add first Cube to the Queue
        Cube_Queue.put(Curr_Cube)

        #start Recursive Traverser

        #Recursive_Cube_Solver_Utility(Cube_Queue)

        #start Iterative Traverser

        Iterative_Cube_Solver(Cube_Queue)

        #last cube in Cube_Queue is solved

        Solved_Cube = 0;
        while(Cube_Queue.empty() is False):
            Solved_Cube = Cube_Queue.get()

        #get rotations from this Solved Cube
        while(Solved_Cube.get_prev_rot() != 0):
            correct_rotation.append(Solved_Cube.get_prev_rot())
            Rot_Str.append(Solved_Cube.get_prev_rot())
            Solved_Cube = Solved_Cube.get_prev_cube();

        return correct_rotation;

def color_adder(box_single, color_letter):
    if(color_letter == 'R'):
        box_single.setStyleSheet("background-color: red")
    if(color_letter == 'W'):
        box_single.setStyleSheet("background-color: white")
    if(color_letter == 'Y'):
        box_single.setStyleSheet("background-color: yellow")
    if(color_letter == 'O'):
        box_single.setStyleSheet("background-color: orange")
    if(color_letter == 'B'):
        box_single.setStyleSheet("background-color: blue")
    if(color_letter == 'G'):
        box_single.setStyleSheet("background-color: green")

def fill_cube_w_colors(boxes, curr_cube_arr):
    j = 0;
    z = 0;
    k = 0;
    for i in range(54):
        if(i % 3 == 0 and i > 0):
            z = z + 1
            j = 0
        if(i % 9 == 0 and i > 0):
            k = k + 1;
            z = 0;
        color_adder(boxes[i], curr_cube_arr[k][z][j])
        j = j + 1

def Rotation_By_Click(R_c, boxes, index, Corr_Rot):
    Str_Check = "";
    if(index == 0):
        R_c.clockwise_rotate_up();
        Str_Check = "Clockwise Rotate Up"
    if(index == 1):
        R_c.anti_clockwise_rotate_up();
        Str_Check = "Anti Clockwise Rotate Up"
    if(index == 2):
        R_c.clockwise_rotate_down();
        Str_Check = "Clockwise Rotate Down"
    if(index == 3):
        R_c.anti_clockwise_rotate_down();
        Str_Check = "Anti Clockwise Rotate Down"
    if(index == 4):
        R_c.clockwise_rotate_left();
        Str_Check = "Clockwise Rotate Left"
    if(index == 5):
        R_c.anti_clockwise_rotate_left();
        Str_Check = "Anti Clockwise Rotate Left"
    if(index == 6):
        R_c.clockwise_rotate_right();
        Str_Check = "Clockwise Rotate Right"
    if(index == 7):
        R_c.anti_clockwise_rotate_right();
        Str_Check = "Anti Clockwise Rotate Right"
    if(index == 8):
        R_c.clockwise_rotate_front();
        Str_Check = "Clockwise Rotate Front"
    if(index == 9):
        R_c.anti_clockwise_rotate_front();
        Str_Check = "Anti Clockwise Rotate Front"
    if(index == 10):
        R_c.clockwise_rotate_back();
        Str_Check = "Clockwise Rotate Back"
    if(index == 11):
        R_c.anti_clockwise_rotate_back();
        Str_Check = "Anti Clockwise Rotate Back"
    
    if(Corr_Rot.count() > 0 and len(Rot_Str) > 0):
        if(Rot_Str[-1] == Str_Check):
            Corr_Rot.takeItem(0);
            Rot_Str.pop(-1)
        elif(Rot_Str[-1] != Str_Check):
            Corr_Rot.clear();
            Rot_Str.clear();
            Corr_Rot.addItem("Incorrect Move Detected! Start Again!")
    fill_cube_w_colors(boxes, R_c.Get_Cube_Combinations())

def Cube_Solver_GUI(Corr_Rot, R_c):
        Corr_Rot.setHidden(False);
        Corr_Rot.clear()
        corr_rot = Solve_Rubik_Cube(R_c)

        Display_String = ""

        while(len(corr_rot) > 0):
            Corr_Rot.addItem(corr_rot.pop())

def Rubik_Cube_Anim(R_c):
    
       app = QApplication(sys.argv)
       win = QMainWindow();

       win.setGeometry(200, 200, 950, 700)
       win.setWindowTitle("Rubik Cube Animator")

       Corr_Rot = qtWid.QListWidget(win)

              #starting boxes initialization
       boxes = [0] * 54;
       for i in range(54):
           boxes[i] = qtWid.QPushButton(win)
           boxes[i].setFixedWidth(30)
           boxes[i].setFixedHeight(30)

       #front 
       boxes[0].move(60, 100); boxes[1].move(90, 100); boxes[2].move(120, 100); boxes[3].move(60, 130); boxes[4].move(90, 130);
       boxes[5].move(120, 130); boxes[6].move(60, 160); boxes[7].move(90, 160); boxes[8].move(120, 160);

       #back
       boxes[9].move(300, 100); boxes[10].move(330, 100); boxes[11].move(360, 100); boxes[12].move(300, 130); boxes[13].move(330, 130);
       boxes[14].move(360, 130); boxes[15].move(300, 160); boxes[16].move(330, 160); boxes[17].move(360, 160);

       #right
       boxes[18].move(530, 100); boxes[19].move(560, 100); boxes[20].move(590, 100); boxes[21].move(530, 130); boxes[22].move(560, 130);
       boxes[23].move(590, 130); boxes[24].move(530, 160); boxes[25].move(560, 160); boxes[26].move(590, 160);

       #left
       boxes[27].move(60, 300); boxes[28].move(90, 300); boxes[29].move(120, 300); boxes[30].move(60, 330); boxes[31].move(90, 330);
       boxes[32].move(120, 330); boxes[33].move(60, 360); boxes[34].move(90, 360); boxes[35].move(120, 360);

       #up
       boxes[36].move(300, 300); boxes[37].move(330, 300); boxes[38].move(360, 300); boxes[39].move(300, 330); boxes[40].move(330, 330);
       boxes[41].move(360, 330); boxes[42].move(300, 360); boxes[43].move(330, 360); boxes[44].move(360, 360);

       #down
       boxes[45].move(530, 300); boxes[46].move(560, 300); boxes[47].move(590, 300); boxes[48].move(530, 330); boxes[49].move(560, 330);
       boxes[50].move(590, 330); boxes[51].move(530, 360); boxes[52].move(560, 360); boxes[53].move(590, 360);

       #call color function
       fill_cube_w_colors(boxes, R_c.Get_Cube_Combinations())

       buttonUp = qtWid.QPushButton(win)
       buttonUp.setText("Clockwise Rotate Up!")
       buttonUp.setFixedWidth(220)
       buttonUp.move(700, 50)

       buttonUp.setFont(QFont('Courier New, monospace', 7, 800, True))

       buttonUp.clicked.connect(lambda: Rotation_By_Click(R_c, boxes, 0, Corr_Rot))

       buttonAntiUp = qtWid.QPushButton(win)
       buttonAntiUp.setText("Anti Clockwise Rotate Up!")
       buttonAntiUp.setFixedWidth(220)
       buttonAntiUp.move(700, 100)

       buttonAntiUp.setFont(QFont('Courier New, monospace', 7, 800, True))

       buttonAntiUp.clicked.connect(lambda: Rotation_By_Click(R_c, boxes, 1, Corr_Rot))

       buttonDown = qtWid.QPushButton(win)
       buttonDown.setText("Clockwise Rotate Down!")
       buttonDown.setFixedWidth(220)
       buttonDown.move(700, 150)

       buttonDown.setFont(QFont('Courier New, monospace', 7, 800, True))


       buttonDown.clicked.connect(lambda: Rotation_By_Click(R_c, boxes, 2, Corr_Rot))

       buttonAntiDown = qtWid.QPushButton(win)
       buttonAntiDown.setText("Anti Clockwise Rotate Down!")
       buttonAntiDown.setFixedWidth(220)
       buttonAntiDown.move(700, 200)

       buttonAntiDown.setFont(QFont('Courier New, monospace', 7, 800, True))

       buttonAntiDown.clicked.connect(lambda: Rotation_By_Click(R_c, boxes, 3, Corr_Rot))

       buttonLeft = qtWid.QPushButton(win)
       buttonLeft.setText("Clockwise Rotate Left!")
       buttonLeft.setFixedWidth(220)
       buttonLeft.move(700, 250)

       buttonLeft.setFont(QFont('Courier New, monospace', 7, 800, True))

       buttonLeft.clicked.connect(lambda: Rotation_By_Click(R_c, boxes, 4, Corr_Rot))

       buttonAntiLeft = qtWid.QPushButton(win)
       buttonAntiLeft.setText("Anti Clockwise Rotate Left!")
       buttonAntiLeft.setFixedWidth(220)
       buttonAntiLeft.move(700, 300)

       buttonAntiLeft.setFont(QFont('Courier New, monospace', 7, 800, True))

       buttonAntiLeft.clicked.connect(lambda: Rotation_By_Click(R_c, boxes, 5, Corr_Rot))

       buttonRight = qtWid.QPushButton(win)
       buttonRight.setText("Clockwise Rotate Right!")
       buttonRight.setFixedWidth(220)
       buttonRight.move(700, 350)

       buttonRight.setFont(QFont('Courier New, monospace', 7, 800, True))

       buttonRight.clicked.connect(lambda: Rotation_By_Click(R_c, boxes, 6, Corr_Rot))

       buttonAntiRight = qtWid.QPushButton(win)
       buttonAntiRight.setText("Anti Clockwise Rotate Right!")
       buttonAntiRight.setFixedWidth(220)
       buttonAntiRight.move(700, 400)

       buttonAntiRight.setFont(QFont('Courier New, monospace', 7, 800, True))

       buttonAntiRight.clicked.connect(lambda: Rotation_By_Click(R_c, boxes, 7, Corr_Rot))

       buttonFront = qtWid.QPushButton(win)
       buttonFront.setText("Clockwise Rotate Front!")
       buttonFront.setFixedWidth(220)
       buttonFront.move(700, 450)

       buttonFront.setFont(QFont('Courier New, monospace', 7, 800, True))

       buttonFront.clicked.connect(lambda: Rotation_By_Click(R_c, boxes, 8, Corr_Rot))

       buttonAntiFront = qtWid.QPushButton(win)
       buttonAntiFront.setText("Anti Clockwise Rotate Front!")
       buttonAntiFront.setFixedWidth(220)
       buttonAntiFront.move(700, 500)

       buttonAntiFront.setFont(QFont('Courier New, monospace', 7, 800, True))

       buttonAntiFront.clicked.connect(lambda: Rotation_By_Click(R_c, boxes, 9, Corr_Rot))

       buttonBack = qtWid.QPushButton(win)
       buttonBack.setText("Clockwise Rotate Back!")
       buttonBack.setFixedWidth(220)
       buttonBack.move(700, 550)

       buttonBack.setFont(QFont('Courier New, monospace', 7, 800, True))

       buttonBack.clicked.connect(lambda: Rotation_By_Click(R_c, boxes, 10, Corr_Rot))

       buttonAntiBack = qtWid.QPushButton(win)
       buttonAntiBack.setText("Anti Clockwise Rotate Back!")
       buttonAntiBack.setFixedWidth(220)
       buttonAntiBack.move(700, 600)

       buttonAntiBack.setFont(QFont('Courier New, monospace', 7, 800, True))

       buttonAntiBack.clicked.connect(lambda: Rotation_By_Click(R_c, boxes, 11, Corr_Rot))

       buttonSolveMe = qtWid.QPushButton(win)
       buttonSolveMe.setText("Solve Me!")
       buttonSolveMe.setFixedWidth(120)
       buttonSolveMe.move(473, 600)

       Corr_Rot.move(423, 470)

       Corr_Rot.setFixedHeight(100)
       Corr_Rot.setFixedWidth(200)

       Corr_Rot.setHidden(True);

       Corr_Rot.setFont(QFont("monospace", 10))

       Corr_Rot.setStyleSheet("background-color:lightblue")

       buttonSolveMe.clicked.connect(lambda: Cube_Solver_GUI(Corr_Rot, R_c))

       buttonSolveMe.setStyleSheet("background-color:lightgreen")
       buttonSolveMe.setFont(QFont('Courier New, monospace', 10, 500, True))

       FlashyTitlePartOne = qtWid.QLabel(win)
       FlashyTitlePartTwo = qtWid.QLabel(win)
       FlashyTitlePartThree = qtWid.QLabel(win)
       FlashyTitlePartFour = qtWid.QLabel(win)
       FlashyTitlePartFive = qtWid.QLabel(win)
       FlashyTitlePartOne.setText("Rubik")
       FlashyTitlePartTwo.setText("Cube")
       FlashyTitlePartThree.setText("Solver")
       FlashyTitlePartFour.setText("v1.0")
       FlashyTitlePartFive.setText("by Bilal Shahid and Musira Khan")

       FlashyTitlePartOne.setFont(QFont('Brush Script MT, Brush Script Std, cursive', 40, 10))
       FlashyTitlePartTwo.setFont(QFont('Brush Script MT, Brush Script Std, cursive', 40, 10))
       FlashyTitlePartThree.setFont(QFont('Brush Script MT, Brush Script Std, cursive', 40, 10))
       FlashyTitlePartFour.setFont(QFont('Brush Script MT, Brush Script Std, cursive', 40))
       FlashyTitlePartFive.setFont(QFont('Brush Script MT, Brush Script Std, cursive', 40))


       FlashyTitlePartOne.setFixedWidth(100)
       FlashyTitlePartTwo.setFixedWidth(100)
       FlashyTitlePartThree.setFixedWidth(200)
       FlashyTitlePartFour.setFixedWidth(100)
       FlashyTitlePartFive.setFixedWidth(200)
       FlashyTitlePartOne.setStyleSheet("color:Indigo; font-size:37px;")
       FlashyTitlePartTwo.setStyleSheet("color:Green; font-size:33px;")
       FlashyTitlePartThree.setStyleSheet("color:Red; font-size:37px;")
       FlashyTitlePartFour.setStyleSheet("color:Black; font-size:33px;")
       FlashyTitlePartFive.setStyleSheet("color:Black; font-size:21px;")
       FlashyTitlePartOne.move(70, 470);
       FlashyTitlePartTwo.move(170, 474);
       FlashyTitlePartThree.move(255, 470);
       FlashyTitlePartFour.move(70, 530);
       FlashyTitlePartFive.move(70, 570);

       

       frontTitle = qtWid.QLabel(win)
       frontTitle.setText("Front")
       frontTitle.setFixedWidth(100)
       frontTitle.move(80, 50)
       frontTitle.setFont(QFont("Brush Script MT, Brush Script Std",30))

       BackTitle = qtWid.QLabel(win)
       BackTitle.setText("Back")
       BackTitle.setFixedWidth(100)
       BackTitle.move(320, 50)
       BackTitle.setFont(QFont("Brush Script MT, Brush Script Std",30))

       RightTitle = qtWid.QLabel(win)
       RightTitle.setText("Right")
       RightTitle.setFixedWidth(100)
       RightTitle.move(550, 50)
       RightTitle.setFont(QFont("Brush Script MT, Brush Script Std",30))

       LeftTitle = qtWid.QLabel(win)
       LeftTitle.setText("Left")
       LeftTitle.setFixedWidth(100)
       LeftTitle.move(80, 250)
       LeftTitle.setFont(QFont("Brush Script MT, Brush Script Std",30))

       UpTitle = qtWid.QLabel(win)
       UpTitle.setText("Up")
       UpTitle.setFixedWidth(100)
       UpTitle.move(320, 250)
       UpTitle.setFont(QFont("Brush Script MT, Brush Script Std",30))

       DownTitle = qtWid.QLabel(win)
       DownTitle.setText("Down")
       DownTitle.setFixedWidth(100)
       DownTitle.move(550, 250)
       DownTitle.setFont(QFont("Brush Script MT, Brush Script Std",30))

       win.show()
       sys.exit(app.exec_())

        

