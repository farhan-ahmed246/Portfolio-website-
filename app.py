import os
import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie
import webbrowser

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="My Webpage",
    page_icon="🎉",
    layout="wide"
)

# ---------------- Lottie Loader ----------------
def load_lottieurl(url):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

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

# ---------------- Header ----------------
st.subheader("My Personal Portfolio 👋")
st.title("Welcome to My Personal Portfolio")
st.write("This is a place where I share my projects and work.")
st.write("[LinkedIn Profile](https://www.linkedin.com/in/farhan-ahmed-05140b299)")

# ---------------- Lottie Animation ----------------
lottie_animation = load_lottieurl(
    "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"
)

left_col, right_col = st.columns(2)
with left_col:
    st.header("What I Do")
    st.markdown("""
    - Project Development  
    - Web / App Design  
    - Automation Tools  
    - Creative Solutions  
    """)
with right_col:
    if lottie_animation:
        st_lottie(lottie_animation, height=300)



# ---------------- Contact Info Buttons ----------------
st.subheader("Contact Me 📞✉️")
col1, col2 = st.columns(2)
with col1:
    if st.button("📞 WhatsApp / Call +92 336 3016943"):
        webbrowser.open_new_tab("https://wa.me/923363016943")
with col2:
    if st.button("📧 Email: ucristao37@gmail.com"):
        webbrowser.open_new_tab("mailto:ucristao37@gmail.com")

st.write("---")

# ---------------- Projects ----------------
projects = [
    {
        "title": "PDF GENERATOR",
        "description": "Automation tool using Python to generate PDFs easily.",
        "image": "proj2.png",
        "url": "https://www.linkedin.com/posts/farhan-ahmed-05140b299_pythondeveloper-automationtools-pdfgenerator-activity-7412236161559191552-jQlG?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEgkSn0BsUyA_gMmgApiEXNCiDDJpFKzilE"
    },
    {
        "title": "Airplane Flight",
        "description": "Streamlit app to manage airplane ticket registrations.",
        "image": "proj1.png",
        "url": "https://www.linkedin.com/posts/farhan-ahmed-05140b299_streamlit-pythonprojects-codingjourney-activity-7400967741312004097-J1_j?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEgkSn0BsUyA_gMmgApiEXNCiDDJpFKzilE"
    },
    {
        "title": "Currency Exchanger",
        "description": "Real-time currency converter with Forex integration.",
        "image": "proj3.png",
        "url": "https://www.linkedin.com/posts/farhan-ahmed-05140b299_currencyexchange-forextrading-fastcash-activity-7410780475549450241-L-a3?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEgkSn0BsUyA_gMmgApiEXNCiDDJpFKzilE"
    },
    {
        "title": "Streamlit Web App",
        "description": "Complete Streamlit web app for interactive projects.",
        "image": "proj5.png",
        "url": "https://www.linkedin.com/posts/farhan-ahmed-05140b299_title-build-a-complete-streamlit-web-activity-7401542239014862848-ndM4?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEgkSn0BsUyA_gMmgApiEXNCiDDJpFKzilE"
    },
    {
        "title": "Quiz Game with Live API",
        "description": "Interactive quiz game fetching questions from live APIs.",
        "image": "proj4.png",
        "url": "https://www.linkedin.com/posts/farhan-ahmed-05140b299_quizgame-programmingproject-webdevelopment-activity-7419014868546060288-Zhlp?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEgkSn0BsUyA_gMmgApiEXNCiDDJpFKzilE"
    }
]

for project in projects:
    st.subheader(project["title"])
    st.write(project["description"])
    img = Image.open(project["image"])
    st.image(img, use_column_width=True)
    
    # Watch Now button
    if project["url"]:
        if st.button(f"▶ Watch Now: {project['title']}"):
            webbrowser.open_new_tab(project["url"])
    
    # Download Resume button
    if st.button(f"📄 Download Resume: {project['title']}"):
        webbrowser.open_new_tab("/mnt/data/53bf4c03-001e-499c-ba26-53bde8ca1b4e.docx")
    
    st.write("---")

# ---------------- Skills ----------------
st.subheader("Skills 🛠️")
skills = ["HTML", "TypeScript", "JavaScript", "Python", "Agentic AI Engineer", "Next.js"]
st.write(", ".join(skills))

# ---------------- Social Buttons ----------------
st.write("Connect with me:")
col1, col2 = st.columns(2)
with col1:
    if st.button("🔗 LinkedIn"):
        webbrowser.open_new_tab("https://www.linkedin.com/in/farhan-ahmed-05140b299")
with col2:
    if st.button("🐙 GitHub"):
        webbrowser.open_new_tab("https://github.com/farhan-ahmed246")
