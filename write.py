import datetime

def write_invoice(customer_name, phone_number, kitta, city, direction, price, number_of_anas, duration, fine=0, print_invoice=True):
    """
    Writes invoice details to a file and optionally prints the invoice.

    Args:
        customer_name (str): Name of the customer.
        phone_number (str): Phone number of the customer.
        kitta (str): Kitta number of the land.
        city (str): City where the land is located.
        direction (str): Direction of the land.
        price (str): Price of renting the land.
        number_of_anas (int): Number of anas (land area).
        duration (int): Duration of rent in months.
        fine (int, optional): Fine amount, default is 0.
        print_invoice (bool, optional): Whether to print the invoice, default is True.

    Returns:
        str: Name of the invoice file.
    """
    # Get the current timestamp for the invoice.
    invoice_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Generate a unique invoice file name.
    invoice_file_name = f"{customer_name}_{invoice_timestamp}_invoice.txt"

    # Calculate the total amount to be paid.
    total_amount = int(price) * duration + fine

    try:
        # Open the invoice file for writing.
        with open(invoice_file_name, 'w') as invoice_file:
            # Write header and invoice details to the file.
            invoice_file.write("\n")
            invoice_file.write("\n")
            invoice_file.write("                        Techno Property Nepal\n")
            invoice_file.write("                Kathmandu, Nepal | Phone No. 987654321\n")
            invoice_file.write("--------------------------------------------------------------\n")
            invoice_file.write("Customer Details:\n")
            invoice_file.write("--------------------------------------------------------------\n")
            invoice_file.write(f"Customer Name: {customer_name}\n")
            invoice_file.write(f"Phone Number: {phone_number}\n\n")
            invoice_file.write("--------------------------------------------------------------\n")
            invoice_file.write("Land Details:\n")
            invoice_file.write("--------------------------------------------------------------\n")
            invoice_file.write(f"Kitta: {kitta}\n")
            invoice_file.write(f"City: {city}\n")
            invoice_file.write(f"Direction: {direction}\n")
            invoice_file.write(f"Price: {price}\n")
            invoice_file.write(f"Area: {number_of_anas} anas\n")
            invoice_file.write(f"Duration: {duration} months\n")
            if fine > 0:
                invoice_file.write(f"Fine: {fine}\n")
            invoice_file.write("--------------------------------------------------------------\n")
            invoice_file.write(f"Total Amount: {total_amount}\n")
            invoice_file.write(f"Transaction Time: {invoice_timestamp}\n")

        if print_invoice:
            # Write customer and land details to the file.
            print("Invoice generated successfully. Printing invoice...")
            # Open the generated invoice file and print its contents.
            with open(invoice_file_name, 'r') as invoice_file:
                print(invoice_file.read())

        return invoice_file_name

    except Exception as e:
        # Handle errors that may occur during invoice generation.
        print(f"An error occurred while generating the invoice: {e}")
        return None
