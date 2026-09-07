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


def convert_units(unit_type):
    # Dictionary mapping units to their multiplier relative to a base unit
    conversion_rules = {
        "distance": {"m": 1.0,
                     "km": 1000.0,
                     "cm": 0.01
                     },
        "time": {"sec": 1.0,
                 "min": 60.0,
                 "hr": 3600.0
                 },
        "mass": {"g": 1.0,
                 "kg": 1000.0,
                 "T": 1000000.0
                 },
        "volume": {"ml": 1.0,
                   "l": 1000.0,
                   "kl" : 0.001
                   }
    }

    # Get rules for the selected type
    units_dict = conversion_rules[unit_type]
    available_units = ", ".join(units_dict.keys())

    # Get valid inputs from user
    print(f"\nAvailable units for {unit_type}: {available_units}")
    from_unit = input("Convert FROM unit: ").strip().lower()
    to_unit = input("Convert TO unit: ").strip().lower()

    if from_unit not in units_dict or to_unit not in units_dict:
        print("Error: One or both units are invalid.")
        return

    try:
        value = float(input(f"Enter amount in {from_unit}: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    # Conversion Logic: Convert to base unit first, then to target unit
    value_in_base = value * units_dict[from_unit]
    final_value = value_in_base / units_dict[to_unit]

    print(f"--> {value} {from_unit} = {final_value:.4f} {to_unit}")

# Main execution loop
if __name__ == "__main__":
    selected_type = get_unit_type()
    convert_units(selected_type)

