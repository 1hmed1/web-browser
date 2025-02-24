# import streamlit  as st 
# import pandas as pd
# import os 
# from io import BytesIO


# st.set_page_config(page_title="Datasweeper", layout= 'wide')
# st.title("")
# import streamlit as st



# st.markdown("<h1 style='text-align: center; color: blue;'>🌟 Welcome to My Amazing Website! 🚀</h1>", unsafe_allow_html=True)
# st.markdown("<h2 style='text-align: center; color:blue;'>Explore the power of Python and build amazing web apps with easy 💡!</h2>", unsafe_allow_html=True)
import streamlit as st

# Custom CSS for Styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://source.unsplash.com/1600x900/?technology,nature");
        background-size: cover;
        background-position: center;
    }
    .title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        color: #ff5733;
        margin-top: 20px;
    }
    .subtitle {
        text-align: center;
        font-size: 25px;
        color: white;
        font-weight: bold;
    }
    .button {
        background-color: #ff5733;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: block;
        font-size: 20px;
        margin: 20px auto;
        cursor: pointer;
        border-radius: 10px;
        transition: 0.3s;
        width: 50%;
    }
    .button:hover {
        background-color: #e74c3c;
    }
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: rgba(0, 0, 0, 0.7);
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Subtitle
st.markdown("<h1 class='title'>🚀 Welcome to My Amazing Website! 🌟</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitle'>Explore Python and Build Beautiful Web Apps 💡</h2>", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "📊 Analytics", "📞 Contact"])

# Page Routing
if page == "🏠 Home":
    st.write("Welcome to the Home Page! 🎉")
elif page == "📊 Analytics":
    st.write("Here is the analytics dashboard. 📈")
elif page == "📞 Contact":
    st.write("📩 Contact us at: ahmedsheikh0021@gmail.com")
    st.write("📞 Phone No: **03446086595**")

# Hix AI Chat Button
st.markdown(
    """
    <a href="https://hix.ai/" target="_blank">
        <button class="button">🚀 Try Hix AI Chat Now!</button>
    </a>
    """,
    unsafe_allow_html=True
)


# Footer with "Created by Ahmed Sheikh"
st.markdown(
    """
    <div class="footer">
        Created by <b>Ahmed Sheikh</b> 
    </div>
    """,
    unsafe_allow_html=True
)

