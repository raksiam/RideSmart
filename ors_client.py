# ors_client.py
import os
import openrouteservice
from openrouteservice import convert

# Try Streamlit secrets first
try:
    import streamlit as st
    API_KEY = st.secrets["ORS_API_KEY"]
except (ModuleNotFoundError, KeyError):
    # fallback to .env for local
    from dotenv import load_dotenv
    load_dotenv()
    API_KEY = os.getenv("ORS_API_KEY")

# Initialize client
client = None
if API_KEY:
    client = openrouteservice.Client(key=API_KEY)
else:
    client = None

def get_route(start_lon, start_lat, end_lon, end_lat):
    if client is None:
        raise RuntimeError("ORS client not configured. Set ORS_API_KEY in .env or Streamlit secrets.")

    coords = ((start_lon, start_lat), (end_lon, end_lat))
    route = client.directions(coords)

    summary = route['routes'][0]['summary']
    geometry = route['routes'][0]['geometry']
    decoded = convert.decode_polyline(geometry)

    return {
        "distance_km": summary['distance'] / 1000.0,
        "duration_min": summary['duration'] / 60.0,
        "geometry_coords": decoded['coordinates']
    }
