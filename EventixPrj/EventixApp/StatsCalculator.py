import pandas as pd
import csv
import math
from collections import Counter
from .CSV_Reader import CSV_Reader


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

    def get_events_name_list():
        list = CSV_Reader.create_transactions_from_csv(
            "mock.csv"
        )
        data = []
        for element in list:
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