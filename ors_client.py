# ors_client.py
import os
from dotenv import load_dotenv
import openrouteservice
from openrouteservice import convert
import streamlit as st

# Load .env for local development
load_dotenv()

# First try to get from Streamlit secrets, then fallback to environment variable
try:
    API_KEY = st.secrets["ORS_API_KEY"]
except Exception:
    API_KEY = os.getenv("ORS_API_KEY")

# Initialize client
client = None
if API_KEY:
    client = openrouteservice.Client(key=API_KEY)

def get_route(start, end):
    """
    start: dict with 'lat' and 'lng'
    end: dict with 'lat' and 'lng'
    Returns:
        distance_km, duration_min, geometry_coords
    """
    if client is None:
        raise RuntimeError("ORS client not configured. Set ORS_API_KEY in .env or Streamlit secrets.")

    coords = ((start['lng'], start['lat']), (end['lng'], end['lat']))
    route = client.directions(coords)

    summary = route['routes'][0]['summary']
    geometry = route['routes'][0]['geometry']
    decoded = convert.decode_polyline(geometry)

    return {
        "distance_km": summary['distance'] / 1000.0,
        "duration_min": summary['duration'] / 60.0,
        "geometry_coords": decoded['coordinates']
    }
