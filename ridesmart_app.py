# ridesmart_app.py
import streamlit as st
from ridesmart import select_location, show_ride_options

# Step 1: Source
source = select_location("Source")

# Step 2: Destination
destination = select_location("Destination")

# Step 3: Show rides
show_ride_options(source, destination)
