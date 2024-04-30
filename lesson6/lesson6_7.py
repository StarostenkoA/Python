from pyowm import OWM


owm = OWM('3b7520cfa14d8220f49bed37a19a7b4d')
mgr = owm.weather_manager()

city=""
while city!="Quit":
    city=input("city:")
    if(city!="Quit"):
        observation = mgr.weather_at_place(city)
        w = observation.weather
        print(f"status - {w.status}")
        print(f"detailed_status - {w.detailed_status}")
        print(f"temperature - {w.temperature('celsius')['temp']}")
        wind=w.wind()
        print("WIND")
        print(f"wind speed - {wind['speed']} m/s")
        print(f"wind deg - {wind['deg']}")
        print(f"wind gust - {wind['gust']}")
        bar=w.barometric_pressure()
        print("BAROMETRIC PRESSURE")
        print(f"press - {bar['press']} hPa")
        print(f"sea level - {bar['sea_level']}  hPa")
        print("OTHER")
        print(f"visibility distance - {w.visibility_distance} km")
        print(f"sunrise time - {w.sunrise_time(timeformat='iso')} UTC")
        print(f"sunset time - {w.sunset_time(timeformat='iso')} UTC")
        print("")
