import streamlit as st
import pandas as pd
import time
from datetime import datetime
import plotly.express as px

# PAGE CONFIG
st.set_page_config(
    page_title="Smart Study Focus Tracker",
    page_icon="📚",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3 {
    color: #00F5FF;
}

div.stButton > button {
    background: linear-gradient(
        90deg,
        #00F5FF,
        #0066FF
    );

    color: white;

    border-radius: 12px;

    height: 3em;

    font-size: 20px;

    border: none;

    width: 100%;
}

section[data-testid="stSidebar"] {
    background-color: #161B22;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("📊 Dashboard")

st.sidebar.info("""
Smart productivity tracker for students.

Built using:
- Python
- Streamlit
- AI Analytics
- Data Visualization
""")

# TITLE
st.title("📚 Smart Study Focus Tracker")

st.markdown("""
### 🚀 AI-Powered Productivity Monitoring System

Track:
- Active Applications
- Focus Level
- Distractions
- Productivity Trends
- Smart Analytics
""")

# TIMER
st.sidebar.subheader("⏳ Study Timer")

study_time = st.sidebar.slider(
    "Select Study Minutes",
    1,
    60,
    1
)

# FUNCTION


# BUTTON
if st.button("🚀 Start Study Session"):

    records = []

    st.info("Tracking Started...")

    progress = st.progress(0)

    total_seconds = study_time * 60
    
    timer_placeholder = st.empty()

    for i in range(total_seconds):

       active_app = st.selectbox(
    "Select Current Activity",
    [
        "Studying",
        "Coding",
        "Reading PDF",
        "YouTube",
        "Instagram",
        "Netflix"
    ],
    key=f"activity_{i}"
)

current_time = datetime.now()
records.append({
            "Time": current_time,
            "Active App": active_app
        })

mins, secs = divmod(
            total_seconds - i,
            60
        )

timer_placeholder.info(
            f"⏳ Time Left: {mins:02d}:{secs:02d}"
        )

progress.progress(
            (i + 1) / total_seconds
        )

time.sleep(1)

    # DATAFRAME
df = pd.DataFrame(records)

    # SAVE CSV
df.to_csv(
        "study_data.csv",
        index=False
    )

    # ANALYSIS
focus_count = 0
distraction_count = 0

categories = []

for app in df["Active App"]:

        app_lower = str(app).lower()

        if (
            "youtube" in app_lower or
            "instagram" in app_lower or
            "netflix" in app_lower
        ):

            categories.append(
                "Distracting"
            )

            distraction_count += 1

        else:

            categories.append(
                "Productive"
            )

            focus_count += 1

df["Category"] = categories

    # SCORES
focus_score = (
        focus_count / len(df)
    ) * 100

distraction_score = (
        distraction_count / len(df)
    ) * 100

    # TOP DISTRACTING APP
distracting_apps = df[
        df["Category"] == "Distracting"
    ]

if not distracting_apps.empty:

        top_distracting = distracting_apps[
            "Active App"
        ].value_counts().idxmax()

else:

        top_distracting = "None"

st.success(
        "✅ Session Completed"
    )

    # METRICS
col1, col2, col3 = st.columns(3)

with col1:

        st.metric(
            "🎯 Focus Score",
            f"{focus_score:.2f}%"
        )

with col2:

        st.metric(
            "⚠️ Distraction Score",
            f"{distraction_score:.2f}%"
        )
with col3:

        st.metric(
            "📱 Apps Tracked",
            len(df)
        )

    # PRODUCTIVITY STATUS
if focus_score >= 80:

        st.success(
            "🔥 HIGH PRODUCTIVITY SESSION"
        )

elif focus_score >= 50:

        st.warning(
            "⚡ MODERATE PRODUCTIVITY SESSION"
        )

else:

        st.error(
            "🚨 LOW PRODUCTIVITY SESSION"
        )

    # DISTRACTING APP
st.info(
        f"📌 Most Distracting App: {top_distracting}"
    )

    # AI SUGGESTIONS
st.subheader(
        "🤖 AI Suggestions"
    )

if distraction_score > 50:

        st.error(
            "Too many distractions detected. Avoid social media while studying."
        )

elif focus_score > 70:

        st.success(
            "Excellent productivity session. Keep it up!"
        )

else:

        st.warning(
            "Average productivity detected. Improve focus."
        )

    # PIE CHART
st.subheader(
        "📊 Productivity Distribution"
    )

pie = px.pie(
        df,
        names="Category"
    )

pie.update_traces(
        textinfo="percent+label"
    )

pie.update_layout(
        height=500
    )

st.plotly_chart(
        pie,
        use_container_width=True
    )

    # SESSION DATA
st.subheader(
        "📄 Session Data"
    )

st.dataframe(df)

    # BAR CHART
st.subheader(
        "📊 Application Usage"
    )

chart_data = df[
        "Active App"
    ].value_counts()

st.bar_chart(
        chart_data,
        height=400
    )