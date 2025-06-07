import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Minecraft PvP Strategy Simulator", layout="centered") st.title("🗡️ Minecraft PvP Strategy Simulator")

--- Dropdowns and Sliders ---

health = st.selectbox("Player Health", ["High", "Low"]) cps = st.selectbox("CPS (Clicks per Second)", ["High (15-20)", "Low (5-10)"]) gamesense = st.selectbox("Game Sense", ["High", "Medium", "Low"]) playstyle = st.selectbox("Playstyle", ["Aggressive", "Defensive", "Balanced"]) tactic = st.selectbox("Tactic Used", ["Web", "Short Pearl", "Medium Pearl", "Long Pearl", "Totem", "Gap"])

--- Simulated Rules Based on User Input ---

def calculate_success_rate(health, cps, gamesense, playstyle, tactic): # Initialize a base rate rate = 50

if tactic == "Web":
    if playstyle == "Aggressive":
        rate += 20
    if cps.startswith("High") and gamesense == "High":
        rate -= 30

elif tactic == "Long Pearl":
    if health == "High":
        if cps.startswith("High") and gamesense == "High":
            rate = 30
        else:
            rate = 70
    else:
        if cps.startswith("High") and gamesense == "High":
            rate = 20
        else:
            rate = 40

elif tactic == "Medium Pearl":
    if health == "High":
        if gamesense == "High" and cps.startswith("High"):
            rate = 30
        else:
            rate = 75
    else:
        if gamesense == "High":
            rate = 25
        else:
            rate = 80

elif tactic == "Short Pearl":
    if playstyle == "Defensive":
        rate = 65
    elif playstyle == "Aggressive":
        rate = 80

elif tactic == "Gap":
    if gamesense == "High":
        rate = 85
    else:
        rate = 60

elif tactic == "Totem":
    rate = 50  # Neutral outcome in most cases

# Add modifiers
if playstyle == "Defensive" and tactic == "Web":
    rate += 10
if cps.startswith("High"):
    rate += 5
if gamesense == "High":
    rate += 5
if health == "Low":
    rate -= 10

return min(max(rate, 0), 100)  # Clamp to 0-100

--- Calculate ---

success_rate = calculate_success_rate(health, cps, gamesense, playstyle, tactic)

st.markdown(f"### 📊 Success Rate of Selected Strategy: {success_rate}%")

--- Graph ---

data = pd.DataFrame({ 'Strategy': ["Your Selection", "Average"], 'Success Rate': [success_rate, 50] })

chart = alt.Chart(data).mark_bar().encode( x='Strategy', y='Success Rate', color=alt.condition( alt.datum.Strategy == "Your Selection", alt.value('green'), alt.value('gray') ) ).properties( width=400, height=300 )

st.altair_chart(chart, use_container_width=True)

st.caption("This simulator is based on hypothetical data and in-game PvP logic provided by the community. Not tied to Mojang or Microsoft.")

