import streamlit as st
import json
import pandas as pd

@st.cache_data
def load_beach_data(json_file: str):
    """Load the beach data from a JSON file."""
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def filter_beaches(beaches, wheelchair_only: bool, tel_aviv_only: bool):
    """Filter beaches by wheelchair accessibility and city."""
    filtered = beaches
    if wheelchair_only:
        filtered = [b for b in filtered if b.get("wheelchair_accessible", False)]
    if tel_aviv_only:
        # This example considers both "Tel Aviv" and "Tel Aviv-Yafo" as Tel Aviv beaches.
        filtered = [b for b in filtered if "Tel Aviv" in b.get("city", "")]
    return filtered

# Load beach data from the JSON file (e.g., beaches.json)
data = load_beach_data("database/sample_db.json")

# Sidebar filters
st.sidebar.header("Filters")
wheelchair_filter = st.sidebar.checkbox("Only Wheelchair Accessible")
tel_aviv_filter = st.sidebar.checkbox("Only Tel Aviv Beaches")

# Apply filters – if none are selected, all beaches are shown
filtered_data = filter_beaches(data, wheelchair_filter, tel_aviv_filter)

# Convert the filtered data into a DataFrame for st.map
# st.map expects columns named "lat" and "lon"
df = pd.DataFrame([
    {
        "lat": beach["location"]["latitude"],
        "lon": beach["location"]["longitude"],
        "beach_name": beach["beach_name"],
        "city": beach["city"],
        "wheelchair_accessible": beach["wheelchair_accessible"]
    }
    for beach in filtered_data
])

# Main screen content
st.title("Beaches in Israel")
st.write(f"Displaying {len(df)} beaches.")

# Display the map with the filtered beaches
st.map(df)

# Optionally, list detailed information for each beach below the map.
st.header("Beach Details")
for beach in filtered_data:
    st.subheader(beach["beach_name"])
    st.write(f"City: {beach['city']}")
    st.write(f"Wheelchair Accessible: {beach['wheelchair_accessible']}")
    st.write("---")
