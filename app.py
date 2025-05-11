import streamlit as st

st.set_page_config(page_title="Hardener Calculator", layout="centered")
st.title("🧪 Hardener Mixing Calculator")

st.markdown("Enter your mixing specs and actual resin weight. The app will compute the ideal hardener weight and the acceptable range.")

# --- Inputs ---
col1, col2 = st.columns(2)
with col1:
    mix_resin = st.number_input("Resin Ratio Part (e.g. 100)", min_value=1.0, step=1.0)
with col2:
    mix_hardener = st.number_input("Hardener Ratio Part (e.g. 30)", min_value=1.0, step=1.0)

tolerance_percent = st.number_input("Tolerance (%)", value=3.0, step=0.1)

resin_weight = st.number_input("Actual Resin Weight (g)", min_value=0.0, step=0.1)

# --- Computation ---
if resin_weight > 0:
    ideal_hardener = (resin_weight / mix_resin) * mix_hardener
    tolerance = ideal_hardener * (tolerance_percent / 100)
    min_acc = ideal_hardener - tolerance
    max_acc = ideal_hardener + tolerance

    st.success("💡 Results")
    st.write(f"**Ideal Hardener Weight:** {ideal_hardener:.2f} g")
    st.write(f"**Acceptable Range:** {min_acc:.2f} g – {max_acc:.2f} g")
else:
    st.info("Enter actual resin weight to calculate ideal hardener range.")
