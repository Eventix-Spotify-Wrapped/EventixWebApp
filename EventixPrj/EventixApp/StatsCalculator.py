from datetime import datetime

import pandas as pd
import csv
import math
from collections import Counter
from .CSV_Reader import CSV_Reader
from EventixApp.models import Wrap, Card, CardTemplate


class StatsCalculate:
    def load_csv_data(filename):
        myList = []
        with open(filename) as fields:
            fields_data = csv.reader(fields, delimiter=',')
            next(fields_data)  # skip the header
            for row in fields_data:
                myList.append(row)
            return myList

    def create_list_of_objects(csv_file):
        transactions = CSV_Reader.create_transactions_from_csv(csv_file)
        return transactions

    def calculate_total_revenue_event(transactions, event_name):
        total_revenue = 0
        for i in range(len(transactions)):
            if transactions[i]['event_name'] == event_name:
                total_revenue = total_revenue + transactions[i]['ticket_value']
        return total_revenue

    def calculate_average_ticket_price(transactions, event_name):
        ticket_values = 0
        relevant_transactions_counter = 0
        for i in range(len(transactions)):
            if transactions[i]['event_name'] == event_name:
                ticket_values = ticket_values + transactions[i]['ticket_value']
                relevant_transactions_counter += 1
        average_ticket_price = ticket_values / relevant_transactions_counter
        return average_ticket_price

    def calculate_total_ticket_sells(transactions, event_name):
        relevant_transactions_counter = 0
        for i in range(len(transactions)):
            if transactions[i]['event_name'] == event_name:
                relevant_transactions_counter += 1
        return relevant_transactions_counter

    def calculate_day_most_tickets_sold(transactions, event_name):
        days = []
        for i in range(len(transactions)):
            if transactions[i]['event_name'] == event_name:
                date_time_obj = datetime.strptime(transactions[i]['created_at'], "%m/%d/%Y %H:%M")
                days.append(date_time_obj.date())
        most_common_day = Counter(days).most_common(1)
        return most_common_day[0][0]

    def calculate_events_per_year(transactions, event_name):
        events_per_year = 0
        for i in range(len(transactions)):
            if transactions[i]['event_name'] == event_name:
                events_per_year = 1
        return events_per_year

    def calculate_gender_percentage(transactions, event_name):
        male_counter = 0
        female_counter = 0
        relevant_transactions_counter = 0
        for i in range(len(transactions)):
            if transactions[i]['event_name'] == event_name:
                if transactions[i]['order_metadata_gender'] == 'male':
                    male_counter += 1
                    relevant_transactions_counter += 1
                else:
                    female_counter += 1
                    relevant_transactions_counter += 1
        if male_counter >= female_counter:
            percentage = male_counter / relevant_transactions_counter * 100
            return percentage, 100 - percentage
        else:
            percentage = female_counter / relevant_transactions_counter * 100
            return 100 - percentage, percentage
        # I always return a tuple as a data structure. This is because I can then use the tuple to create a pie chart in
        # the frontend. On position 0 there is always going to be the male percentage. On position 2 there is always going
        # to be the female percentage

    def calculate_average_age(transactions, event_name):
        age_sum = 0
        relevant_transactions_counter = 0
        for i in range(len(transactions)):
            if transactions[i]['event_name'] == event_name:
                age_sum = age_sum + transactions[i]['order_metadata_age']
                relevant_transactions_counter += 1
        average_age = age_sum / relevant_transactions_counter
        return average_age

    def calculate_showup_percentage(transactions, event_name):
        showup_counter = 0
        relevant_transactions_counter = 0
        for i in range(len(transactions)):
            if transactions[i]['event_name'] == event_name:
                relevant_transactions_counter += 1
                if transactions[i]['is_scanned'] == 1:
                    showup_counter += 1
        showup_percentage = showup_counter / relevant_transactions_counter * 100
        return showup_percentage

    def calculate_total_visitors(transactions, event_name):
        showup_counter = 0
        for i in range(len(transactions)):
            if transactions[i]['event_name'] == event_name:
                if transactions[i]['is_scanned'] == 1:
                    showup_counter += 1
        return showup_counter

    def calculate_city_percentage(transactions, event_name):
        relevant_transactions = [t for t in transactions if t['event_name'] == event_name and t.get(
            # 'order_metadata_city') is not None and not math.isnan(t['order_metadata_city'])]
            'order_metadata_city') is not None and not ['order_metadata_city']]
        city_counts = Counter(t['order_metadata_city'] for t in relevant_transactions if
                              t['order_metadata_city'] is not None and t['order_metadata_city'] != '')
        most_common_city = city_counts.most_common(1)
        if most_common_city:
            return most_common_city[0][0]
        else:
            return None

    def calculate_most_popular_country(transactions, event_name):
        countries = []
        total_transactions = 0
        for i in range(len(transactions)):
            if transactions[i]['event_name'] == event_name:
                country = transactions[i]['order_metadata_country']
                if country:  # This checks that country is not None or an empty string
                    countries.append(country)
                    total_transactions += 1
        most_common_country = Counter(countries).most_common(1)[0]
        most_common_country_name = most_common_country[0]
        most_common_country_count = most_common_country[1]
        percentage = (most_common_country_count / total_transactions) * 100
        return most_common_country_name, percentage

    def get_events_name_list():
        list = CSV_Reader.create_transactions_from_csv(
            "mock.csv"
        )
        data = []
        for element in list:
            data.append(element["event_name"])
        return data

    def get_events_name_list(guid):
        list = CSV_Reader.create_transactions_from_csv(
            "mock.csv"
        )
        data = []
        for element in list:
            if (element["account_id"] in guid):
                data.append(element["event_name"])
        return data

    def get_events_name_guid_keypair():
        list = CSV_Reader.create_transactions_from_csv(
            "mock.csv"
        )
        data = []
        for element in list:
            data.append({"Name": element["event_name"],
                         "Guid": element["account_id"]})
        return data

    def get_organizer_events_guid():
        list = CSV_Reader.create_transactions_from_csv(
            "mock.csv"
        )
        checkedOrganizers = []

        data = []
        for element in list:
            if (element["account_id"] not in checkedOrganizers):
                checkedOrganizers.append(element['account_id'])
                selectedOrganizer = element["shop_name"]
                obj = {"Organizer": selectedOrganizer,
                       "Guid": element["account_id"], "Events": []}
                for e in list:
                    if (selectedOrganizer in e["shop_name"]):
                        if (e["event_name"] not in obj["Events"]):
                            obj["Events"].append(e["event_name"])
                data.append(obj)

        return data

    def get_organizer_name_by_guid(guid):
        list = CSV_Reader.create_transactions_from_csv(
            "mock.csv"
        )

        data = []
        for element in list:
            if (element["account_id"] in guid):
                data = element["shop_name"]

        return data

    def get_organizer_events_guid_by_guid(guid):
        list = CSV_Reader.create_transactions_from_csv(
            "mock.csv"
        )
        checkedOrganizers = []

        data = []
        for element in list:
            if (element["account_id"] in guid):
                if (element["account_id"] not in checkedOrganizers):
                    checkedOrganizers.append(element['account_id'])
                    selectedOrganizer = element["shop_name"]
                    obj = {"Organizer": selectedOrganizer,
                           "Guid": element["account_id"], "Events": []}
                    for e in list:
                        if (selectedOrganizer in e["shop_name"]):
                            if (e["event_name"] not in obj["Events"]):
                                obj["Events"].append(e["event_name"])
                    data = obj

        return data

    def get_organizer_events_cards_guid_by_guid(guid):
        data = StatsCalculate.get_organizer_events_guid_by_guid(guid)

        completed_wraps_account_ids = Wrap.objects.values_list(
            'owner_account_id', flat=True)
        for owner in completed_wraps_account_ids:
            if (owner in guid):
                data["Cards"] = list(Card.objects.all().values("html_path").filter(
                    wrap=Wrap.objects.get(owner_account_id=guid)).values())

        return data
