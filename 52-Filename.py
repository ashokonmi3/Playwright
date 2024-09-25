import datetime
import inspect
import os


def file_creation():
    # Get the current date and time
    now = datetime.datetime.now()
    print(f"current time: {now}")

    # Format it as a string for the file name
    # Example format: "2024-09-22_14-30-45"
    file_name = now.strftime("%Y-%m-%d_%H-%M-%S")

    # Get the current function name using the inspect module
    function_name = inspect.currentframe().f_code.co_name

    # Create the file name with the function name and date/time
    file_name_with_extension = f"{function_name}_{file_name}.txt"

    # Output the file name
    print(file_name_with_extension)

    # Use this file name to save a file
    with open(file_name_with_extension, "w") as file:
        file.write(f"This file was created by the function: {
                   function_name} on {file_name}")
    current_file_name = os.path.basename(__file__)
    full_file_name = f"{current_file_name}_{function_name}_{file_name}.txt"

    with open(full_file_name, "w") as file:
        file.write(f"This file was created by the function: {
                   function_name} on {full_file_name}")

    print(f"The  file name is: {full_file_name}")


# Call the function to create a file
file_creation()
