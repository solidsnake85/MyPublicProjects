import requests
import yelpconfig

url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization": "Bearer " + yelpconfig.api_key
}
params = {
    "term": "pizza",
    "location": "LA"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
names = [business["name"]
    for business in businesses if business["rating"] > 4.5]

print(names)
