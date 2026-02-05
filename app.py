import streamlit as st
from PyPDF2 import PdfReader
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(page_title="SAY AI Assistant", layout="wide")

# =====================================================
# ⭐ PROFESSIONAL SAY LOGO HEADER
# =====================================================
# =====================================================
# ⭐ CREATIVE PROFESSIONAL SAY HEADER (MODERN STYLE)
# =====================================================

# =====================================================
# ⭐ PROFESSIONAL SVG LOGO HEADER (GRAPHIC STYLE)
# =====================================================

# =====================================================
# PROFESSIONAL SAY HEADER (SAFE VERSION)
# =====================================================

# =====================================================
# ⭐ ROUND PROFESSIONAL SAY LOGO
# =====================================================

# =====================================================
# ⭐ MINIMAL ROUND SAY LOGO (NO BOX)
# =====================================================

# =====================================================
# ⭐ LARGE PROFESSIONAL ROUND SAY LOGO
# =====================================================

st.markdown(
"""
<div style="
display:flex;
align-items:center;
gap:22px;
margin-bottom:35px;
">

<!-- BIG ROUND LOGO -->
<div style="
width:90px;
height:90px;
border-radius:50%;
background:linear-gradient(145deg,
        #1f77ff 0%,
        #00c6ff 50%,
        #7b2cff 100%);
display:flex;
align-items:center;
justify-content:center;
color:white;
font-size:42px;
font-weight:bold;
box-shadow:0 8px 20px rgba(0,0,0,0.25);
">
SAY
</div>

<!-- BIG BRAND TEXT -->
<div>
<div style="
font-size:48px;
font-weight:900;
letter-spacing:4px;
color:#222;
">

</div>

<div style="
font-size:44px;
color:##EAE0C8;
margin-top:-6px;
">
Productivity Powered by AI
</div>
</div>

</div>
""",
unsafe_allow_html=True
)




st.success("AI Office Automation • Offline • Professional System")

# =====================================================
# SIDEBAR
# =====================================================
st.sidebar.title("⚙️ Modules")

menu = st.sidebar.selectbox(
    "Select Tool",
    [
        "💬 Chat Assistant",
        "Email Generator",
        "Report Generator",
        "Text Summarizer",
        "PDF Summarizer",
        "PPT Generator",
        "Poster Generator"
    ]
)

st.sidebar.markdown("---")
st.sidebar.metric("Modules", "7")
st.sidebar.metric("Mode", "Offline AI")

st.sidebar.markdown("---")
st.sidebar.markdown("### 👨‍💻 Developed by")
st.sidebar.write("Soham Kulkarni")
st.sidebar.write("Ayush Lonare")
st.sidebar.write("Yash More")

# =====================================================
# 💬 CHAT ASSISTANT (CHATGPT STYLE)
# =====================================================
if menu == "💬 Chat Assistant":

    st.header("💬 AI Chat Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for role, msg in st.session_state.messages:
        with st.chat_message(role):
            st.markdown(msg)

    prompt = st.chat_input("Ask anything (email, report, summary...)")

    if prompt:

        st.session_state.messages.append(("user", prompt))

        with st.chat_message("user"):
            st.markdown(prompt)

        text = prompt.lower()

        if "email" in text:
            reply = f"""Subject: {prompt}

Dear Sir/Madam,

This email is regarding {prompt}. Kindly review and respond.

Best Regards,
Team SAY
"""

        elif "report" in text:
            reply = f"""REPORT: {prompt}

• Introduction
• Objectives
• Analysis
• Findings
• Conclusion
"""

        else:
            reply = "I can generate emails, reports, summaries, PPTs and posters. Please specify your request."

        st.session_state.messages.append(("assistant", reply))

        with st.chat_message("assistant"):
            st.markdown(reply)

# =====================================================
# EMAIL GENERATOR
# =====================================================
elif menu == "Email Generator":

    st.header("📧 Email Generator")

    topic = st.text_input("Enter purpose")

    if st.button("Generate Email"):

        email = f"""Subject: {topic}

Dear Sir/Madam,

This email is regarding {topic}. Kindly review and respond.

Best Regards,
Team SAY
"""

        st.text_area("Generated Email", email, height=200)
        st.download_button("⬇ Download Email", email, file_name="email.txt")

# =====================================================
# REPORT GENERATOR
# =====================================================
elif menu == "Report Generator":

    st.header("📄 Report Generator")

    topic = st.text_input("Enter topic")

    if st.button("Generate Report"):

        report = f"""REPORT ON {topic}

Introduction
Details
Analysis
Conclusion
"""

        st.text_area("Generated Report", report, height=250)
        st.download_button("⬇ Download Report", report, file_name="report.txt")

# =====================================================
# ⭐ SMART NLP TEXT SUMMARIZER
# =====================================================
elif menu == "Text Summarizer":

    # auto download safely
    try:
        nltk.data.find('tokenizers/punkt')
    except:
        nltk.download('punkt')

    try:
        nltk.data.find('tokenizers/punkt_tab')
    except:
        nltk.download('punkt_tab')

    try:
        nltk.data.find('corpora/stopwords')
    except:
        nltk.download('stopwords')

    st.header("📝 Smart NLP Text Summarizer")

    text = st.text_area("Paste long paragraph")

    if st.button("Summarize Text"):

        sentences = sent_tokenize(text)
        words = word_tokenize(text.lower())

        stop_words = set(stopwords.words("english"))

        freq = defaultdict(int)

        for w in words:
            if w.isalnum() and w not in stop_words:
                freq[w] += 1

        scores = {}
        for sentence in sentences:
            for word in word_tokenize(sentence.lower()):
                if word in freq:
                    scores[sentence] = scores.get(sentence, 0) + freq[word]

        top_sentences = sorted(scores, key=scores.get, reverse=True)[:5]

        summary = "\n• " + "\n• ".join(top_sentences)

        st.text_area("Summary", summary, height=250)
        st.download_button("⬇ Download Summary", summary, file_name="summary.txt")

# =====================================================
# PDF SUMMARIZER
# =====================================================
elif menu == "PDF Summarizer":

    st.header("📄 PDF Summarizer")

    uploaded = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded:

        reader = PdfReader(uploaded)
        text = ""

        for page in reader.pages:
            text += page.extract_text()

        if st.button("Summarize PDF"):
            summary = text[:800] + "..."
            st.text_area("Summary", summary, height=250)
            st.download_button("⬇ Download Summary", summary, file_name="pdf_summary.txt")

# =====================================================
# PPT
# =====================================================
elif menu == "PPT Generator":

    st.header("📊 PPT Generator")
    st.link_button("Open Gamma AI", "https://gamma.app")

# =====================================================
# POSTER
# =====================================================
elif menu == "Poster Generator":

    st.header("🎨 Poster Generator")
    st.link_button("Open Canva", "https://www.canva.com")

