def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("you did not choose a valid response")


print("🎲🎲roll it 13🎲🎲")


def instructions():
    print('''
    *** Instructions ***
    Do something
    and then do something else
    etc
       ''')


want_instructions = yes_no("do you want to read the instructions?")

if want_instructions == "yes":
    instructions()
print("program ends")
