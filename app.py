
import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Family Class Classifier", page_icon="🏡", layout="centered")

st.title("🏡 Family Class Classification Tool")
st.write("Adjust the sliders below to determine the family tier based on purchase power and property specs.")

st.markdown("---")


st.subheader("🎛️ Adjust Property & Financial Criteria")


purchase_price = st.slider(
    "💰 Purchase Price (EGP / USD)", 
    min_value=100000, 
    max_value=5000000, 
    value=1200000, 
    step=50000,
    format="%d"
)

# House Type Selection
house_type = st.select_slider(
    "🏢 House Type",
    options=["Low class House type", "Middle class House type", "High class House type"],
    value="Middle class House type"
)

# Unit Size Selection
unit_size = st.select_slider(
    "📐 Unit Size",
    options=["Narrow size Units", "Middle size Units", "Wide size Units"],
    value="Middle size Units"
)

st.markdown("---")

# 3. Classification Logic Engine
st.subheader("📊 Dynamic Classification Result")

# Logic to calculate family tier based on your rules
if purchase_price > 2500000 and house_type == "High class House type" and unit_size == "Wide size Units":
    family_class = "👑 High Class Family"
    bg_color = "rgba(255, 215, 0, 0.2)"  # Gold background
    text_color = "#8B8000"
    description = "Rich family with high purchasing power, premium property, and wide layout units."

elif purchase_price >= 1000000 and house_type == "Middle class House type" and unit_size == "Middle size Units":
    family_class = "⚖️ Middle Class Family"
    bg_color = "rgba(0, 128, 255, 0.2)"  # Blue background
    text_color = "#0056b3"
    description = "Standard family profile with stable purchasing power and standard property specs."

elif purchase_price < 1000000 and house_type == "Low class House type" and unit_size == "Narrow size Units":
    family_class = "🌱 Low Class Family"
    bg_color = "rgba(128, 128, 128, 0.2)"  # Gray background
    text_color = "#555555"
    description = "Basic budget tier family with smaller unit layouts and essential pricing."

else:
    family_class = "❓ Mixed / Unclassified Profile"
    bg_color = "rgba(255, 165, 0, 0.2)"  # Orange background
    text_color = "#cc7a00"
    description = "The selected criteria do not cleanly match a single strict family class definition."

# 4. Interactive Display UI Box
st.markdown(
    f"""
    <div style="background-color: {bg_color}; padding: 20px; border-radius: 10px; border-left: 5px solid {text_color};">
        <h3 style="color: {text_color}; margin-top: 0;">{family_class}</h3>
        <p style="color: #333333; font-size: 16px; margin-bottom: 5px;"><b>Current Selection Specs:</b></p>
        <ul style="color: #333333; margin-top: 0;">
            <li>Price: {purchase_price:,}</li>
            <li>House: {house_type}</li>
            <li>Unit Size: {unit_size}</li>
        </ul>
        <small style="color: #666666; font-style: italic;">{description}</small>
    </div>
    """,
    unsafe_allow_html=True)
