from faker import Faker
import csv
import random


class MockMaker:
    def GenerateMockData():
        # Define the number of rows to generate
        num_rows = 10

        # Define the names of the columns in the output CSV file
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
        fields = [
            "Order Id",
            "Shop Name",
            "Event Name",
            "Event Category",
            "First Event",
            "Last Event",
            "First Name",
            "Last Name",
            "Email",
            "Ticket Name",
            "Barcode",
            "Order Status",
            "Order Invalidated",
            "Order Invalidated At",
            "Ticket Invalidated",
            "Ticket Invalidated At",
            "Created At",
            "Paid Currency",
            "Order Value",
            "Order Fees",
            "Transaction Fees",
            "Ticket Value",
            "Ticket Fees",
            "Optionals Value",
            "Refunded Amount",
            "Payment Method",
            "Coupons",
            "Device",
            "Tracker",
            "Tracker Name",
            "Seat",
            "Is Scanned",
            "First Scanned At",
            "Order Metadata First Name",
            "Order Metadata Last Name",
            "Order Metadata Wrong1",
            "Order Metadata Wrong2",
            "Order Metadata Wrong3",
            "Order Metadata Wrong4",
            "Order Metadata Wrong5",
            "Order Metadata Wrong6",
            "Order Metadata Wrong7",
            "Order Metadata Wrong8",
            "Order Metadata City",
            "Order Metadata Gender",
            "Order Metadata Province",
            "Order Metadata Company",
            "Order Metadata Country",
            "Order Metadata Covid No Symptoms",
            "Order Metadata Age",
            "Order Metadata Wrong9",
            "Order Metadata Wrong10",
            "Order Metadata Wrong11",
            "Order Metadata Wrong12",
            "Order Metadata Wrong13",
            "Order Metadata Wrong14",
            "Order Ticket Metadata First Name",
            "Order Ticket Metadata Last Name",
            "Order Ticket Wrong1",
            "Order Ticket Metadata Email",
            "Order Ticket Metadata Street",
            "Order Ticket Metadata Street Number",
            "Order Ticket Metadata Street Number Additional",
            "Order Ticket Metadata Postal",
            "Order Ticket Metadata Date Of Birth",
            "Order Ticket Metadata State",
            "Order Ticket Metadata City",
            "Order Ticket Metadata Gender",
            "Order Ticket Metadata Province",
            "Order Ticket Metadata Company",
            "Order Ticket Metadata Country",
            "Order Ticket Metadata Covid No Symptoms",
            "Order Ticket Metadata Age",
            "Order Ticket Wrong2",
            "Order Ticket Metadata Phone",
            "Order Ticket Metadata Fullname",
            "Order Ticket Metadata Covid One Household",
            "Order Ticket Metadata Keep Me Informed",
            "Order Ticket Metadata Diet",
            "Geolocation Street Name",
            "Geolocation Street Number",
            "Geolocation Locality",
            "Geolocation Postal Code",
            "Geolocation Sub Locality",
            "Geolocation Admin Level 1",
            "Geolocation Admin Level 2",
            "Geolocation Country Code",
            "Geolocation Latitude",
            "Geolocation Longitude",
            "Ticket Pdf Link",
        ]

        # Initialize the Faker library
        fake = Faker()

        # Create a list of dictionaries to hold the generated data
        data = []

        # Generate fake data and write to a CSV file
        with open('fake_data.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for i in range(num_rows):
                order_id = fake.uuid4()
                shop_name = fake.company()
                event_name = fake.company() + " " + fake.word()
                event_category = fake.word()
                first_event = fake.date_time_between(
                    start_date='-1y', end_date='now')
                last_event = fake.date_time_between(
                    start_date=first_event, end_date='now')
                first_name = fake.first_name()
                last_name = fake.last_name()
                email = fake.email()
                ticket_name = fake.word() + " Ticket"
                barcode = fake.ean13()
                order_status = random.choice(["Pending", "Paid", "Cancelled"])
                order_invalidated = random.choice([True, False])
                order_invalidated_at = fake.date_time_between(
                    start_date=first_event, end_date='now') if order_invalidated else None
                ticket_invalidated = random.choice([True, False])
                ticket_invalidated_at = fake.date_time_between(
                    start_date=first_event, end_date='now') if ticket_invalidated else None
                created_at = fake.date_time_between(
                    start_date='-1y', end_date='now')
                paid_currency = random.choice(["USD", "EUR", "GBP"])
                order_value = round(random.uniform(10, 500), 2)
                order_fees = round(random.uniform(1, 20), 2)
                transaction_fees = round(random.uniform(0.5, 10), 2)
                ticket_value = round(random.uniform(10, 100), 2)
                ticket_fees = round(random.uniform(0.5, 5), 2)
                optionals_value = round(random.uniform(0, 50), 2)
                refunded_amount = round(random.uniform(0, order_value), 2)
                payment_method = random.choice(
                    ["Credit Card", "PayPal", "Bank Transfer"])
                coupons = fake.random_number(digits=5)
                device = random.choice(["Desktop", "Mobile"])
                tracker = fake.word()
                tracker_name = fake.company()
                seat = fake.word()
                is_scanned = random.choice([True, False])
                first_scanned_at = fake.date_time_between(
                    start_date=first_event, end_date='now') if is_scanned else None
                order_metadata_first_name = fake.first_name()
                order_metadata_last_name = fake.last_name()
                order_metadata_wrong1 = fake.word()
                order_metadata_wrong2 = fake.word()
                order_metadata_wrong3 = fake.word()
                order_metadata_wrong4 = fake.word()
                order_metadata_wrong5 = fake.word()
                order_metadata_wrong6 = fake.word()
                order_metadata_wrong7 = fake.word()
                order_metadata_wrong8 = fake.word()
                order_metadata_city = fake.city()
                order_metadata_gender = random.choice(
                    ["Male", "Female", "Other"])
                order_metadata_province = fake.state()
                order_metadata_company = fake.company()
                order_metadata_country = fake.country()
                order_metadata_covid_no_symptoms = random.choice([True, False])
                order_metadata_age = random.randint(18, 80)
                order_metadata_wrong9 = fake.word()
                order_metadata_wrong10 = fake.word()
                order_metadata_wrong11 = fake.word()
                order_metadata_wrong12 = fake.word()
                order_metadata_wrong13 = fake.word()
                order_metadata_wrong14 = fake.word()
                order_ticket_metadata_first_name = fake.first_name()
                order_ticket_metadata_last_name = fake.last_name()
                order_metadata_last_name = fake.last_name(),
                order_metadata_wrong1 = fake.word(),
                order_metadata_wrong2 = fake.word(),
                order_metadata_wrong3 = fake.word(),
                order_metadata_wrong4 = fake.word(),
                order_metadata_wrong5 = fake.word(),
                order_metadata_wrong6 = fake.word(),
                order_metadata_wrong7 = fake.word(),
                order_metadata_wrong8 = fake.word(),
                order_metadata_city = fake.city(),
                order_metadata_gender = random.choice(["M", "F"]),
                order_metadata_province = fake.state(),
                order_metadata_company = fake.company(),
                order_metadata_country = fake.country(),
                order_metadata_covid_no_symptoms = random.choice(
                    [True, False]),
                order_metadata_age = random.randint(18, 99),
                order_metadata_wrong9 = fake.word(),
                order_metadata_wrong10 = fake.word(),
                order_metadata_wrong11 = fake.word(),
                order_metadata_wrong12 = fake.word(),
                order_metadata_wrong13 = fake.word(),
                order_metadata_wrong14 = fake.word(),
                order_ticket_metadata_first_name = fake.first_name(),
                order_ticket_metadata_last_name = fake.last_name(),
                order_ticket_wrong1 = fake.word(),
                order_ticket_metadata_email = fake.email()
                event_category = fake.word()
                first_event = fake.date_this_month()
                street = fake.street_name()
                street_number = fake.building_number()
                street_number_additional = fake.secondary_address()
                postal = fake.postcode()
                dob = fake.date_of_birth()
                state = fake.state()
                city = fake.city()
                gender = fake.random_element(
                    elements=('Male', 'Female', 'Other'))
                province = fake.state()
                company = fake.company()
                country = fake.country()
                covid_no_symptoms = fake.boolean()
                age = fake.random_int(min=18, max=100, step=1)
                wrong2 = fake.word()
                phone = fake.phone_number()
                fullname = fake.name()
                covid_one_household = fake.boolean()
                keep_me_informed = fake.boolean()
                diet = fake.random_element(
                    elements=('Vegan', 'Vegetarian', 'Gluten-free', 'Keto', 'Paleo', 'None'))
                street_name = fake.street_name()
                street_number = fake.building_number()
                locality = fake.city()
                postal_code = fake.postcode()
                sub_locality = fake.city()
                admin_level_1 = fake.state()
                admin_level_2 = fake.city()
                country_code = fake.country_code()
                latitude = fake.latitude()
                longitude = fake.longitude()
                ticket_pdf_link = fake.url()
                row = [order_id, shop_name, event_name, event_category, first_event, street, street_number,
                       street_number_additional, postal, dob, state, city, gender, province, company, country,
                       covid_no_symptoms, age, wrong2, phone, fullname, covid_one_household, keep_me_informed,
                       diet, street_name, street_number, locality, postal_code, sub_locality, admin_level_1,
                       admin_level_2, country_code, latitude, longitude, ticket_pdf_link]

                writer.writerow(dict(zip(fields, row)))