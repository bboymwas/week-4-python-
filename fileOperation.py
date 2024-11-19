import os

def read_and_modify_file(input_filename, output_filename):
    try:
        # Open and read the input file
        with open(input_filename, 'r') as infile:
            data = infile.read()
        
        # Modify the data (example: converting to uppercase)
        modified_data = data.upper()

        # Write the modified data to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_data)
        
        print(f"Modified content written to '{output_filename}' successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied while trying to read '{input_filename}'.")
    except IsADirectoryError:
        print(f"Error: The path '{input_filename}' is a directory, not a file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Get the input file name from the user
    input_filename = input("Please enter the filename to read: ")
    
    # Define an output filename
    output_filename = "modified_" + os.path.basename(input_filename)

    read_and_modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()