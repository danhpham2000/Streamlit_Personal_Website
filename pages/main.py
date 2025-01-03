import streamlit as st

st.header("Hello, and welcome to my website 👋")
st.markdown("-----------------------------")


intro, image = st.columns(2)

with intro:
    st.write("My name is Danh Pham. I just graduated from San Francisco State University with BS in Computer Science, I am passionate of software engineering, innovative problem-solving, and continuous learning. My journey includes building diverse projects through hackathons and personal endeavors, showcasing adaptability and expertise in modern technologies.")
    st.write("Besides learning, I enjoy reading books, traveling, and exploring new things around the world. I have been to 5 diffrent countries: USA, Thailand, Singapore, Malaysia, and South Korea.")
    st.markdown("**💁‍♂️ Name:** Danh Cong Pham")
    st.markdown("**☘️ Zodiac Sign**: The Dragon 🐉")
    st.markdown("**📝 Recent education:** San Francisco State University")
    st.markdown("**👶 Born in:** Ho Chi Minh City, Vietnam 🇻🇳")
    st.markdown("**📍 Current Location:** Houston, Texas, USA 🇺🇸")
    st.markdown("**⭐️ Interest:** Machine Learning, Data Science, Backend development, Full-stack development")
    st.markdown("**💪 Favorites:** Soccer ⚽️, Reading books 📘, Traveling ✈️, and Coding 💻")


with image:
    st.image("file/IMG_6802.png", caption="My recent picture in Seattle, Washington")

with open("file/Danh_Pham_Resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()
st.download_button("Download my resume", data=PDFbyte, file_name="Danh_Pham_Resume.pdf", mime="application/octet-stream")


st.markdown("-----------------------------")


