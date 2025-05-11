import streamlit as st

st.set_page_config(page_title="Hardener Mixing Calculator", layout="centered")
st.title("🧪 Hardener Mixing Calculator")

st.markdown("Enter your **Hardener ratio part** and the **actual Resin weight**. The Resin part is fixed at 100, and the tolerance is fixed at ±3%.")

# --- Fixed specs ---
mix_resin = 100.0
tolerance_percent = 3.0

st.info(f"🔢 Mixing Ratio: **{mix_resin} : [your hardener]**")
st.info(f"🎯 Tolerance: **±{tolerance_percent}%**")

# --- Inputs ---
col1, col2 = st.columns(2)
with col1:
    mix_hardener = st.number_input("Hardener Ratio Part", min_value=1.0, step=0.1)
with col2:
    resin_weight = st.number_input("Actual Resin Weight (g)", min_value=0.0, step=0.1)

# --- Real-time Calculation ---
if resin_weight > 0 and mix_hardener > 0:
    ideal_hardener = (resin_weight / mix_resin) * mix_hardener
    tolerance = ideal_hardener * (tolerance_percent / 100)
    min_acc = ideal_hardener - tolerance
    max_acc = ideal_hardener + tolerance

    st.success("💡 Computed Results")
    st.write(f"**Ideal Hardener Weight:** `{ideal_hardener:.2f} g`")
    st.write(f"**Acceptable Range:** `{min_acc:.2f} g` – `{max_acc:.2f} g`")
else:
    st.info("Please enter values above to see the results.")
