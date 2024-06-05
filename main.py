# main.py
# Module for running the Land Renting System.

from operations import LandRentingSystem

def main():
    """
    Main function to run the Land Renting System.

    Creates an instance of LandRentingSystem, displays menu options,
    and performs corresponding actions based on user input.
    """
    # Path to the file containing land details.
    file_path = "land_data.txt"
    # Create an instance of LandRentingSystem.
    land_system = LandRentingSystem(file_path)

    while True:
        # Display menu options.
        print("\nMenu:")
        print("1. Rent Land")
        print("2. Return Land")
        print("3. Exit")
        # Prompt user to enter their choice.
        choice = input("Enter your choice (1/2/3): ")
        try:
            # Perform actions based on user choice.
            if choice == '1':
                land_system.rent_land()
            elif choice == '2':
                land_system.return_land()
            elif choice == '3':
                # Exit the program if the user chooses to.
                print("Exiting the Land Renting System.")
                break
            else:
                # Inform the user about an invalid choice.
                print("Invalid choice. Please enter a valid option.")
        except Exception as e:
            # Handle any errors that occur during execution.
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
