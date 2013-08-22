# abusive_height_converter.py
# by Victoria Ward
# A program to convert height in cm to height in feet and vice versa


def is_num(string):                                             #defines function to check if input is number or decimal
        try: 
            float(string)
            return True
        except ValueError:
            return False

def main():
    
    unit = input("Hello there! Right, let's find out your height! Do you know your height in cm or feet? ").lower()  #checks if user knows cm or feet

    while unit != "cm" and unit != "feet":                      #checks user inputs valid answer
        unit = input("That doesn't answer my question. Let's try again. Do you know your height in cm or 'feet? Type 'cm' or 'feet'. ").lower()

    

    if unit == "cm":
        cm = input("Great. So, tell me your height in cms. ")   #asks for height in cm
        while str.isdigit(cm) == False:                         #checks user inputs number answer
            cm = input("That's not a number. Tell me your height in cms, for exmple, you could say 103, or 204! ")

        cm = int(cm)                                            #converts string to int for calculation
        height = str(round((cm * 0.393701) / 12, 1))            #calculates height in feet
        print ("You're", height, "feet tall.")                  #dispays height in feet
        if cm >= 211:                                           #comments on user's height
            print ("Oh we've got ourselves a comedian.")
        elif 191 <= cm <= 210:                                            
            print ("Wow! And does the circus pay well?") 
        elif 181 <= cm <= 190:
            print ("Yawn. Average.")
        elif 176 <= cm <= 180:
            print ("How's the weather down there?")
        elif 171 <= cm <= 175:
            print ("Oh it's YOU! I just loved you in Lord of the Rings.")
        elif 166 <= cm <= 170:
            print ("I'm sorry. I just thought you were standing very far away.")
        elif 161 <= cm <= 165:
            print ("So, can you limbo under a staple?")
        else:
            print ("Whoa, you're so short you could bungee jump off a curb!")
            
            

    elif unit == "feet":
        feet = input("Great. So, tell me your height in feet. ")#asks for height in feet
        while is_num(feet) == False:                            #checks user inputs number answer
            feet = input("That's not a number. Tell me your height in feet, for example, you could say 5.5, or 7.2! ")                                                               #checks user inputs number answer

        feet = float(feet)                                      #converts string to float for calculation
        height = str(round((feet * 12) / 0.393701))             #calculates height in cm                                                    
        print ("You're", height, "cm tall.")                    #displays height in cm
        if feet >= 6.9:                                         #comments on user's height
            print ("Oh we've got ourselves a comedian, have we?")
        elif 6.3 <= feet <= 6.8:                                            
            print ("Wow! And does the circus pay well?") 
        elif 5.9 <= feet <= 6.2:
            print ("Yawn. Average.")
        elif 5.7 <= feet <= 5.8:
            print ("How's the weather down there?")
        elif feet == 5.6:
            print ("Oh it's YOU! I just loved you in Lord of the Rings.")
        elif feet == 5.5:
            print ("I'm sorry. I just thought you were standing very far away.")
        elif feet == 5.4:
            print ("So, can you limbo under a staple?")
        else:
            print ("Whoa, you're so short you could bungee jump off a curb!")
        
    
    return ()

