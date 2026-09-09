import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
import requests

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="The Food Titanic",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp{
background:#061322;
color:white;
}

section[data-testid="stSidebar"]{
background:#081B2E;
}

html {
scroll-behavior:smooth;
}

.hero-title{
font-size:80px;
font-weight:900;
text-align:center;
color:white;
margin-top:150px;
}

.hero-sub{
font-size:24px;
text-align:center;
color:#b9d8ff;
}

.chapter{
min-height:100vh;
padding-top:80px;
padding-bottom:80px;
}

.glass{
background:rgba(255,255,255,0.08);
backdrop-filter:blur(14px);
border-radius:24px;
padding:30px;
margin-bottom:25px;
}

.story{
font-size:22px;
line-height:1.8;
}

.highlight{
color:#55d4ff;
font-weight:700;
}

.ship-card{
border-radius:25px;
padding:20px;
background:rgba(255,255,255,0.08);
text-align:center;
}

.parallax{
background-image:url('https://images.unsplash.com/photo-1500375592092-40eb2168fd21');
height:100vh;
background-attachment:fixed;
background-position:center;
background-repeat:no-repeat;
background-size:cover;
}

.metric-title{
text-align:center;
font-weight:700;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HELPERS
# --------------------------------------------------

def load_lottie(url):
    try:
        r = requests.get(url)
        return r.json()
    except:
        return None

ship_lottie = load_lottie(
    "https://assets6.lottiefiles.com/packages/lf20_xsdj3tt9.json"
)

wave_lottie = load_lottie(
    "https://assets2.lottiefiles.com/packages/lf20_fcfjwiyb.json"
)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

chapters = [
    "1. Warning",
    "2. Five Ships",
    "3. Nutrition Report Card",
    "4. RMS",
    "5. Radar Room",
    "6. Segmentation",
    "7. World",
    "8. Iceberg Reveal",
    "9. Conclusion"
]

selected = st.sidebar.radio(
    "Story Navigator",
    chapters
)

progress = (chapters.index(selected)+1)/len(chapters)
st.sidebar.progress(progress)

sound = st.sidebar.toggle(
    "🌊 Ocean Ambience",
    value=False
)

if sound:
    st.audio("ocean.mp3")

# --------------------------------------------------
# HERO
# --------------------------------------------------

st.markdown("""
<div class="parallax">
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='hero-title'>
🚢 THE FOOD TITANIC
</div>

<div class='hero-sub'>
Can We Spot The Iceberg Before Impact?
</div>
""", unsafe_allow_html=True)

if ship_lottie:
    st_lottie(ship_lottie, height=350)

st.markdown("""
<div class='glass story'>

When Titanic hit the iceberg,
the disaster did not begin at impact.

It began the moment warning signs were ignored.

<br>

Countries face food crises in exactly the same way.

<b>Who is sailing toward the iceberg?</b>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# DATA
# --------------------------------------------------

ships = pd.DataFrame({
    "Country":[
        "Resilient Republic",
        "Hidden Vulnerability",
        "Recoveria",
        "Persistent Crisis",
        "Critical Alert"
    ],
    "NRS":[22,28,72,80,92],
    "RMS":[-3,4,-5,0,8],
    "Segment":[
        "Resilient",
        "Hidden Vulnerability",
        "Recovering",
        "Persistent Crisis",
        "Critical Alert"
    ]
})

# --------------------------------------------------
# FIVE SHIPS
# --------------------------------------------------

st.header("🚢 Meet The Five Ships")

cols = st.columns(5)

captain_images = [
    "captains/resilient.png",
    "captains/vulnerability.png",
    "captains/recoveria.png",
    "captains/persistent.png",
    "captains/critical.png"
]

for idx,col in enumerate(cols):

    with col:

        try:
            st.image(captain_images[idx])
        except:
            pass

        st.markdown(
            f"""
            <div class='ship-card'>
            <h4>{ships.iloc[idx]['Country']}</h4>
            <p>{ships.iloc[idx]['Segment']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# --------------------------------------------------
# NRS
# --------------------------------------------------

st.header("📋 Nutrition Risk Score")

metrics = {
    "Food Security":78,
    "Affordability":66,
    "Food Variety":71,
    "Nutrition Quality":64
}

metric_cols = st.columns(4)

for col,(label,value) in zip(metric_cols, metrics.items()):

    with col:

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=value,
            gauge={
                "axis":{"range":[0,100]}
            }
        ))

        fig.update_layout(
            height=250,
            paper_bgcolor="#061322"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown(
            f"<div class='metric-title'>{label}</div>",
            unsafe_allow_html=True
        )

st.success(
    "Nutrition Risk Score (NRS): 0 = Healthy Waters | 100 = Dangerous Waters"
)

# --------------------------------------------------
# RMS TREND
# --------------------------------------------------

st.header("📈 Risk Momentum Score")

trend = pd.DataFrame({
    "Year":[2020,2021,2022,2023,2024],
    "NRS":[30,33,38,45,52]
})

fig = px.line(
    trend,
    x="Year",
    y="NRS",
    markers=True
)

fig.update_layout(
    paper_bgcolor="#061322",
    plot_bgcolor="#061322"
)

st.plotly_chart(fig,use_container_width=True)

st.info(
    "NRS tells us where a country is. RMS tells us where it is heading."
)

# --------------------------------------------------
# ANIMATED SHIP MOVEMENT
# --------------------------------------------------

st.header("🚢 Journey Through Risk Waters")

animation_df = pd.DataFrame({

    "Year":[2020,2021,2022,2023,2024],

    "RMS":[-4,-2,0,2,5],

    "NRS":[25,30,40,48,58]

})

fig = px.scatter(
    animation_df,
    x="RMS",
    y="NRS",
    animation_frame="Year",
    range_x=[-10,10],
    range_y=[0,100],
    size_max=50
)

fig.update_traces(
    marker=dict(size=35)
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# RADAR ROOM
# --------------------------------------------------

st.header("📡 Captain's Radar Room")

theta = np.linspace(
    0,
    2*np.pi,
    200
)

r = np.abs(
    np.sin(theta*5)
)

radar = go.Figure()

radar.add_trace(
    go.Scatterpolar(
        r=r,
        theta=np.degrees(theta),
        fill="toself"
    )
)

radar.update_layout(
    paper_bgcolor="black",
    polar=dict(
        bgcolor="black"
    )
)

st.plotly_chart(
    radar,
    use_container_width=True
)

# --------------------------------------------------
# CALCULATOR
# --------------------------------------------------

st.header("🧮 Interactive NRS/RMS Calculator")

nrs = st.slider(
    "Nutrition Risk Score",
    0,100,45
)

rms = st.slider(
    "Risk Momentum Score",
    -10,10,3
)

if nrs < 50 and rms <= 0:
    segment = "Resilient"
elif nrs < 50 and rms > 0:
    segment = "Hidden Vulnerability"
elif nrs >=50 and rms <0:
    segment = "Recovering"
elif nrs >=50 and rms ==0:
    segment = "Persistent Crisis"
else:
    segment = "Critical Alert"

st.metric(
    "Segment",
    segment
)

# --------------------------------------------------
# SEGMENTATION MATRIX
# --------------------------------------------------

st.header("🧭 Food Security Matrix")

fig = px.scatter(
    ships,
    x="RMS",
    y="NRS",
    color="Segment",
    text="Country",
    size=[35]*5
)

fig.add_hline(y=50)

fig.add_vline(x=0)

fig.update_layout(
    height=700,
    paper_bgcolor="#061322",
    plot_bgcolor="#061322"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# ICEBERG INDEX
# --------------------------------------------------

st.header("❄️ Iceberg Early Warning Index")

index_value = min(
    100,
    max(
        0,
        nrs + rms*5
    )
)

gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=index_value,
    title={"text":"Iceberg Index"},
    gauge={
        "axis":{"range":[0,100]},
        "steps":[
            {"range":[0,40],"color":"green"},
            {"range":[40,70],"color":"gold"},
            {"range":[70,100],"color":"red"}
        ]
    }
))

gauge.update_layout(
    paper_bgcolor="#061322",
    height=450
)

st.plotly_chart(
    gauge,
    use_container_width=True
)

# --------------------------------------------------
# GLOBE
# --------------------------------------------------

st.header("🌍 Global Navigation View")

components.html(
"""
<div id="globeViz"></div>

//unpkg.com/globe.glscript>

<script>

const world = Globe()
(document.getElementById('globeViz'))

.globeImageUrl(
'//unpkg.com/three-globe/example/img/earth-dark.jpg'
)

.backgroundImageUrl(
'//unpkg.com/three-globe/example/img/night-sky.png'
)

.width(1200)
.height(700);

world.controls().autoRotate = true;
world.controls().autoRotateSpeed = 0.8;

</script>
""",
height=720
)

# --------------------------------------------------
# ICEBERG REVEAL
# --------------------------------------------------

st.header("🧊 Reveal The Threat")

if st.button("Reveal Iceberg"):

    st.image(
        "iceberg.png",
        use_container_width=True
    )

    st.error(
        "Hidden Vulnerability and Critical Alert countries require immediate attention."
    )

# --------------------------------------------------
# ENDING
# --------------------------------------------------

st.header("🎬 Final Message")

if wave_lottie:
    st_lottie(
        wave_lottie,
        height=250
    )

st.markdown("""
# Traditional Reporting

Tell us who hit the iceberg.

---

# Our Framework

Tell us who is heading toward one.

---

### Most food security dashboards tell us where countries are.

### This framework tells us where they are going.

---

## The goal is not to count lifeboats after impact.

## The goal is to spot the iceberg while there is still time to turn.
""")
