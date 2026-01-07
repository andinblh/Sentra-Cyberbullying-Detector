import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from classifier import classify_comment

# PAGE CONFIG
st.set_page_config(
    page_title="Sentra: Cyberbullying Detector",
    page_icon="🛡️",
    layout="centered"
)

# HEADER
st.markdown(
    "<h1 style='text-align: center;'>🛡️ Sentra: Cyberbullying Detector</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; font-size:18px; color:gray;'>Detect • Classify • Protect</p>",
    unsafe_allow_html=True
)


st.divider()

# INPUT SECTION
with st.container():
    st.subheader(" Input Komentar")

    comment = st.text_area(
        "Masukkan komentar yang ingin dianalisis",
        height=140,
        placeholder= "Ketikkan komentar disini..."
    )

    detect_btn = st.button(" Deteksi", use_container_width=True)

# OUTPUT SECTION
if detect_btn:

    if comment.strip() == "":
        st.warning(" Masukkan komentar terlebih dahulu.")
    
    else:
        with st.spinner("Menganalisis komentar..."):
            result = classify_comment(comment)

        st.divider()
        st.subheader(" Hasil Deteksi")

        # Ringkasan status
        if result["category"] == "Bullying":
            st.error(" Komentar terdeteksi sebagai **BULLYING**")
        else:
            st.success(" Komentar terdeteksi sebagai **NON-BULLYING**")

        # METRICS
        col1, col2, col3 = st.columns(3)

        col1.metric("Kategori", result["category"])
        col2.metric("Tipe", result["type"])
        col3.metric("Confidence", f"{result['confidence']:.2f}")

        # DETAIL
        with st.expander(" Detail Analisis"):
            st.write(f"**Original Text:**\n{result['original']}")
            st.write(f"**Translated Text:**\n{result['translated']}")
            st.write(f"**Detected by:** {result['detected_by']}")

