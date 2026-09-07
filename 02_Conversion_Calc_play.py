# Generates headings (eg: ---- Heading ----
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    statement_generator("insructions", "-")

    print('''
- Please enter your measurement type 
- Answer all the questions correctly
- When finished enter xxx to finish code.
    ''')


# Ask user for measurement type (distance / time / mass / volume)
def get_unit_type():
    while True:
        response = input("Measurement type: ").lower()

        # check for the exit code
        if response == "xxx":
            return response

        # check if it's distance
        elif response in ['dis', 'd', 'distance']:
            return "distance"

        # check for time
        elif response in ['t', 'time']:
            return "time"

        # check for mass
        elif response in ['m', 'mass']:
            return "mass"

        # check for volume
        elif response in ['v', 'volume', 'vol']:
            return "volume"

        # if the response is invalid output an error
        else:
            print("Please enter a valid measurement type")


# enter a number that is more than zero
def num_check(question):
    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def unit_checker(question, valid_dict):
    """Checks units are from the correct domain"""

    while True:
        response = input(question)

        if response in valid_dict:
            return response
        else:
            print("This is not convertable, please enter a different unit")

print("program continues")

distance_dict ={
    "mm" : 1000,
    "cm" : 100,
    "m" : 1,
    "km" : 0.001
}

time_dict ={
    "sec" : 3600,
    "min" : 60,
    "hr" : 1
}

mass_dict ={
    "mg" : 1000000,
    "g" : 1000,
    "kg" : 1,
    "T" : 0.001
}

volume_dict ={
    "ml" : 1000,
    "l" : 1,
    "kl" : 0.001
}

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")


if want_instructions == "":
    instructions()

# Main routine
while True:

    unit_type = get_unit_type()

    print(f"You chose {get_unit_type}")

    if get_unit_type == "xxx":
        break

    # get amount and units
    amount = float(input("how much? "))
    from_unit = input("What unit do you have? ")
    to_unit = input("What unit do you want? ")

    # Look up value
    multiply_by = distance_dict[to_unit]
    answer = amount * multiply_by

    print(f"There are {answer} {to_unit} in {amount} {from_unit} ")

