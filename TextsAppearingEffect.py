import time
import msvcrt

def MakeTextEffect(text,FastMode):
    letters = list(text)
    for i, letter in enumerate(text):
        if msvcrt.kbhit():              
            key = msvcrt.getch()         
            if key == b"\r": 
                print(text[i:], end="", flush=True) 
                break           

        print(letter, end="", flush=True)
        Delay = 0.05
        if(FastMode):
            Delay = 0.01
        time.sleep(Delay)

    print("")
    

    