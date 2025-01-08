
def copy_file(source_file, destination_file):
    try:
       
        with open(source_file, 'r') as src:
           
            content = src.read()

        
        with open(destination_file, 'w') as dest:
           
            dest.write(content)

        print(f"Data has been successfully copied from '{source_file}' to '{destination_file}'.")
    except FileNotFoundError:
        print(f"The file '{source_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = input("Enter the name of the source file (with extension): ")
destination_file = input("Enter the name of the destination file (with extension): ")


copy_file(source_file, destination_file)
