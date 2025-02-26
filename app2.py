import streamlit as st
import json
import pandas as pd

# Sidebar navigation: choose between pages.
page = st.sidebar.radio("Navigation", ["Main", "Info about Itai"])


# Common function: Load beach data using the new st.cache_data decorator.
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


if page == "Main":
    # Custom header with an icon and a title ("sea" and "me" in two lines) at the top left.
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("icons/seame_icon.png", width=150)
    with col2:
        st.markdown("<h1 style='margin: 0; line-height: 1.2;'>sea<br>me</h1>", unsafe_allow_html=True)

    # Load the beach data (assuming beaches.json is in the same directory).
    data = load_beach_data("database/sample_db.json")

    # Sidebar filters for the main page.
    st.sidebar.header("Filters")
    wheelchair_filter = st.sidebar.checkbox("Only Wheelchair Accessible")
    tel_aviv_filter = st.sidebar.checkbox("Only Tel Aviv Beaches")

    # Apply filters. If none are selected, all beaches are shown.
    filtered_data = filter_beaches(data, wheelchair_filter, tel_aviv_filter)

    # Convert the filtered data into a DataFrame for st.map.
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

    # Main content: Title, map, and beach details.
    st.title("Beaches in Israel")
    st.write(f"Displaying {len(df)} beaches.")
    st.map(df)

    st.header("Beach Details")
    for beach in filtered_data:
        st.subheader(beach["beach_name"])
        st.write(f"City: {beach['city']}")
        st.write(f"Wheelchair Accessible: {beach['wheelchair_accessible']}")
        st.write("---")

elif page == "Info about Itai":
    # Info about Itai page.

    st.markdown(
        """
        <div style="text-align: right;">
            <h1>איתי פרי ז"ל</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    # Create two columns with an empty left column and a right column for the content.
    empty_col, right_col = st.columns([1, 3])
    with right_col:
        st.image("icons/itayperi_autoOrient_g.jpg", width=300)

    st.write(
        """
        <div style="direction: rtl; text-align: right;">
            <strong>סיפור חייו</strong>
            <br><br>
            איתי פרי נולד ב-29 באוגוסט 1987 בתל אביב, בנו של אהובה ונתן ואח לנטע, עומרי ונועה. 
            נישא להילה והוליד שלושה ילדים: עידו, גיל ואורי.
            <br><br>
            ביום 7.10.2023 התגייס למילואים ושירת בחיל רגלים.
            <br><br>
            רב סמל מתקדם איתי פרי נפל בקרב ביום כ"ז בכסלו תשפ"ד (10.12.2023). בן שלושים ושש בנופלו. 
            <br><br>
            הוא הובא למנוחות בחלקה הצבאית בבית העלמין במודיעין. הותיר אחריו אישה, שלושה ילדים, הורים ואחים.
        </div>
        """,
        unsafe_allow_html=True
    )
    # st.write("Use the navigation on the sidebar to go back to the main page.")
