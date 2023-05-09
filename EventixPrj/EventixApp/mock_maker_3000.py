from faker import Faker
import csv


class MockMaker:
    def GenerateMockData():
        # Define the number of rows to generate
        num_rows = 10

        # Define the names of the columns in the output CSV file
        column_names_template = ["Name", "Age", "Email", "Address"]

        column_names = [
            "order_id",
            "shop_name",
            "event_name",
            "event_category",
            "first_event",
            "last_event",
            "first_name",
            "last_name",
            "email",
            "ticket_name",
            "barcode",
            "order_status",
            "order_invalidated",
            "order_invalidated_at",
            "ticket_invalidated",
            "ticket_invalidated_at",
            "created_at",
            "paid_currency",
            "order_value",
            "order_fees",
            "transaction_fees",
            "ticket_value",
            "ticket_fees",
            "optionals_value",
            "refunded_amount",
            "payment_method",
            "coupons",
            "device",
            "tracker",
            "tracker_name",
            "seat",
            "is_scanned",
            "first_scanned_at",
            "order_metadata_first_name",
            "order_metadata_last_name",
            "order_metadata_wrong1",
            "order_metadata_wrong2",
            "order_metadata_wrong3",
            "order_metadata_wrong4",
            "order_metadata_wrong5",
            "order_metadata_wrong6",
            "order_metadata_wrong7",
            "order_metadata_wrong8",
            "order_metadata_city",
            "order_metadata_gender",
            "order_metadata_province",
            "order_metadata_company",
            "order_metadata_country",
            "order_metadata_covid_no_symptoms",
            "order_metadata_age",
            "order_metadata_wrong9",
            "order_metadata_wrong10",
            "order_metadata_wrong11",
            "order_metadata_wrong12",
            "order_metadata_wrong13",
            "order_metadata_wrong14",
            "order_ticket_metadata_first_name",
            "order_ticket_metadata_last_name",
            "order_ticket_wrong1",
            "order_ticket_metadata_email",
            "order_ticket_metadata_street",
            "order_ticket_metadata_street_number",
            "order_ticket_metadata_street_number_additional",
            "order_ticket_metadata_postal",
            "order_ticket_metadata_date_of_birth",
            "order_ticket_metadata_state",
            "order_ticket_metadata_city",
            "order_ticket_metadata_gender",
            "order_ticket_metadata_province",
            "order_ticket_metadata_company",
            "order_ticket_metadata_country",
            "order_ticket_metadata_covid_no_symptoms",
            "order_ticket_metadata_age",
            "order_ticket_wrong2",
            "order_ticket_metadata_phone",
            "order_ticket_metadata_fullname",
            "order_ticket_metadata_covid_one_household",
            "order_ticket_metadata_keep_me_informed",
            "order_ticket_metadata_Diet",
            "geolocation_street_name",
            "geolocation_street_number",
            "geolocation_locality",
            "geolocation_postal_code",
            "geolocation_sub_locality",
            "geolocation_admin_level_1",
            "geolocation_admin_level_2",
            "geolocation_country_code",
            "geolocation_latitude",
            "geolocation_longitude",
            "ticket_pdf_link",
        ]

        # Customize the names of the columns
        custom_column_names = [
            "Full Name",
            "Years Old",
            "Email Address",
            "Home Address",
        ]

        # Initialize the Faker library
        fake = Faker()

        # Create a list of dictionaries to hold the generated data
        data = []

        # Generate mock data for each row
        for i in range(num_rows):
            row = {
                "Name": fake.name(),
                "Age": fake.random_int(min=18, max=65),
                "Email": fake.email(),
                "Address": fake.address(),
            }
            data.append(row)

        # Write the generated data to a CSV file with the custom column names
        with open("mock_data.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=custom_column_names)
            writer.writeheader()
            for row in data:
                writer.writerow(
                    {
                        custom_column_names[i]: row[column_names_template[i]]
                        for i in range(len(column_names_template))
                    }
                )
