# Write a program that will determine weather when the value of temperature and humidity is provided by the user.
#               Temperature(c)                   Humidity(%)                    Weather
#                   >=30                            >=90                     Hot and humid
#                   >=30                            <90                      hot
#                   <30                             >=90                     cool and humid
#                   <30                             <90                      cool


def weather(t,h):
    if (t >= 30 and h >= 90):
        return "hot and humid"
    elif (t >=30 and h <90):
        return  "hot"
    elif (t < 30 and h >=90):
        return "cold and humid"
    else:
        return "cold"

print(weather(20,90))