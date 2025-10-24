# ------------------ Fare Configuration for RideSmart ------------------

# Base fare rates for each app (average / approximate values for multiple cities in India)
FARE_RATES = {
    "Ola": {"base_fare": 50, "per_km": 10, "per_min": 1},
    "Uber": {"base_fare": 55, "per_km": 9, "per_min": 1},
    "Rapido": {"base_fare": 40, "per_km": 8, "per_min": 1}
}

# Optional surge multipliers
SURGE_MULTIPLIERS = {
    "Ola": 1.0,
    "Uber": 1.0,
    "Rapido": 1.0
}

def calculate_fare(app_name, distance_km, duration_min):
    """
    Calculate ride fare for a given app based on distance (km) and duration (min)
    Returns: (fare, surge_multiplier)
    """
    base = FARE_RATES[app_name]["base_fare"]
    per_km = FARE_RATES[app_name]["per_km"]
    per_min = FARE_RATES[app_name]["per_min"]
    surge = SURGE_MULTIPLIERS.get(app_name, 1.0)

    fare = (base + (per_km * distance_km) + (per_min * duration_min)) * surge
    fare = round(fare, 0)  # round to nearest rupee
    return fare, surge
