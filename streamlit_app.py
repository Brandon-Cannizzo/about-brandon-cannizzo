import streamlit as st
import datetime
import git
from datetime import timezone
from zoneinfo import ZoneInfo

st.title("Brandon Cannizzo")
st.write(
    "I will use this page to advertise my skills and experience \n\n :no_pedestrians: Coming Soon :no_pedestrians:"
)

st.image('src/images/LinkedIn_pfp.jpg', width=400, caption="Check out my profiles below!")

ico_width = 80
with st.container():
    col_1, col_2, col_3 = st.columns(3, width = 200)
    with col_1:
        st.image('src/images/LinkedIn_logo.png', width=ico_width, link="https://www.linkedin.com/in/brandoncannizzo/")
    
    with col_2:
        
        st.image('src/images/github_logo.png', width=ico_width, link="https://github.com/Brandon-Cannizzo")
        
    with col_3:
        st.image('src/images/tryhackme_logo.jpg', width=ico_width, link="https://tryhackme.com/p/Brandoon")



# Sidebar with sections links for easy navigation
with st.sidebar:
    st.title("Sections")
    st.markdown("[About Me](#about-me)")
    st.markdown("[Resume](#resume)")
    st.markdown("[Education](#education)")
    st.markdown("[Skills](#skills)")

st.divider()
st.header(":material/Info: About Me")
st.write("")

st.divider()
st.header(":material/docs: Resume")

# Resume Download Button
with open("src/files/Brandon Cannizzo Resume 2026.pdf", "rb") as file:
    st.download_button(label=":material/Download: Download a PDF of my Resume!", file_name="Brandon Cannizzo Resume 2026.pdf", data=file, mime="application/pdf")

# Work Experience Section
st.title(":material/Work: Experience")

# Offer different views for Experience for testing purposes
choice = st.selectbox("Choose formatting option for realtime comparison", 
                      ("Expanders", "Columns", "Tabs"))

if choice=="Expanders":
    with st.expander("Harmony Biosciences - IT Service Desk"):
        st.write('''
                November 2025 - Present \n\n
                Write detailed explanation of responsibilities and software/hardware experience.
                ''')
        
    with st.expander("AuresTech - Engineer"):
        st.write('''
                June 2024 - September 2025 \n\n
                Write detailed explanation of responsibilities and software/hardware experience.
                ''')
        
    with st.expander("New Jersey Institute of Technology - Research Assistant"):
        st.write('''
                May 2023 - May 2024 \n\n
                Write detailed explanation of responsibilities and software/hardware experience.
                ''')
        with open("src/files/Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", "rb") as file:
            st.download_button(label="Download a copy of the paper I helped work on", file_name="Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", data=file, mime="application/pdf")

if choice=="Columns":
    col_3, col_4, col_5 = st.columns(3)
    with col_3:
        st.header("Harmony Biosciences - IT Service Desk")
        st.write('''
                November 2025 - Present \n\n
                Write detailed explanation of responsibilities and software/hardware experience.
                ''')
        
    with col_4:
        st.header("AuresTech - Engineer")
        st.write('''
                June 2024 - September 2025 \n\n
                Write detailed explanation of responsibilities and software/hardware experience.
                ''')
    with col_5:
        st.header("New Jersey Institute of Technology - Research Assistant")
        st.write('''
                May 2023 - May 2024 \n\n
                Write detailed explanation of responsibilities and software/hardware experience.
                ''')
        with open("src/files/Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", "rb") as file:
            st.download_button(label="Download a copy of the paper I helped work on", file_name="Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", data=file, mime="application/pdf")


if choice=="Tabs":
    tab_1, tab_2, tab_3 = st.tabs(["Harmony Biosciences", "AuresTech", "New Jersey Institute of Technology"])
    with tab_1:
        st.write("Title: IT Service Desk \n\n Experience")
    with tab_2:
        st.write("Title: Engineer \n\n Experience")
    with tab_3:
        st.write("Title: Research Assistant \n\n Experience")
        with open("src/files/Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", "rb") as file:
            st.download_button(label="Download a copy of the paper I helped work on", file_name="Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", data=file, mime="application/pdf")



st.title(":material/School: Education")
col_6, col_7 = st.columns(2)
with col_6:
    st.image('src/images/NJIT_simple.png', width="content", link="https://www.njit.edu/")

with col_7:
    st.write("New Jersey Institute of Technology")

st.write(''' May 2023 - BS In Computer Engineering \n\n May 2024 - MS In Computer Engineering
         ''')

st.divider()
st.header(":material/Build_Circle: Skills")
st.write("...")


st.divider()

# Get latest commit date

# Get the latest commit object from the current active branch
latest_commit = git.Repo().head.commit 

# Access the committed date and convert it to a readable format
commit_date_timestamp = latest_commit.committed_date
commit_date = datetime.datetime.fromtimestamp(commit_date_timestamp)

est_time= commit_date.astimezone(ZoneInfo("America/New_York"))

st.caption(f"Last Updated: {est_time} (EST)")