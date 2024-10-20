# Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates

This is a Django-based weather monitoring system that retrieves real-time weather data from the OpenWeatherMap API for various cities.
The system stores data in a database, processes it into daily rollups and aggregates (such as average temperature, humidity, wind speed, etc.),
and visualizes the results using Chart.js. Additionally, the system can trigger alerts when specific weather thresholds are breached (e.g., high temperature )

# Features

- Fetch real-time weather data from the OpenWeatherMap API for multiple cities.
- Support for multiple weather parameters: temperature, humidity, wind speed, and weather conditions.
- Calculate daily rollups and aggregates for cities (average, max, and min temperature, humidity, and wind speed).
- Visualize weather trends using Chart.js (line charts).
- Trigger alerts for extreme weather conditions (e.g., high temperature, humidity, or wind speed).
- Extendable design to support additional weather parameters.

# Requirements

- Python 3.8 or higher
- Django 5.1.2
- requests library for fetching data from OpenWeatherMap API
- Chart.js for front-end visualizations (included via CDN)

# Installation
1. Clone the Repository
   https://github.com/crossboww/Weather_Monitoring.git
   cd weather_monitoring_system
   
2. Create a Virtual Environment
   python -m venv env
   env\Scripts\activate     # For Windows
   
3. Install Dependencies
   pip install django
   pip install requests pytz

4. Set Up Django Project
   python manage.py makemigrations
   python manage.py migrate

5. Configure OpenWeatherMap API Key
   OPENWEATHERMAP_API_KEY = 'your_openweathermap_api_key'

6. Run the Development Server
   python manage.py runserver

7. Open in Browser
   Go to http://127.0.0.1:8000/weather/weather-summary/ to view the weather summaries and trends.

1. To Run Project
python manage.py runserver

2. For fetch the Weather Summary data
   http://127.0.0.1:8000/weather/fetch-weather/

3. To check the weather summary and rollup and aggregate weather data in database
   http://127.0.0.1:8000/admin/

   username : krish2311
   password : kiddo@2311

   Now you can see the weather summary in database

4. to see Weather_summary and trends and alert
   http://127.0.0.1:8000/weather/weather-summary/

   Now you can see the weather Summary in Table and chart visulization on web page

# Usage 

1. Fetching Weather Data
  - The system fetches weather data for predefined cities by using a management command.
  - You can run the fetch command manually or automate it using cron jobs or Windows Task Scheduler.

# Run the management command:
  python manage.py fetch_weather --unit=Celsius

2. Daily Aggregates
   The system calculates daily rollups and aggregates for cities, including:
   
   - Average temperature
   - Maximum temperature
   - Minimum temperature
   - Average humidity
   - Maximum wind speed
     
4. Threshold-Based Alerts
   Alerts are triggered when predefined thresholds are breached, such as:

  - High temperature (e.g., > 35°C)
  - High humidity (e.g., > 80%)
  - Strong wind speed (e.g., > 15 m/s)
    
5. Visualizations
   Visualize daily trends for temperature, humidity, and wind speed using 
   Chart.js.
   Visit the /weather/weather-summary/ page to see the trends.

# Configuration

1. API Key
Make sure to configure your OpenWeatherMap API key in the settings.py file:
OPENWEATHERMAP_API_KEY = 'your_openweathermap_api_key'

2. Cities to Monitor
   You can add or modify the cities you want to monitor by updating the   
   fetch_weather_data() function in the management/commands/fetch_weather.py 
   file.
   CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']


# Technologies Used
  Django: The web framework used for building the backend.
  OpenWeatherMap API: The external API for retrieving real-time weather data.
  Chart.js: A JavaScript library used for creating dynamic charts for visualizing weather trends.
  SQLite: The database used for storing weather summaries.

# Contact:

Your Name: Krish Kondabatni
email: krishkonda89@gmail.com
GitHub: https://github.com/crossboww


   





