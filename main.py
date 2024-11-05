import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 13.081028
MY_LONG = 80.271004
MY_EMAIL = "myemail@gmail.com"
MY_PASSWORD = "*********"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is with +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data=response.json()
    sunrise_hour = int(data["results"]['sunrise'].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]['sunset'].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset_hour or time_now <= sunrise_hour:
        return True

while True:
    time.sleep(60)          #program run's every 60sec
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 465) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
            )