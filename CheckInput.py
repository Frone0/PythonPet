import colors as color


def GetResponse(Question, AllowedAnswers):
    
    while True:
        PlayerInput = input(Question).strip().lower()
         
        if(PlayerInput in AllowedAnswers):
            return PlayerInput
        else:
            print(color.RED + "Wrong input!" + color.RESET)   