import pandas as pd
from .models import Transaction
import os
import django
import pathlib

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EventixPrj.settings")
django.setup()


class CSV_Reader:
    def create_transactions_from_csv(csv_file_path):
        csv_file_path = str(pathlib.Path(
            __file__).parent.resolve()) + '/' + csv_file_path
        df_tickets = pd.read_csv(csv_file_path,
                                 encoding='latin1', low_memory=False)
        transactions = []
        for _, row in df_tickets.iterrows():
            transaction_data = dict(order_id=row['order_id'], shop_name=row['shop_name'], event_name=row['event_name'],
                                    #   event_category=row['event_subcategories'],
                                    #    first_event=row['first_event_date_start'],
                                    #   last_event=row['last_event_date_end'],
                                    first_name=row['first_name'],
                                    last_name=row['last_name'], email=row['email'], ticket_name=row['ticket_name'],
                                    barcode=row['barcode'], order_status=row['order_status'],
                                    order_invalidated=row['order_invalidated'],
                                    order_invalidated_at=row['order_invalidated_at'],
                                    ticket_invalidated=row['ticket_invalidated'],
                                    ticket_invalidated_at=row['ticket_invalidated_at'], created_at=row['created_at'],
                                    paid_currency=row['paid_currency'], order_value=row['order_value'],
                                    order_fees=row['order_fees'], transaction_fees=row['transaction_fees'],
                                    ticket_value=row['ticket_value'], ticket_fees=row['ticket_fees'],
                                    optionals_value=row['optionals_value'], refunded_amount=row['refunded_amount'],
                                    payment_method=row['payment_method'], coupons=row['coupons'], device=row['device'],
                                    tracker=row['tracker'], tracker_name=row['tracker_name'], seat=row['seat'],
                                    is_scanned=row['is_scanned'], first_scanned_at=row['first_scanned_at'],
                                    order_metadata_first_name=row['order_metadata_first_name'],
                                    order_metadata_last_name=row['order_metadata_last_name'],
                                    order_metadata_wrong1=row['order_metadata_wrong1'],
                                    order_metadata_wrong2=row['order_metadata_wrong2'],
                                    order_metadata_wrong3=row['order_metadata_wrong3'],
                                    order_metadata_wrong4=row['order_metadata_wrong4'],
                                    order_metadata_wrong5=row['order_metadata_wrong5'],
                                    order_metadata_wrong6=row['order_metadata_wrong6'],
                                    order_metadata_wrong7=row['order_metadata_wrong7'],
                                    order_metadata_wrong8=row['order_metadata_wrong8'],
                                    order_metadata_city=row['order_metadata_city'],
                                    order_metadata_gender=row['order_metadata_gender'],
                                    order_metadata_province=row['order_metadata_province'],
                                    order_metadata_company=row['order_metadata_company'],
                                    order_metadata_country=row['order_metadata_country'],
                                    order_metadata_covid_no_symptoms=row['order_metadata_covid_no_symptoms'],
                                    order_metadata_age=row['order_metadata_age'],
                                    order_metadata_wrong9=row['order_metadata_wrong9'],
                                    order_metadata_wrong10=row['order_metadata_wrong10'],
                                    order_metadata_wrong11=row['order_metadata_wrong11'],
                                    order_metadata_wrong12=row['order_metadata_wrong12'],
                                    order_metadata_wrong13=row['order_metadata_wrong13'],
                                    order_metadata_wrong14=row['order_metadata_wrong14'],
                                    order_ticket_metadata_first_name=row['order_ticket_metadata_first_name'],
                                    order_ticket_metadata_last_name=row['order_ticket_metadata_last_name'],
                                    order_ticket_wrong1=row['order_ticket_wrong1'],
                                    order_ticket_metadata_email=row['order_ticket_metadata_email'],
                                    order_ticket_metadata_street=row['order_ticket_metadata_street'],
                                    order_ticket_metadata_street_number=row[
                                        'order_ticket_metadata_street_number'],
                                    order_ticket_metadata_street_number_additional=row[
                                        'order_ticket_metadata_street_number_additional'],
                                    order_ticket_metadata_postal=row['order_ticket_metadata_postal'],
                                    order_ticket_metadata_date_of_birth=row[
                                        'order_ticket_metadata_date_of_birth'],
                                    order_ticket_metadata_state=row['order_ticket_metadata_state'],
                                    order_ticket_metadata_city=row['order_ticket_metadata_city'],
                                    order_ticket_metadata_gender=row['order_ticket_metadata_gender'],
                                    order_ticket_metadata_province=row['order_ticket_metadata_province'],
                                    order_ticket_metadata_company=row['order_ticket_metadata_company'],
                                    order_ticket_metadata_country=row['order_ticket_metadata_country'],
                                    order_ticket_metadata_covid_no_symptoms=row[
                                        'order_ticket_metadata_covid_no_symptoms'],
                                    order_ticket_metadata_age=row['order_ticket_metadata_age'],
                                    order_ticket_wrong2=row['order_ticket_wrong2'],
                                    order_ticket_metadata_phone=row['order_ticket_metadata_phone'],
                                    order_ticket_metadata_fullname=row['order_ticket_metadata_fullname'],
                                    order_ticket_metadata_covid_one_household=row[
                                        'order_ticket_metadata_covid_one_household'],
                                    order_ticket_metadata_keep_me_informed=row[
                                        'order_ticket_metadata_keep_me_informed'],
                                    order_ticket_metadata_Diet=row['order_ticket_metadata_Diet'],
                                    geolocation_street_name=row['geolocation_street_name'],
                                    geolocation_street_number=row['geolocation_street_number'],
                                    geolocation_locality=row['geolocation_locality'],
                                    geolocation_postal_code=row['geolocation_postal_code'],
                                    geolocation_sub_locality=row['geolocation_sub_locality'],
                                    geolocation_admin_level_1=row['geolocation_admin_level_1'],
                                    geolocation_admin_level_2=row['geolocation_admin_level_2'],
                                    geolocation_country_code=row['geolocation_country_code'],
                                    geolocation_latitude=row['geolocation_latitude'],
                                    geolocation_longitude=row['geolocation_longitude'],
                                    ticket_pdf_link=row['ticket_pdf_link'])

            # transaction = Transaction(**transaction_data)

            transactions.append(transaction_data)

        return transactions
