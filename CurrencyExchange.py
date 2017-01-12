import requests
import json

app_id = "e466cf69644f4eb0bd22bb0b727fbbb9"

def RequestCurrency():

    request = requests.get("https://openexchangerates.org/api/currencies.json")
    currencyDict = request.json()

    listOfCountries = []

    for key in currencyDict:

        country = key
        listOfCountries.append(country)

    return listOfCountries

countryList = RequestCurrency()

print("Here is a list of the available countries.")

countryTemp = ""

for x in countryList:

    countryTemp = x
    print(countryTemp)

firstCountry = input("Please enter the the currency code you have: ").upper()

print(firstCountry)
