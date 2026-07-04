# Rain Alert

A Python weather alert project that checks the upcoming forecast and sends an email notification if rain is expected.

This project was built using Python, requests, OpenWeather API, SMTP email automation, and environment variables for safer credential handling.

---

## Features

- Fetches weather forecast data from the OpenWeather API
- Uses latitude and longitude coordinates to check local weather
- Checks the upcoming forecast in 3-hour intervals
- Detects rain or bad weather conditions using weather condition IDs
- Uses a boolean flag to track if rain is expected
- Sends an email alert when rain is forecasted
- Uses environment variables to keep API keys, email, and password out of the code
- Handles HTTP errors with `response.raise_for_status()`

---

## What I practiced

- Working with APIs using `requests`
- Passing parameters to an API request with `params`
- Reading JSON data returned from an API
- Navigating nested dictionaries and lists
- Using `for` loops to check multiple forecast entries
- Using boolean flags like `will_rain`
- Sending emails with `smtplib`
- Using `starttls()` for secure email connection
- Loading secret values from environment variables
- Avoiding hardcoded passwords and API keys in public code

---

## Project structure

```
main.py
```

---

## How to run

Run the project with:

```bash
python main.py
```

Before running the project, set the required environment variables:

```bash
OPENWEATHER_API_KEY=your_openweather_api_key
MY_EMAIL=your_email
MY_EMAIL_PASSWORD=your_email_app_password
```

---

## Technologies used

- Python
- Requests
- OpenWeather API
- SMTP
- Gmail App Password
- Environment Variables

---

## Note

This project was created as part of my Python learning journey through Angela Yu’s Udemy course.

---

## Author

Alex — Aspiring Python developer building projects step by step through daily practice, with the long-term goal of becoming a professional software developer.