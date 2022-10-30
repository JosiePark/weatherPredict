import os
import pandas as pd

class visualCrossingAPI():

    def __init__(self, api_key):

        self.base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
        self.content_type = "csv"
        self.include = "days"
        self.unit_group = "metric"
        self.api_key = api_key

    def _make_query(self, location, start_date, end_date):

        api_query = self.base_url + location + "/" + start_date + "/" + end_date
        api_query += "?"
        api_query += "unitGroup="+ self.unit_group
        api_query += "&include="+ self.include
        api_query += "&key=" + self.api_key
        api_query += "&contentType=csv"

        return api_query

    def get_data(self, location, start_date, end_date):

        api_query = self._make_query(location, start_date, end_date)
        
        print("reading from ", api_query)
        try:
            df = pd.read_csv(api_query)
        except:
            print("could not read from " + api_query)
            return

        return df