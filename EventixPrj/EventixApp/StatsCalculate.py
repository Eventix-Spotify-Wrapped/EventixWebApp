import pandas as pd
import csv



def load_csv_data(filename):
    myList = []
    with open(filename) as fields:
        fields_data = csv.reader(fields, delimiter=',')
        next(fields_data)  # skip the header
        for row in fields_data:
            myList.append(row)
        return myList


def calculate_total_revenue(transactions):
    total_revenue = sum(transaction.ticket_value for transaction in transactions)
    return total_revenue

def calculate_average_ticket_price(transactions):
    ticket_values = [transaction.ticket_value for transaction in transactions]
    average_ticket_price = sum(ticket_values) / len(ticket_values)
    return average_ticket_price


def calculate_transactions_by_payment_method(transactions):
    payment_methods = {}
    for transaction in transactions:
        payment_method = transaction.payment_method
        if payment_method in payment_methods:
            payment_methods[payment_method] += 1
        else:
            payment_methods[payment_method] = 1
    return payment_methods
