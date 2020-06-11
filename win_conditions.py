
def P1_conditions():

    condition_1 = Board[0] == "X", Board[1] == "X", Board[2] == "X"
    condition_2 = Board[3] == "X", Board[4] == "X", Board[5] == "X"
    condition_3 = Board[6] == "X", Board[7] == "X", Board[8] == "X"
    
    condition_4 = Board[0] == "X", Board[3] == "X", Board[6] == "X" 
    condition_5 = Board[1] == "X", Board[4] == "X", Board[7] == "X"
    condition_6 = Board[2] == "X", Board[5] == "X", Board[8] == "X"
    
    condition_7 = Board[0] == "X", Board[4] == "X", Board[8] == "X"
    condition_8 = Board[6] == "X", Board[4] == "X", Board[2] == "X"

    def winner():

        global P1_condition

        if condition_1 == True or condition_2 == True or condition_3 == True or condition_4 == True or condition_5 == True or condition_6 == True or condition_7 == True or condition_8 == True


            P1_condition = True

        else:

            P1_condition = False

    winner()



def P2_conditions():
   
    condition_1 = Board[0] == "O", Board[1] == "O", Board[2] == "O"
    condition_2 = Board[3] == "O", Board[4] == "O", Board[5] == "O"
    condition_3 = Board[6] == "O", Board[7] == "O", Board[8] == "O"

    condition_4 = Board[0] == "O", Board[3] == "O", Board[6] == "O"
    condition_5 = Board[1] == "O", Board[4] == "O", Board[7] == "O"
    condition_6 = Board[2] == "O", Board[5] == "O", Board[8] == "O"

    condition_7 = Board[0] == "O", Board[4] == "O", Board[8] == "O"
    condition_8 = Board[6] == "O", Board[4] == "O", Board[2] == "O"

    def winner():

        global P2_condition

        if condition_1 == True or condition_2 == True or condition_3 == True or condition_4 == True or condition_5 == True or condition_6 == True or condition_7 == True or condition_8 == True

            P2_condition = True

        else:

            P2_condition = False

    winner()