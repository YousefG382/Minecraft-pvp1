import streamlit as st
import pandas as pd
import altair as alt

# Page config
st.set_page_config(page_title="Minecraft PvP Strategy Simulator", layout="centered")
st.title("🗡️ Minecraft PvP Strategy Simulator")

# --- Dropdowns and Sliders ---
health = st.selectbox("Player Health", ["High", "Low"])
cps = st.selectbox("CPS (Clicks per Second)", ["High (15-20)", "Low (5-10)"])
gamesense = st.selectbox("Game Sense", ["High", "Medium", "Low"])
playstyle = st.selectbox("Playstyle", ["Aggressive", "Defensive", "Balanced"])
tactic = st.selectbox("Tactic Used", ["Web", "Short Pearl", "Medium Pearl", "Long Pearl", "Totem", "Gap"])

# --- Strategy Evaluation Logic ---
def evaluate_strategy(health, cps, gamesense, playstyle, tactic):
    # Initial base score
    score = 50

    # Modify score based on tactic interactions
    if tactic == "Web":
        if playstyle == "Aggressive":
            score += 20
        if cps == "High (15-20)" and gamesense == "High":
            score -= 30
        if tactic == "Web" and health == "Low":
            score -= 10

    elif tactic == "Short Pearl":
        score += 15
        if playstyle == "Aggressive":
            score += 10
        if gamesense == "Low":
            score += 5

    elif tactic == "Medium Pearl":
        if cps == "Low (5-10)":
            score += 10
        if gamesense == "High" and cps == "High (15-20)":
            score -= 25

    elif tactic == "Long Pearl":
        if gamesense == "High" and cps == "High (15-20)":
            score -= 20
        elif health == "High":
            score += 10
        else:
            score -= 10

    elif tactic == "Totem":
        score += 5

    elif tactic == "Gap":
        if tactic == "Gap" and playstyle == "Aggressive":
            score += 10

    # Modify score by playstyle matchups
    if playstyle == "Aggressive" and cps == "High (15-20)" and gamesense == "Low":
        score += 5
    if playstyle == "Defensive" and cps == "Low (5-10)" and gamesense == "High":
        score += 15
    if playstyle == "Balanced":
        score += 5

    # Clamp score between 0 and 100
    score = max(0, min(score, 100))
    return score

# --- Output ---
success_rate = evaluate_strategy(health, cps, gamesense, playstyle, tactic)
st.metric(label="Success Rate", value=f"{success_rate} %")

# Optional: Show result as bar chart
chart_data = pd.DataFrame({
    'Strategy': ['Your Setup'],
    'Success Rate': [success_rate]
})

st.altair_chart(
    alt.Chart(chart_data).mark_bar().encode(
        x='Strategy',
        y='Success Rate',
        color=alt.value('steelblue')
    ).properties(width=400, height=300),
    use_container_width=True
)
