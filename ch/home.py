import streamlit as st

# Set the page layout

# Home Title
st.title("🏠 Home")

# Logo Banner with reduced size
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://cdn.jsdelivr.net/gh/AadishY/EcoSnap@main/Logo/Squarecorner.png" width="700">
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    # <div style="text-align: center;">
    #     <a href="https://github.com/AadishY/EcoSnap">
    #         <img src="https://img.shields.io/badge/Source%20Code-GitHub-green" alt="GitHub">
    #     </a>
    # </div>
    """,
    unsafe_allow_html=True
)

# Title and Description in the center
st.markdown("<h2 style='color: #2e8b57;'>🌿 EcoSnap: Your Eco-Friendly AI Assistant</h2>", unsafe_allow_html=True)


st.markdown("<h5 style='color: #3e8e41;'>An AI-powered application to classify waste and find proper disposal steps.</h5>", unsafe_allow_html=True)

# Description Section
st.markdown("""

**EcoSnap** is an AI-powered go-to tool for waste disposal, utilizing cutting-edge image recognition technology to identify waste types and assist in effective waste management. Our mission is to promote healthy practices for a cleaner environment. EcoSnap offers a range of innovative features to simplify waste management and spread waste awareness:

#### **EcoSnap** 📸
**Snap a picture of any waste item**, and EcoSnap will identify it and provide detailed information about the waste. You'll also receive step-by-step instructions on how to dispose of it properly.

#### **EcoAlt** 🌱
**Discover eco-friendly alternatives** to your everyday products. EcoAlt helps you make choices that are not only healthier but also reduce your carbon footprint, contributing to a sustainable lifestyle.

#### **EcoTalk** 💬
**Chat with our AI bot** to gain insights into waste management, recycling, and sustainable practices. EcoTalk is here to answer all your questions and raise awareness about environmental issues.

🌟 **Join us in our mission to foster environmental awareness and offer practical solutions for a greener, healthier future. Together, we can make a difference!** 🌟

---
""", unsafe_allow_html=True)



# Navigation Buttons (not in the same line, one below the other)
if st.button("Go to EcoSnap 📸"):
    st.switch_page("ch/EcoSnap.py")

if st.button("Go to EcoAlt 🌱"):
    st.switch_page("ch/EcoAlt.py")

if st.button("Go to EcoTalk 🗣️"):
    st.switch_page("ch/EcoTalk.py")

st.write("---")
# About Us Section
st.markdown("<h2 style='color: #4682b4;'>About Us</h2>", unsafe_allow_html=True)

st.markdown("""
#### **Our Project** 🚀  
We created EcoSnap for the Sustainable Innovators competition, aiming to deliver a user-friendly application that encourages green choices. We are enthusiastic about making a positive environmental impact and inviting others to join us in our mission. 🌿

For more details about our projects or contacting with us, you can visit my <a href="https://github.com/AadishY">
    <img src="https://img.shields.io/badge/Github-Profile-green" alt="GitHub">
</a>

Thank you for visiting our page and supporting our efforts to make the world a greener place! Your interest and involvement are crucial in driving the change towards a more sustainable future. 🌏
""", unsafe_allow_html=True)


st.write("---")

st.markdown("<h2 style='color: #6a5acd;'>Credit</h2>", unsafe_allow_html=True)

st.markdown("""
We would like to extend our gratitude to the following:

- **Google Gemini** 🧠: For providing advanced image recognition capabilities.
- **Groq** 🚀: For powering our text models with high performance.
- **Streamlit** 🌐: For enabling us to create this web application from python with ease.
""")
st.write("---")
st.markdown("""
<div style="text-align: center;">
    <h2 style='color: #32cd32;'>Thank You!</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("""
We deeply appreciate your support for EcoSnap! 🌟
**Your interest** helps drive our mission for a sustainable future. 🌍 Together, we can make a positive impact on the environment. 🌿
Thank you for joining us on this journey! 💪
""", unsafe_allow_html=True)
