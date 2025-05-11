import streamlit as st

st.set_page_config(page_title="Hardener Mixing Calculator", layout="centered")
st.title("🧪 Hardener Mixing Calculator")

st.markdown("Enter your **mixing ratio (hardener only)** and the actual resin weight. Resin is always fixed at 100.")

# --- Mixing Ratio (Resin:Hardener) ---
st.info("🔢 Resin Part: **100** (fixed)")

mix_resin = 100.0
mix_hardener = st.number_input("Hardener Ratio Part (e.g. 30)", min_value=1.0, step=0.1)

# --- Tolerance ---
tolerance_percent = st.number_input("Tolerance (%)", value=3.0, step=0.1)

# --- Actual Resin Weight ---
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
    st.info("Enter the actual resin weight to calculate ideal hardener range.")
