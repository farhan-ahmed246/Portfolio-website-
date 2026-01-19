import os
import streamlit as st
import webbrowser
import requests
from PIL import Image
from streamlit_lottie import st_lottie

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Farhan Portfolio", page_icon="🔥", layout="wide")

# ---------------- BLACK BACKGROUND FIX ----------------
st.markdown("""
<style>
.stApp {
    background-color: #000000;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "section" not in st.session_state:
    st.session_state.section = "projects"

# ---------------- LOTTIE LOADER ----------------
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_anim = load_lottie("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# ---------------- TOP NAV BAR ----------------
left, space, right = st.columns([2, 5, 4])

with left:
    if st.button("📁 Projects"):
        st.session_state.section = "projects"

with right:
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("📞 Contact"):
            st.session_state.section = "contact"
    with c2:
        if st.button("🛠 Skills"):
            st.session_state.section = "skills"
    with c3:
        if st.button("📄 Resume"):
            st.session_state.section = "resume"

st.markdown("---")

# ---------------- HERO SECTION ----------------
colA, colB = st.columns(2)
with colA:
    st.title("Farhan Ahmed")
    st.subheader("Agentic AI Devloper | Python Developer | Web Developer")
with colB:
    if lottie_anim:
        st_lottie(lottie_anim, height=300)

# ---------------- PROJECTS ----------------
projects = [
    {
        "title": "PDF Generator",
        "desc": "Automation tool using Python to generate PDFs.",
        "image": "proj2.png",
        "url": "https://www.linkedin.com/posts/farhan-ahmed-05140b299_pythondeveloper-automationtools-pdfgenerator"
    },
    {
        "title": "Airplane Ticket App",
        "desc": "Streamlit app for airplane ticket registration.",
        "image": "proj1.png",
        "url": "https://www.linkedin.com/posts/farhan-ahmed-05140b299_streamlit-pythonprojects"
    },
    {
        "title": "Currency Exchanger",
        "desc": "Real-time currency converter with Forex.",
        "image": "proj3.png",
        "url": "https://www.linkedin.com/posts/farhan-ahmed-05140b299_currencyexchange"
    },
    {
        "title": "Quiz Game",
        "desc": "Live API based quiz game.",
        "image": "proj4.png",
        "url": "https://www.linkedin.com/posts/farhan-ahmed-05140b299_quizgame"
    },
    {
        "title": "Streamlit Web App",
        "desc": "Complete interactive Streamlit app.",
        "image": "proj6.png",
        "url": "https://www.linkedin.com/posts/farhan-ahmed-05140b299_streamlit-web"
    }
]

if st.session_state.section == "projects":
    st.header("📁 My Projects")
    for p in projects:
        st.subheader(p["title"])
        st.write(p["desc"])

        if os.path.exists(p["image"]):
            st.image(p["image"], width=600)
        else:
            st.error(f"Image file missing: {p['image']}")

        if st.button(f"▶ Watch {p['title']}"):
            webbrowser.open_new_tab(p["url"])
        st.markdown("---")

# ---------------- CONTACT ----------------
if st.session_state.section == "contact":
    st.header("📞 Contact Me")

    col1, col2 = st.columns(2)
    with col1:
        st.button("📱 WhatsApp: +92 336 3016943")
    with col2:
        st.button("📧 Email: fmukhtar420@gmail.com")

    st.markdown("### Send Message")

   
st.header("📞 Contact Me")



contact_form = """

<form action="https://formsubmit.co/ucristano37@gmail.com" method="POST">
  <input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="_template" value="table">

  <input type="text" name="name" placeholder="Your Name" required
   style="width:100%; padding:10px; margin-bottom:10px; border-radius:5px;">

  <input type="email" name="email" placeholder="Your Email" required
   style="width:100%; padding:10px; margin-bottom:10px; border-radius:5px;">

  <textarea name="message" placeholder="Your Message" required
   style="width:100%; padding:10px; margin-bottom:10px; border-radius:5px;"></textarea>

  <button type="submit"
   style="width:100%; padding:12px; background:#ff4b4b; color:white;
   border:none; border-radius:6px; font-size:16px;">
   Send Message 🚀
  </button>
</form>
"""

left, right = st.columns(2)

with left:
    st.markdown(contact_form, unsafe_allow_html=True)

with right:
    st.info("📨 Your message will be delivered safely & quickly ✅")


# ---------------- SKILLS ----------------
if st.session_state.section == "skills":
    st.header("🛠 Skills")
    st.write("""
- HTML  
- CSS  
- TypeScript  
- JavaScript  
- Node.js  
- Tailwind CSS  
- Python  
- Agentic AI Developer  
""")

# ---------------- RESUME ----------------
if st.session_state.section == "resume":
    st.header("📄 Download Resume")
    st.markdown(
        '<a href="/mnt/data/your_cv.docx" download '
        'style="color:white; background:#444; padding:12px; border-radius:6px; text-decoration:none;">Download CV</a>',
        unsafe_allow_html=True
    )


 
