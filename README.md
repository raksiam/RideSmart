# RideSmart 🚖

RideSmart is a Streamlit-based app that simulates ride-hailing services (Ola, Uber, Rapido) with live distance & duration calculation using OpenRouteService (ORS) API. Users can input addresses, confirm pickup/drop pins on the map, and view ride options with estimated price and ETA.

---

## Features

- Autocomplete address search with suggestions
- Map pin selection for exact pickup and drop points
- Automatic distance & duration calculation via ORS API
- Simulated ride options with best ride highlighted
- Configurable ride rates per km and per minute
- Friendly UI via Streamlit & Folium

---

## Setup & Installation

### 1. Clone the Repository
git clone https://github.com/raksiam/RideSmart.git
cd RideSmart

### 2. Create & Activate Virtual Environment
python -m venv venv

- Linux/macOS:
  source venv/bin/activate
- Windows:
  venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Configure ORS API Key
1. Create a `.env` file in the project root.
2. Add your ORS API key:

ORS_API_KEY=your_openrouteservice_api_key

> You can get a free ORS API key from https://openrouteservice.org/sign-up/

---

## Usage

1. Run the Streamlit app:
streamlit run ridesmart.py

2. In the web app:
- Enter the **Source Address** and select from suggestions.
- Drop a pin on the map to confirm pickup location.
- Enter the **Destination Address** and select from suggestions.
- Drop a pin on the map to confirm drop location.
- View calculated rides (Ola, Uber, Rapido) with ETA and price.
- The best ride (shortest ETA) will be highlighted and others marked as canceled.

---

## Project Structure

- `ridesmart.py` - Main Streamlit app.
- `ors_client.py` - ORS API client to calculate distance & duration.
- `ride_values.py` - Configurable ride rates per app (per km & per min).
- `.env` - Environment file for API keys.
- `requirements.txt` - Python dependencies.

---

## Development Workflow

1. Create a feature branch:
git checkout -b feature/branch-name

2. Make changes and commit:
git add .
git commit -m "Describe your changes"

3. Push to GitHub:
git push origin feature/branch-name

4. Create a Pull Request (PR) to merge changes into `main`.

---

## Notes

- Ensure the ORS API key is valid and `.env` is properly configured.
- All distances and durations are automatically calculated; manual input is not required.
- Ride prices are computed as: `price = per_km * distance + per_min * duration` (values configurable in `ride_values.py`).

---

## License

MIT License
