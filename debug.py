# import lauzhack.lauzhack.journey_selector as journey_selector
import lauzhack.lauzhack.views as views

# a = journey_selector.compute_all_additional_bike_travels(6.5601536,46.514176, 6.211753,46.401823, 1000, {"id": "8503000", "name": "Lausanne", "coordinates": [6.632273, 46.519653], "time": "2023-04-18T15:11:00+02:00"}, "1000", "1000", "2023-04-18", 1701566527)
# print(a)

a = views.find_trips_complete(None, "[6.5601536,46.514176]", "[6.211753,46.401823]", 1000, 1000, 1701566527, True, True, True)
print(a)

