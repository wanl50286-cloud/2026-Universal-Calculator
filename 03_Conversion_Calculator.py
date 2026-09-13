# Generates headings (eg: ---- Heading ----
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    statement_generator("insructions", "-")

    print('''
- Please enter your measurement type 
- Put how much you want to convert
- Choose from one of the units suggested
- When finished enter xxx to finish code.
    ''')


# Ask user for measurement type (distance / time / mass / volume)
def measurement_type():
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
            print("Choose from [distance (dis, d, distance), time (t, time), mass (m, mass), or volume (v, vol, volume)] ")


# enter a number that is more than zero
def num_check(question):
    error = "Please enter a valid number that is more than zero\n"
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
            print("This is not convertable, please enter a different unit ")
            print("Choose from [mass (T, kg, g, mg), distance (km, m, cm, mm), time (hr, min, sec), volume (kl, l, ml)] ")

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

    unit_type = measurement_type()
    print(f"You chose {unit_type} ")

    if measurement_type == volume_dict:
        print("Choose from [kl, l, or ml]")

    if unit_type == "xxx":
        print("Thank you for using conversion calculator")
        break
    elif unit_type == "distance":
        dict_to_use = distance_dict
    elif unit_type == "mass":
        dict_to_use = mass_dict
    elif unit_type == "time":
        dict_to_use = time_dict
    elif unit_type == "volume":
        dict_to_use = volume_dict
    else:
        print(f"Error: '{unit_type}' is not a recognized measurement type.")
        continue

    options = list(dict_to_use)
    print(f"Please choose from {options}")

    # get amount and units
    amount = num_check("how much? ")
    from_unit = unit_checker("From? ", dict_to_use)
    to_unit = unit_checker("To? ", dict_to_use)

    # multiply ro get to our standard value...
    multiply_by = dict_to_use[to_unit]
    standard = amount * multiply_by

    # divide to get our desired value
    divide_by = dict_to_use[from_unit]
    answer = standard / divide_by
    print(f"There are {answer} {to_unit} in {amount} {from_unit} ")

