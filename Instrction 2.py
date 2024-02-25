# checks users enter yes (y) or no (n)
def yes_no(queston):
    while True:
        response = input(queston).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("you did not choose a valid response")


            #main routine
            while True:
                want_instructions = yes_no("do you want to read the instruction ?")
                print(f"you chose {want_instructions}")