class TrendReader:
    def AnalyzeTrends(account, startDate, endDate):
        return {
            "Trend Analysis": {
                "Account": "Template",
                "Found Trends": [
                    {
                        # tickets sold out in 10 min
                        "Trend": "Sell-out timeframe",
                        "BeginDate": "06/09/2010 10:30 PM",
                        "EndDate": "06/09/2010 10:40 PM",
                    },
                    {
                        "Trend": "Country insight",
                        "BeginDate": "06/09/2010 10:30 PM",
                        "EndDate": "06/09/2010 10:40 PM",
                    },
                ],
            }
        }

    # every trend should correspond to a method in CardService.py which will generate a card for that trend
