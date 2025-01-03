#PostLab2
def navigate_file():
    # Prompt the user for a filename
    filename = input("Enter the filename: ")
    
    try:
        # Open the file and read the lines into a list
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        if not lines:
            print("The file is empty. No lines to display.")
            return

        # Enter a loop to navigate through the lines
        while True:
            print(f"\nThe file contains {len(lines)} lines.")
            
            # Prompt the user for a line number
            try:
                line_number = int(input(f"Enter a line number (1 to {len(lines)}, or 0 to quit): "))
                
                if line_number == 0:
                    print("Exiting program.")
                    break
                elif 1 <= line_number <= len(lines):
                    print(f"Line {line_number}: {lines[line_number - 1].strip()}")
                else:
                    print(f"Invalid line number. Please enter a number between 1 and {len(lines)}, or 0 to quit.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Call the function to start the program
navigate_file()
