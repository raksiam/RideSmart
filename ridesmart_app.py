import streamlit as st
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from streamlit_folium import st_folium
import folium
import pandas as pd
import time

st.set_page_config(page_title="RideSmart", layout="centered")
st.title("🚖 RideSmart: Autocomplete + Map Pin + Ride Simulation")

# Initialize Nominatim geocoder
geolocator = Nominatim(user_agent="ridesmart_app", timeout=10)

# Retry geocoding function
def geocode_with_retry(address, retries=3):
    for i in range(retries):
        try:
            return geolocator.geocode(address, exactly_one=False, limit=5)
        except GeocoderTimedOut:
            if i < retries - 1:
                time.sleep(1)
                continue
            else:
                return None

# ------------------ SOURCE ------------------
st.subheader("Step 1: Enter Source Address")
source_input = st.text_input("Source Address:")

if source_input:
    results = geocode_with_retry(source_input)
    if results:
        options = [r.address for r in results]
        selected_source = st.selectbox("Select Source from suggestions", options)
        st.write("You selected:", selected_source)

        source_loc = geolocator.geocode(selected_source)
        lat, lng = source_loc.latitude, source_loc.longitude

        # Map for click-to-drop pin
        st.subheader("Confirm Source Pin (Click on map to drop pin)")
        m_source = folium.Map(location=[lat, lng], zoom_start=15)
        source_map = st_folium(m_source, width=700, height=400, returned_objects=["last_clicked"])

        if source_map['last_clicked']:
            final_source = source_map['last_clicked']
            # Show marker at clicked location
            m_source = folium.Map(location=[final_source['lat'], final_source['lng']], zoom_start=15)
            folium.Marker([final_source['lat'], final_source['lng']], tooltip="Source Pin", draggable=True).add_to(m_source)
            st_folium(m_source, width=700, height=400)
            st.write("Confirmed Source Pin:", final_source)
        else:
            final_source = {'lat': lat, 'lng': lng}
    else:
        st.write("No results found for source.")
        final_source = None
else:
    final_source = None

# ------------------ DESTINATION ------------------
st.subheader("Step 2: Enter Destination Address")
dest_input = st.text_input("Destination Address:")

if dest_input:
    results = geocode_with_retry(dest_input)
    if results:
        options = [r.address for r in results]
        selected_dest = st.selectbox("Select Destination from suggestions", options)
        st.write("You selected:", selected_dest)

        dest_loc = geolocator.geocode(selected_dest)
        lat, lng = dest_loc.latitude, dest_loc.longitude

        # Map for click-to-drop pin
        st.subheader("Confirm Destination Pin (Click on map to drop pin)")
        m_dest = folium.Map(location=[lat, lng], zoom_start=15)
        dest_map = st_folium(m_dest, width=700, height=400, returned_objects=["last_clicked"])

        if dest_map['last_clicked']:
            final_dest = dest_map['last_clicked']
            # Show marker at clicked location
            m_dest = folium.Map(location=[final_dest['lat'], final_dest['lng']], zoom_start=15)
            folium.Marker([final_dest['lat'], final_dest['lng']], tooltip="Destination Pin", draggable=True).add_to(m_dest)
            st_folium(m_dest, width=700, height=400)
            st.write("Confirmed Destination Pin:", final_dest)
        else:
            final_dest = {'lat': lat, 'lng': lng}
    else:
        st.write("No results found for destination.")
        final_dest = None
else:
    final_dest = None

# ------------------ SIMULATED RIDE OPTIONS ------------------
if final_source and final_dest:
    st.subheader("Available Rides (Simulated)")
    
    # Simulated rides: price & ETA
    data = {
        "App": ["Ola", "Uber", "Rapido"],
        "Price (₹)": [150, 140, 130],
        "ETA (min)": [5, 3, 7]
    }
    df = pd.DataFrame(data)
    st.table(df)

    # Best ride selection
    best_ride = df.loc[df['ETA (min)'].idxmin()]
    st.success(f"🚀 Best ride selected: {best_ride['App']} (ETA: {best_ride['ETA (min)']} min, ₹{best_ride['Price (₹)']})")

    # Simulate canceling other rides
    canceled_rides = df[df['App'] != best_ride['App']]['App'].tolist()
    if canceled_rides:
        st.info(f"❌ Canceled rides: {', '.join(canceled_rides)}")
