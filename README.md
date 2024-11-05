# ISS Overhead Notifier

This Python program checks if the International Space Station (ISS) is overhead and if it is nighttime at a specified location. If both conditions are met, it sends an email notification to the user, prompting them to look up at the sky to view the ISS.

## Project Overview

The program performs the following tasks:
1. Checks if the ISS is currently overhead by comparing its latitude and longitude with the user's specified location.
2. Verifies if it is nighttime at the specified location by retrieving sunrise and sunset times from the [Sunrise Sunset API](https://sunrise-sunset.org/api).
3. Sends an email notification to the user if both conditions are met.

The program runs continuously, checking every 60 seconds.

## Prerequisites

- Python 3.x
- [requests](https://pypi.org/project/requests/) - for making HTTP requests
- [smtplib](https://docs.python.org/3/library/smtplib.html) - for sending emails
- An active email account (e.g., Gmail) for sending notifications

## Installation

1. Clone the repository or download the project files.
2. Install the required libraries using the following command:
   ```bash
   pip install requests
   ```

3. Edit the `MY_LAT`, `MY_LONG`, `MY_EMAIL`, and `MY_PASSWORD` variables with your latitude, longitude, email, and email password, respectively. Replace `myemail@gmail.com` with your actual email address.

## Usage

1. Run the program:
   ```bash
   python main.py
   ```
2. The program will check every minute to see if the ISS is overhead and it is nighttime.
3. If both conditions are met, an email will be sent to the specified address.

## Code Explanation

### Functions

- **is_iss_overhead**: Checks if the ISS is within ±5 degrees of the specified latitude and longitude.
- **is_night**: Determines if it is nighttime by comparing the current hour to sunset and sunrise times.
  
### Main Loop

The program uses an infinite loop with a 60-second delay between iterations. If both `is_iss_overhead` and `is_night` return `True`, an email is sent.

## Notes

- Ensure "Less secure app access" is enabled in your email settings if using Gmail, or use an [app-specific password](https://support.google.com/accounts/answer/185833?hl=en) for better security.
- Be cautious when storing passwords in plain text. You can use environment variables or a secure vault for better security.

## API References

- **ISS Position API**: [Open Notify ISS API](http://api.open-notify.org/iss-now.json)
- **Sunrise Sunset API**: [Sunrise Sunset API](https://sunrise-sunset.org/api)
