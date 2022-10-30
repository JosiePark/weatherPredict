import os
import pandas as pd

from weatherPredict.api_funcs import visualCrossingAPI
from config import api_key


def get_weather_data(
    location = "california", 
    start_date = "2019-01-01",
    end_date = "2020-12-31"
    ):

    api = visualCrossingAPI(api_key = api_key)
    df = api.get_data(
        location=location,
        start_date=start_date,
        end_date=end_date
        )

    return df

if __name__ == "__main__":

    df = get_weather_data()
    # df = pd.read_csv(
    #     "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/california/2019-01-01/2020-12-31?unitGroup=metric&include=days&key=GJGGYNTW6FW3LZAJBHLHSUVY9&contentType=csv"
    # )
    df.to_csv(os.path.join("data", "weather_data.csv"))
