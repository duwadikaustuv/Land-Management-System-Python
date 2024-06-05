class LandReader:
    """Class to read land details from a file."""

    def read_land_details(file_path):
        """
        Reads land details from a file.

        Args:
            file_path (str): Path to the file containing land details.

        Returns:
            list: A list containing lists of land details.
        """
        lands = []
        try:
            # Open the file for reading.
            with open(file_path, 'r') as file:
                # Read each line in the file.
                for line in file:
                    # Split the line into land details.
                    land_details = line.strip().split(', ')
                    # Append the land details to the list of lands.
                    lands.append(land_details)
        except FileNotFoundError:
            # Handle the case when the file is not found.
            print("land_details.txt not found")
        return lands
