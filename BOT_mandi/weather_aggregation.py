def aggregate_weather_data(records):
    # Dictionary to store city-wise aggregated data
    city_data = {}

    for record in records:
        city = record.get('city')
        temperature = record.get('temperature')
        humidity = record.get('humidity')

        if city not in city_data:
            city_data[city] = {'temperature_sum': 0, 'humidity_sum': 0, 'temp_count': 0, 'hum_count': 0}

        # Aggregate temperature if available
        if temperature is not None:
            city_data[city]['temperature_sum'] += temperature
            city_data[city]['temp_count'] += 1

        # Aggregate humidity if available
        if humidity is not None:
            city_data[city]['humidity_sum'] += humidity
            city_data[city]['hum_count'] += 1

    # Compute average temperature and humidity for each city
    result = {}
    for city, data in city_data.items():
        avg_temp = data['temperature_sum'] / data['temp_count'] if data['temp_count'] > 0 else None
        avg_humidity = data['humidity_sum'] / data['hum_count'] if data['hum_count'] > 0 else None
        result[city] = {'average_temperature': avg_temp, 'average_humidity': avg_humidity}

    return result

# Example usage:
records = [
    {'city': 'CityA', 'temperature': 20, 'humidity': 70},
    {'city': 'CityA', 'temperature': 22},  # Missing humidity
    {'city': 'CityB', 'temperature': 25, 'humidity': 60},
    {'city': 'CityB', 'humidity': 55},  # Missing temperature
]

print(aggregate_weather_data(records))
