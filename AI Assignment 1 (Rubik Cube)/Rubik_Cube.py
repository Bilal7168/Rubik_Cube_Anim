import copy

class Rubik_Cube:
    """description of class"""

    #prev Rotation String
    prev_rotation = 0

    #prev Cube Object
    prev_cube = 0
    

    def __init__(self):
        self.front  = [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']]
        self.back = [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]
        self.right = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
        self.left = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']]
        self.up = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]
        self.down = [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]


    def _overloader_self_(self, R_C_Param):
        R_C_Param_Combs = copy.deepcopy(R_C_Param.Get_Cube_Combinations()) #f, b, r, l, u, d
        self.front = R_C_Param_Combs[0]
        self.back = R_C_Param_Combs[1]
        self.right = R_C_Param_Combs[2]
        self.left = R_C_Param_Combs[3]
        self.up = R_C_Param_Combs[4]
        self.down = R_C_Param_Combs[5]

    def print_all_faces(self):
        print("\nFront Face: " , self.front)
        print("Back Face: " , self.back)
        print("Right Face: " , self.right)
        print("Left Face: " , self.left)
        print("Up Face: " , self.up)
        print("Down Face: " , self.down)

    #add rotation for this cube
    def set_prev_rot(self, rotation):
        self.prev_rotation = rotation;

    def set_prev_cube(self, _cube):
        self.prev_cube = _cube;

    def get_prev_rot(self):
        return self.prev_rotation;

    def get_prev_cube(self):
        return self.prev_cube;

    #self rotations

    def __rotate_frbl(self, index):
        temp_front = [self.front[index][0], self.front[index][1], self.front[index][2]];
        temp_right = [self.right[index][0], self.right[index][1], self.right[index][2]];
        temp_back = [self.back[index][0], self.back[index][1], self.back[index][2]];
        temp_left = [self.left[index][0], self.left[index][1], self.left[index][2]];

        self.front[index][0] = temp_right[0]; self.front[index][1] = temp_right[1]; self.front[index][2] = temp_right[2]; 
        self.left[index][0] = temp_front[0]; self.left[index][1] = temp_front[1]; self.left[index][2] = temp_front[2];  
        self.back[index][0] = temp_left[0]; self.back[index][1] = temp_left[1]; self.back[index][2] = temp_left[2]; 
        self.right[index][0] = temp_back[0]; self.right[index][1] = temp_back[1]; self.right[index][2] = temp_back[2];

    def __rotate_fubd(self, index):
        temp_front = [self.front[0][index], self.front[1][index], self.front[2][index]];
        temp_up = [self.up[0][index], self.up[1][index], self.up[2][index]];
        if(index == 2):
            temp_back = [self.back[0][0], self.back[1][0], self.back[2][0]];
        else:
            temp_back = [self.back[0][2], self.back[1][2], self.back[2][2]];
        temp_down = [self.down[0][index], self.down[1][index], self.down[2][index]];

        self.front[0][index] = temp_down[0]; self.front[1][index] = temp_down[1]; self.front[2][index] = temp_down[2]; 
        self.up[0][index] = temp_front[0]; self.up[1][index] = temp_front[1]; self.up[2][index] = temp_front[2];  
        if(index == 2):
            self.back[0][0] = temp_up[2]; self.back[1][0] = temp_up[1]; self.back[2][0] = temp_up[0]; 
        else:
            self.back[0][2] = temp_up[2]; self.back[1][2] = temp_up[1]; self.back[2][2] = temp_up[0]; 
        self.down[0][index] = temp_back[2]; self.down[1][index] = temp_back[1]; self.down[2][index] = temp_back[0];

    def __rotate_uldr(self, index):
        temp_up = [self.up[index][0], self.up[index][1], self.up[index][2]]
        temp_left = [self.left[0][index], self.left[1][index], self.left[2][index]]
        if(index == 2):
            temp_right = [self.right[0][0], self.right[1][0], self.right[2][0]]
            temp_down = [self.down[0][0], self.down[0][1], self.down[0][2]]
        else:
            temp_right = [self.right[0][2], self.right[1][2], self.right[2][2]]
            temp_down = [self.down[2][0], self.down[2][1], self.down[2][2]]

        self.up[index][0] = temp_left[2]; self.up[index][1] = temp_left[1]; self.up[index][2] = temp_left[0];
        self.left[0][index] = temp_down[0]; self.left[1][index] = temp_down[1]; self.left[2][index] = temp_down[2] 
        if(index == 2):
            self.right[0][0] = temp_up[0]; self.right[1][0] = temp_up[1]; self.right[2][0] = temp_up[2]
            self.down[0][0] = temp_right[2]; self.down[0][1] = temp_right[1]; self.down[0][2] = temp_right[0]
        else:
            self.right[0][2] = temp_up[0]; self.right[1][2] = temp_up[1]; self.right[2][2] = temp_up[2]
            self.down[2][0] = temp_right[2]; self.down[2][1] = temp_right[1]; self.down[2][2] = temp_right[0]

    def __check_face_similar(self, poss_coms, list_face):
        for i in range(6):
            if(list_face == poss_coms[i]):
                return True;
        return False;
            
    def clockwise_rotate_up(self):
        #rotate the top part, move the upper right->front->left->back
        self.__rotate_frbl(0)    
      
    def anti_clockwise_rotate_up(self):
        for i in range(3):
            self.__rotate_frbl(0)

    def clockwise_rotate_down(self):
        #rotate the top part, move the upper right->front->left->back
        self.__rotate_frbl(2)

    def anti_clockwise_rotate_down(self):
        for i in range(3):
            self.__rotate_frbl(2)

    def clockwise_rotate_right(self):
        #rotate the right part, move front->up->back->down
        self.__rotate_fubd(2)

    def anti_clockwise_rotate_right(self):
        for i in range(3):
            self.__rotate_fubd(2)

    def clockwise_rotate_left(self):
        #rotate the right part, move front->up->back->down
        self.__rotate_fubd(0)

    def anti_clockwise_rotate_left(self):
        for i in range(3):
            self.__rotate_fubd(0)

    def clockwise_rotate_front(self):
        #rotate the front part, move right->up->left->down
        self.__rotate_uldr(2)

    def anti_clockwise_rotate_front(self):
        for i in range(3):
            self.__rotate_uldr(2)

    def clockwise_rotate_back(self):
        #rotate the back part, move right->up->left->down
        self.__rotate_uldr(0)

    def anti_clockwise_rotate_back(self):
        for i in range(3):
            self.__rotate_uldr(0)
        
    #..end of self rotations

    def allFacesEqual(self):
        #declare the list of possible combinations
        Poss_combs = [[['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']], 
                      [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']], 
                      [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']], 
                      [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']], 
                      [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']], 
                      [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]]
    
        #check faces in array
        if (self.__check_face_similar(Poss_combs, self.front) 
           and self.__check_face_similar(Poss_combs, self.back) 
           and self.__check_face_similar(Poss_combs, self.up)
           and self.__check_face_similar(Poss_combs, self.down)
           and self.__check_face_similar(Poss_combs, self.left)
           and self.__check_face_similar(Poss_combs, self.right)
           ):
            return True
        else:
            return False

    #Main Solver

    def Get_Cube_Combinations(self):
        #Combine arrays in one
        Current_Cube = [self.front, self.back, self.right, self.left, self.up, self.down]
        
        #return the combinations of the cube
        return Current_Cube


