Country = {
    "Belarus":["Minsk","Grodno","Brest"],
    "Ukraine":["Kyiv","Kharkiv","Lviv"]
    }

city = input("Enter city:")
for country, cities in Country.items():
    if city in cities:
        print(f"{city} is a city in {country}")
        break
else:
    print(f"Country for {city} not found")
