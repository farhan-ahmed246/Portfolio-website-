import streamlit as st
import requests
import os
from streamlit_lottie import st_lottie

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="My Portfolio",
    page_icon="🎉",
    layout="wide"
)

# ---------------- Lottie Loader ----------------
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---------------- Lottie Animation ----------------
lottie_animation = load_lottieurl(
    "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"
)

# ---------------- Header ----------------
st.subheader("My Personal Portfolio 👋")
st.title("Welcome to My Personal Portfolio")
st.write("This is a place where I share my projects and work.")
st.write("[Learn More >](https://www.linkedin.com)")

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


for i, proj in enumerate(projects):
    with cols[i]:
        if os.path.exists(proj["image"]):
            st.image(proj["image"], width=180)
        else:
            st.warning("Image missing")
        st.subheader(proj["title"])
        st.write(proj["description"])
        st.markdown(f"[View Project]({proj['link']})")

# ---------------- Contact Info ----------------
st.write("---")
st.header("Contact Info")
st.write("📞 +92 336 3016943")
st.write("📧 ucristano37@gmail.com")

# ---------------- CONTACT FORM CSS (SAFE) ----------------
st.markdown("""
<style>
form {
    display: flex;
    flex-direction: column;
    gap: 14px;
}

input, textarea {
    padding: 12px;
    font-size: 16px;
    border-radius: 6px;
    border: 1px solid #ccc;
    width: 100%;
}

textarea {
    min-height: 120px;
}

button {
    padding: 12px;
    font-size: 16px;
    background-color: #2563eb;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
}

button:hover {
    background-color: #1e40af;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Contact Form ----------------
st.write("---")
st.header("Get In Touch With Me!")

contact_form = """
<form action="https://formsubmit.co/ucristano37@gmail.com" method="POST">
  <input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="_template" value="table">

  <input type="text" name="name" placeholder="Your Name" required>
  <input type="email" name="email" placeholder="Your Email" required>
  <textarea name="message" placeholder="Your Message" required></textarea>

  <button type="submit">Send Message 🚀</button>
</form>
"""

left, right = st.columns(2)

with left:
    st.markdown(contact_form, unsafe_allow_html=True)

else:
    st.print("YOUR MESSAGE HAS BEEN DELIVERED.")
