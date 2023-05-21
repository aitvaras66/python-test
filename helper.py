def days_to_units(num_of_days, conversion_unit):
    # condition_check = num_of_days > 0
    # print(type(condition_check))
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"


# def scope_check():
#     print(name_of_unit)


def validate_and_execute(days_and_unit_dictionary):
    try:
        # if user_input.isdigit():
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("no zeros pls")
        else:
            print("negative")
    except ValueError:
        print("input NaN")


user_input_message = "enter a number of dates\n"
