# ors_client.py
import os
from dotenv import load_dotenv
import openrouteservice
from openrouteservice import convert

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("ORS_API_KEY")

# Initialize client
client = None
if API_KEY:
    client = openrouteservice.Client(key=API_KEY)

def get_route(start, end):
    """
    Returns route info:
    - distance_km: float
    - duration_min: float
    - geometry_coords: list of (lon, lat)

    start and end should be dicts with 'lat' and 'lng' keys
    """
    if client is None:
        raise RuntimeError("ORS client not configured. Set ORS_API_KEY in .env")

    coords = ((start['lng'], start['lat']), (end['lng'], end['lat']))
    route = client.directions(coords)

    summary = route['routes'][0]['summary']
    geometry = route['routes'][0]['geometry']
    decoded = convert.decode_polyline(geometry)

    return {
        "distance_km": round(summary['distance'] / 1000.0, 2),
        "duration_min": round(summary['duration'] / 60.0, 2),
        "geometry_coords": decoded['coordinates']
    }
