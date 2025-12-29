import streamlit as st
import requests
from streamlit_lottie import st_lottie

# ---------------------- Page Config ----------------------
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ---------------------- Function to load Lottie ----------------------
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.sidebar.title("Theme Settings")
theme = st.sidebar.radio(
    "Select Theme",
    ["Light White", "Full White", "Black"]
)
if theme == "Light White":
    st.markdown("""
    <style>
    .stApp {
        background-color: #f4f6f8;
        color: #1f2937;
    }
    </style>
    """, unsafe_allow_html=True)

elif theme == "Full White":
    st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
        color: #000000;
    }
    </style>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Load Lottie animation
lottie_animation = load_lottieurl('https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json')

# ---------------------- Header Section ----------------------
st.subheader("Hi! I am Abdul Nafay :wave:")
st.title("Welcome to My Personal Portfolio")
st.write("This is a place where I share my projects and work.")
st.write("[Learn More >](https://www.linkedin.com/in/abdul-nafay-98299b382)")

# ---------------------- What I Do Section ----------------------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            - Project Development
            - Web / App Design
            - Automation Tools
            - Creative Solutions
            - Other Personal Projects
            """
        )
        st.write("[Learn More >](https://www.linkedin.com/in/abdul-nafay-98299b382)")
    
    with right_column:
        if lottie_animation:
            st_lottie(lottie_animation, height=300, key="animation")

# ---------------------- Projects Section ----------------------
with st.container():
    st.write('---')
    st.header('My Projects')
    st.write('##')

    # List of projects
    projects = [
        {
            "image": "project1.png",
            "title": "Currency Exchange App",
            "description": "Global 25 Currency Exchange – Fast, Secure & Anytime 💱",
            "link": "https://www.linkedin.com/posts/abdul-nafay-98299b382_currencyexchange-forextrading-fastcash-activity-7405346219301953536-gk9K"
        },
        {
            "image": "project2.png",
            "title": "PDF Generator",
            "description": "I Built a Fully Automated PDF Generator Using Python — Turning Complex Documents Into One-Click Exports! 🚀",
            "link": "https://www.linkedin.com/posts/abdul-nafay-98299b382_pythondeveloper-automationtools-pdfgenerator-activity-7401890025140797440-MDk4?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAF55dLIBUEsF4tBVSCY-udhNhU446vcrXFw"
        },
        {
            "image": "project3.png",
            "title": "Not REAL Airplane Ticket Booking Automation",
            "description": "I Just Built a Complete Flight Registration System Using Streamlit — From User Inputs to Auto-Generated Flight Details ✈️🔥",
            "link": "https://www.linkedin.com/posts/abdul-nafay-98299b382_streamlit-pythonprojects-codingjourney-activity-7399890361235439616-alJs?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAF55dLIBUEsF4tBVSCY-udhNhU446vcrXFw"
        },
        {
            "image": "project4.png",
            "title": "Quiz Game with Live API",
            "description": "Build a Dynamic Quiz Game with live API using Python 🤖",
            "link": "https://www.linkedin.com/posts/abdul-nafay-98299b382_build-a-dynamic-quiz-game-with-live-api-with-ugcPost-7369632106689323009-TsNS?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAF55dLIBUEsF4tBVSCY-udhNhU446vcrXFw"
        },
        {
            "image": "project5.png",
            "title": "Calendar App",
            "description": "Enter any year and see full months and dates of that year 🤖",
            "link": "https://www.linkedin.com/posts/abdul-nafay-98299b382_this-is-a-small-project-in-it-if-you-ugcPost-7369974497401180160-6Hpe?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAF55dLIBUEsF4tBVSCY-udhNhU446vcrXFw"
        },
    ]

    # Display each project
    for proj in projects:
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(proj["image"], width=300)  # Updated: use width instead of use_column_width
        with text_column:
            st.subheader(proj["title"])
            st.write(proj["description"])
            st.markdown(f'[Watch Video]({proj["link"]})')  # Changed text here
        st.write('---')

# ---------------------- Additional Section Placeholder ----------------------
with st.container():
    st.header("Contact Info")
    st.write("phone number: +92 3363016943")
    st.write("email: ucristano37@gamail.com")

with st.container():
    st.header("My social media accounts")
    st.write("LinkedIn: https // linkedin.com/in/abdul-nafay-98299b382")
    st.write("Github: github.com/AbdulNafay37")

with st.container():
    st.write("-------")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """

<form class="contact-form"
action="https://formsubmit.co/ucristano37@gmail.com"
method="POST">

<input type="hidden" name="_captcha" value="false">
<input type="text" name="name" placeholder="Your name" required>
<input type="email" name="email" placeholder="Your email" required>

<textarea name="message" placeholder="Your message here" required></textarea>

<button type="submit">Send</button>
</form>

"""
    
left_column, right_column = st.columns(2)
with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
        st.empty()    
