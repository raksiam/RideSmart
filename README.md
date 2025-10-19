# RideSmart 🚖

RideSmart is a **user-friendly ride booking assistant** for India that helps users compare and select rides from Ola, Uber, and Rapido in one place. Users can choose exact pickup and drop locations using an interactive map.

---

## Features Implemented

1. **Autocomplete for addresses**

   * Source and Destination fields use geocoding to provide suggestions.

2. **Interactive Map Pin Selection**

   * Click on map to drop pin for exact pickup/drop location.
   * Draggable markers for fine-tuning.

3. **Simulated Ride Booking**

   * Shows ride options from Ola, Uber, Rapido with ETA & price.
   * Automatically selects the ride with the **shortest ETA** and “cancels” others.

4. **Free & Portfolio-Friendly**

   * Uses **Nominatim** (OpenStreetMap) for geocoding.
   * Uses **Folium** for maps and **Streamlit** for the frontend.

---

## Tech Stack

* Python 3.13
* Streamlit
* Folium
* Geopy (Nominatim)
* Pandas

---

## Step-by-Step Implementation

### Step 1: GitHub Repository

1. Created a GitHub repo called `RideSmart`.
2. Cloned it locally on Mac:

```bash
git clone https://github.com/raksiam/RideSmart.git
cd RideSmart
```

3. Created a feature branch:

```bash
git checkout -b feature/initial-app
```

---

### Step 2: Project Structure

1. Created main app file:

```bash
touch ridesmart_app.py
```

2. Created supporting files:

```bash
touch requirements.txt
```

```bash
touch README.md
```

---

### Step 3: Virtual Environment & Dependencies

1. Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

2. Installed dependencies:

```bash
pip install streamlit folium geopy pandas streamlit-folium
```

3. Saved dependencies:

```bash
pip freeze > requirements.txt
```

---

### Step 4: Streamlit App Implementation

1. Implemented autocomplete search for **source and destination** using `geopy.Nominatim`.
2. Implemented **click-to-drop map pins** using `folium` and `streamlit-folium`.
3. Added **simulated ride options** for Ola, Uber, Rapido with ETA and price.
4. Added **automatic selection** of the fastest ride and cancellation of others.

> Full code is in `ridesmart_app.py`

---

### Step 5: Run the App

```bash
streamlit run ridesmart_app.py
```

* Enter source & destination addresses
* Confirm exact pickup/drop location on map
* View simulated ride options and automatic selection

---

### Step 6: Commit Changes

```bash
git add .
git commit -m "Initial implementation of RideSmart app with autocomplete, map pin, and simulated rides"
git push origin feature/initial-app
```

> Note: We pushed to a **feature branch first** instead of main.

---

### Step 7: Next Steps / Improvements

* Integrate **Uber API** for real-time ride estimates.
* Make Ola & Rapido simulated rides dynamic (random price & ETA).
* Enhance UI for better user experience.
* Add screenshots and GIFs for map interaction and ride selection.

---

## Notes

* Fully free to use with no billing.
* Works on Mac, Windows, Linux.
