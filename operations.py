from read import LandReader
from write import write_invoice
import datetime

class LandRentingSystem:
    """Class to manage operations related to land renting."""
    def __init__(self, file_path):
        """
        Initializes the LandRentingSystem with a file path.

        Args:
            file_path (str): Path to the file containing land details.
        """
        self.file_path = file_path

    def display_available_lands(self):
        """
        Displays available lands for rent.
        """
        # Read land details from the file and display available lands.
        lands = LandReader.read_land_details(self.file_path)
        for land_details in lands:
            # Print land details.
            print(f"Kitta: {land_details[0]}, City: {land_details[1]}, Direction: {land_details[2]}, Area: {land_details[3]}, Price: {land_details[4]}, Status: {land_details[5]}")

    def rent_land(self):
        """
        Rents a land to a customer.

        Displays available lands, prompts user to select a land by kitta number,
        verifies availability and area, collects customer details, calculates
        total rent, generates invoice, updates land status, and writes changes to file.
        """
        print("\nRent Land:")
        # Display available lands for rent.
        self.display_available_lands()
        while True:
            # Prompt user to enter kitta number of the land to rent.
            kitta = input("Enter the kitta number of the land you want to rent: ")
            # Read land details from file.
            lands = LandReader.read_land_details(self.file_path)
            found = False
            for land_details in lands:
                city = land_details[1]
                direction = land_details[2]
                price = land_details[4]
                # Check if the selected land is available for rent.
                if land_details[0] == kitta:
                    if land_details[-2] == 'Available':
                        found = True
                        land_area = int(land_details[3])
                        break
                    else:
                        print("Land is not available for rent. Please choose another kitta number.")
                        break
            if found:
                break

        # Collect customer details.
        customer_name = input("Enter your name: ")
        phone_number = input("Enter your phone number: ")
        while True:
            # Prompt user to enter number of anas (land area) to rent.
            number_of_anas = int(input(f"Enter number of anas (land area) (should be {land_area}): "))
            if number_of_anas != land_area:
                print(f"You must rent the entire {land_area} anas of land. Please enter again.")
            else:
                break

        # Prompt user to enter duration of rent in months.
        duration = int(input("Enter the duration of rent (in months): "))
        # Generate invoice for the rent.
        invoice_text = write_invoice(customer_name, phone_number, kitta, city, direction, price, number_of_anas, duration)

        print("\nInvoice:")
        print(invoice_text)

        # Update land status to 'Not Available' and update duration.
        for land_details in lands:
            if land_details[0] == kitta:
                land_details[-2] = 'Not Available'
                land_details[-1] = str(duration)
                break

        # Write updated land details to file.
        with open(self.file_path, 'w') as file:
            for land_details in lands:
                file.write(', '.join(land_details) + '\n')

        print("Land rented successfully.")

    def return_land(self):
        """
        Returns a rented land.

        Displays available lands, prompts user to select a land by kitta number,
        verifies availability and area, collects customer details, calculates
        fine (if applicable), generates invoice, updates land status, and writes changes to file.
        """
        print("\nReturn Land:")
        # Display available lands for return.
        self.display_available_lands()
        while True:
            # Prompt user to enter kitta number of the land to return.
            kitta = input("Enter the kitta number of the land you want to return: ")
            # Read land details from file.
            lands = LandReader.read_land_details(self.file_path)
            found = False
            for land_details in lands:
                city = land_details[1]
                direction = land_details[2]
                price = land_details[4]
                original_duration = int(land_details[-1])
                # Check if the selected land is currently rented.
                if land_details[0] == kitta:
                    if land_details[-2] == 'Not Available':
                        found = True
                        land_area = int(land_details[3])
                        break
                    else:
                        print("Land is not currently rented. Please choose another kitta number.")
                        break
            if found:
                break

        # Collect customer details.
        customer_name = input("Enter your name: ")
        phone_number = input("Enter your phone number: ")
        while True:
            # Prompt user to enter number of anas (land area) to return.
            number_of_anas = int(input(f"Enter number of anas (land area) (should be {land_area}): "))
            if number_of_anas != land_area:
                print(f"You must return the entire {land_area} anas of land. Please enter again.")
            else:
                break

        # Prompt user to enter actual duration of rent in months.
        returned_duration = int(input("Enter the duration of actual rent (in months): "))
        
        fine = 0

        # Calculate fine if the returned duration exceeds the original duration.
        if returned_duration > original_duration:
            fine = 0.1 * int(price) * (returned_duration - original_duration) + (returned_duration - original_duration) * int(price)

        # Generate invoice for the return.
        invoice_text = write_invoice(customer_name, phone_number, kitta, city, direction, price, number_of_anas, original_duration, fine)

        print("\nInvoice:")
        print(invoice_text)

        # Update land status to 'Available' and reset duration.
        for land_details in lands:
            if land_details[0] == kitta:
                land_details[-2] = 'Available'
                land_details[-1] = '0'
                break

        # Write updated land details to file.
        with open(self.file_path, 'w') as file:
            for land_details in lands:
                file.write(', '.join(land_details) + '\n')

        print("Land returned successfully.")
