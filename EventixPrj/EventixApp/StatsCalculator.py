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

    def calculate_total_revenue_event(transactions, account_id):

        total_revenue = 0
        for i in range(len(transactions)):
            if transactions[i]['account_id'] == account_id:
                total_revenue = total_revenue + transactions[i]['ticket_value']
        return total_revenue

    def calculate_average_ticket_price(transactions, account_id):
        ticket_values = 0
        relevant_transactions_counter = 0
        for i in range(len(transactions)):
            if transactions[i]['account_id'] == account_id:
                ticket_values = ticket_values + transactions[i]['ticket_value']
                relevant_transactions_counter += 1
        average_ticket_price = ticket_values / relevant_transactions_counter
        return average_ticket_price

    def calculate_total_ticket_sells(transactions, account_id):
        relevant_transactions_counter = 0
        for i in range(len(transactions)):
            if transactions[i]['account_id'] == account_id:
                relevant_transactions_counter += 1
        return relevant_transactions_counter

    def calculate_day_most_tickets_sold(transactions, account_id):
        days = []
        for i in range(len(transactions)):
            if transactions[i]['account_id'] == account_id:
                date_time_obj = datetime.strptime(transactions[i]['created_at'], "%m/%d/%Y %H:%M")
                days.append(date_time_obj.date())
        most_common_day = Counter(days).most_common(1)
        formatted_day = most_common_day[0][0].strftime("%d | %B")  # Format the date to only display month and day
        return formatted_day

    def calculate_events_per_year(transactions, account_id):
        events_per_year = 0
        for i in range(len(transactions)):
            if transactions[i]['account_id'] == account_id:
                events_per_year = 1
        return events_per_year

    def calculate_gender_percentage(transactions, account_id):
        male_counter = 0
        female_counter = 0
        relevant_transactions_counter = 0
        for i in range(len(transactions)):
            if transactions[i]['account_id'] == account_id:
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

    def calculate_average_age(transactions, account_id):
        age_sum = 0
        relevant_transactions_counter = 0
        for i in range(len(transactions)):
            if transactions[i]['account_id'] == account_id:
                age_sum = age_sum + transactions[i]['order_metadata_age']
                relevant_transactions_counter += 1
        average_age = age_sum / relevant_transactions_counter
        return average_age

    def calculate_showup_percentage(transactions, account_id):
        showup_counter = 0
        relevant_transactions_counter = 0
        for i in range(len(transactions)):
            if transactions[i]['account_id'] == account_id:
                relevant_transactions_counter += 1
                if transactions[i]['is_scanned'] == 1:
                    showup_counter += 1
        showup_percentage = showup_counter / relevant_transactions_counter * 100
        showup_percentage = round(showup_percentage)
        return showup_percentage

    def calculate_total_visitors(transactions, account_id):
        showup_counter = 0
        for i in range(len(transactions)):
            if transactions[i]['account_id'] == account_id:
                if transactions[i]['is_scanned'] == 1:
                    showup_counter += 1
        return showup_counter

    def calculate_city_percentage(transactions, account_id):
        relevant_transactions = [t for t in transactions if t['account_id'] == account_id and t.get(
            # 'order_metadata_city') is not None and not math.isnan(t['order_metadata_city'])]
            'order_metadata_city') is not None and not ['order_metadata_city']]
        city_counts = Counter(t['order_metadata_city'] for t in relevant_transactions if
                              t['order_metadata_city'] is not None and t['order_metadata_city'] != '')
        most_common_city = city_counts.most_common(1)
        if most_common_city:
            return most_common_city[0][0]
        else:
            return None

    def calculate_most_popular_country(transactions, account_id):
        countries = []
        total_transactions = 0
        for i in range(len(transactions)):
            if transactions[i]['account_id'] == account_id:
                country = transactions[i]['order_metadata_country']
                if country:  # This checks that country is not None or an empty string
                    countries.append(country)
                    total_transactions += 1
        most_common_country = Counter(countries).most_common(1)[0]
        most_common_country_name = most_common_country[0]
        most_common_country_count = most_common_country[1]
        percentage = (most_common_country_count / total_transactions) * 100
        percentage = round(percentage)
        return most_common_country_name, percentage

    def calculate_most_popular_city(transactions, account_id):
        cities = []
        total_transactions = 0
        for i in range(len(transactions)):
            if transactions[i]['account_id'] == account_id:
                city = transactions[i]['order_metadata_city']
                if city:
                    if isinstance(city, float):  # If the city is float (possibly NaN), skip it
                        continue
                    if city.strip() in ['<null>', '<unset>',
                                        '']:  # If it's '<null>', '<unset>', or an empty string, skip it
                        continue
                    cities.append(city)
                    total_transactions += 1

        if cities:  # Check if cities list is not empty
            most_common_city = Counter(cities).most_common(1)[0]
            most_common_city_name = most_common_city[0]
            most_common_city_count = most_common_city[1]
            percentage = (most_common_city_count / total_transactions) * 100
            percentage = round(percentage)
            return most_common_city_name
        else:
            return None, 0

    def calculate_most_popular_province(transactions, account_id):
        provinces = []
        total_transactions = 0
        for i in range(len(transactions)):
            if transactions[i]['account_id'] == account_id:
                province = transactions[i]['order_metadata_province']
                if province:
                    if isinstance(province, float):  # If the province is float (possibly NaN), skip it
                        continue
                    if province.strip() in ['<null>', '<unset>',
                                            '']:  # If it's '<null>', '<unset>', or an empty string, skip it
                        continue
                    provinces.append(province)
                    total_transactions += 1

        if provinces:  # Check if provinces list is not empty
            most_common_province = Counter(provinces).most_common(1)[0]
            most_common_province_name = most_common_province[0]
            most_common_province_count = most_common_province[1]
            percentage = (most_common_province_count / total_transactions) * 100
            percentage = round(percentage)
            return most_common_province_name
        else:
            return None, 0

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
            "ticketing_export_2023_03_24_11_27_16.csv"
        )
        data = []
        for element in list:
            data.append({"Name": element["event_name"],
                         "Guid": element["account_id"]})
        return data

    def get_organizer_events_guid():
        list = CSV_Reader.create_transactions_from_csv(
            "ticketing_export_2023_03_24_11_27_16.csv"
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
            "ticketing_export_2023_03_24_11_27_16.csv"
        )

        data = []
        for element in list:
            if (element["account_id"] in guid):
                data = element["shop_name"]

        return data

    def get_organizer_events_guid_by_guid(guid):
        list = CSV_Reader.create_transactions_from_csv(
            "ticketing_export_2023_03_24_11_27_16.csv"
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
