import requests
API_KEY="6c4a79f1cc58c39f9b6255fec3b89181"
try: 
    def get_data(place,forecast_days=None,kind=None):
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()
        filter_data=data["list"]
        nr_values=8 * forecast_days
        filter_data=filter_data[:nr_values]
        return filter_data
except KeyError:
    print("you had enterd wrong place")



if __name__=="__main__":
    print(get_data(place="Tokyo",forecast_days=3,kind="temp"))



     