import os
import streamlit as st
import requests
from streamlit_lottie import st_lottie

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="My Webpage",
    page_icon="🎉",
    layout="wide"
)

# ---------------- Function: Load Lottie (Safe) ----------------
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# ---------------- Sidebar Theme ----------------
st.sidebar.title("Theme Settings")
theme = st.sidebar.radio("Select Theme", ["Light White", "Full White", "Black"])

if theme == "Light White":
    bg = "#f4f6f8"
    text = "#1f2937"
elif theme == "Full White":
    bg = "#ffffff"
    text = "#000000"
else:
    bg = "#0e1117"
    text = "#ffffff"

st.markdown(f"""
<style>
.stApp {{
    background-color: {bg};
    color: {text};
}}
</style>
""", unsafe_allow_html=True)

# ---------------- CSS ----------------

# ---------------- Lottie (WORKING URL) ----------------
lottie_animation = load_lottieurl('https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json')

# ---------------- Header ----------------
st.subheader("My Personal portfolio 👋")
st.title("Welcome to My Personal Portfolio")
st.write("This is a place where I share my projects and work.")
st.write("[Learn More >](https://www.linkedin.com/in/abdul-nafay-98299b382)")

# ---------------- What I Do ----------------
st.write("---")
left_column, right_column = st.columns(2)

with left_column:
    st.header("What I Do")
    st.write("""
    - Project Development  
    - Web / App Design  
    - Automation Tools  
    - Creative Solutions  
    """)

    with right_column:
        if lottie_animation:
            st_lottie(lottie_animation, height=300, key="animation")


# ---------------- Projects ----------------
st.write("---")
st.header("My Projects")

projects = [
        {
            "image": "proj1.png",
            "title": "Currency Exchange App",
            "description": "Global 25 Currency Exchange – Fast, Secure & Anytime 💱",
            "link": "https://www.linkedin.com/posts/abdul-nafay-98299b382_currencyexchange-forextrading-fastcash-activity-7405346219301953536-gk9K"
        },
        {
            "image": "proj2.png",
            "title": "PDF Generator",
            "description": "I Built a Fully Automated PDF Generator Using Python — Turning Complex Documents Into One-Click Exports! 🚀",
            "link": "https://www.linkedin.com/posts/abdul-nafay-98299b382_pythondeveloper-automationtools-pdfgenerator-activity-7401890025140797440-MDk4?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAF55dLIBUEsF4tBVSCY-udhNhU446vcrXFw"
        },
        {
            "image": "proj3.png",
            "title": "Not REAL Airplane Ticket Booking Automation",
            "description": "I Just Built a Complete Flight Registration System Using Streamlit — From User Inputs to Auto-Generated Flight Details ✈️🔥",
            "link": "https://www.linkedin.com/posts/abdul-nafay-98299b382_streamlit-pythonprojects-codingjourney-activity-7399890361235439616-alJs?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAF55dLIBUEsF4tBVSCY-udhNhU446vcrXFw"
        },
        {
            "image": "proj4.png",
            "title": "Quiz Game with Live API",
            "description": "Build a Dynamic Quiz Game with live API using Python 🤖",
            "link": "https://www.linkedin.com/posts/abdul-nafay-98299b382_build-a-dynamic-quiz-game-with-live-api-with-ugcPost-7369632106689323009-TsNS?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAF55dLIBUEsF4tBVSCY-udhNhU446vcrXFw"
        },
        {
            "image": "proj5.png",
            "title": "Calendar App",
            "description": "Enter any year and see full months and dates of that year 🤖",
            "link": "https://www.linkedin.com/posts/abdul-nafay-98299b382_this-is-a-small-project-in-it-if-you-ugcPost-7369974497401180160-6Hpe?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAF55dLIBUEsF4tBVSCY-udhNhU446vcrXFw"
        },
    ]

for proj in projects:
    img_col, txt_col = st.columns((1, 2))

    with img_col:
        if os.path.exists(proj["image"]):
            st.image(proj["image"], width=280)
        else:
            st.warning(f"Missing image: {proj['image']}")

    with txt_col:
        st.subheader(proj["title"])
        st.write(proj["description"])
        st.markdown(f"[Watch Video]({proj['link']})")

    st.write("---")



# ---------------- Contact Info ----------------
st.header("Contact Info")
st.write("📞 +92 336 3016943")
st.write("📧 ucristano37@gmail.com")

# ---------------- Contact Form (FAST & SAFE) ----------------
st.write("---")
st.header("Get In Touch With Me!")

contact_form = """
<form action="https://formsubmit.co/ucristano37@gmail.com" method="POST">
  <input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="_template" value="table">
  <input type="hidden" name="_next" value="https://thankyou-page.vercel.app">

  <input type="text" name="name" placeholder="Your Name" required>
  <input type="email" name="email" placeholder="Your Email" required>
  <textarea name="message" placeholder="Your Message" required></textarea>

  <button type="submit">Send Message 🚀</button>
</form>
"""

left, right = st.columns(2)
with left:
    st.markdown(contact_form, unsafe_allow_html=True)
with right:
    st.info("Your message will be delivered safely & quickly ✅")
