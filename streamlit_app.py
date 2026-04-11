import streamlit as st
import datetime
import git
from datetime import timezone
from zoneinfo import ZoneInfo

st.title("Brandon Cannizzo")
st.write(
    "I will use this page to advertise my skills and experience \n\n :no_pedestrians: Coming Soon :no_pedestrians:"
)

st.image('src/images/LinkedIn_pfp_cropped.jpg', width=400, caption="Check out my profiles below!")

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
    st.markdown("[Experience](#experience)")
    st.markdown("[Education](#education)")
    st.markdown("[Skills](#skills)")
    st.markdown("[Certifications](#certifications)")

st.divider()
st.header(":material/Info: About Me", anchor="about-me")
st.write('''
        NJIT alumnus with an M.S. in Computer Engineering, searching 
        for a rewarding opportunity where I can to put my knowledge and 
        skills to use in an impactful and rewarding way. An experienced Radar, 
        AI, and machine learning researcher; with a focus in wireless communications 
        and computer networking. Able to collaborate or complete tasks independently.
        ''')

st.divider()
st.header(":material/docs: Resume", anchor="resume")

# Resume Download Button
with open("src/files/Brandon Cannizzo Resume 2026.pdf", "rb") as file:
    st.download_button(label=":material/Download: Download a PDF of my Resume!", file_name="Brandon Cannizzo Resume 2026.pdf", data=file, mime="application/pdf")

st.divider()

# Work Experience Section
st.title(":material/Work: Experience", anchor="experience")

# Offer different views for Experience for testing purposes
choice = st.selectbox("Choose formatting option for realtime comparison", 
                      ("Expanders", "Columns", "Tabs"))

Harmony_Text = """
            ● Enrolled and removed devices from the environment utilizing Windows Autopilot

            ● Daily monitoring device and user info in Active Directory, Intune, N-Sight RMM, and Sophos

            ● Device experience includes Windows Surface Laptops and Apple iPads & iPhones

            ● Provided IT support in office (printers, conference rooms, user requests) and for remote users
            """

Aures_Text = """
            ● Worked with chief scientist on the investigation of 5G and future networking for drone-based applications
            
            ● Led the research and design of AuresTech open source 5G Network using OAI 5G Core Network
            
            ● Migrated AuresTech Network to hardware
            
            ● Perform testing of over the air AuresTech proprietary system and collected data for evaluation
            """

NJIT_text = """
            ● Lab work – Extensive use of Lab View and MATLAB, alongside hardware simulating Radar
           
            ● Research primarily focused on Radar and Machine learning
            
            ● Generate figures and supply comments for monthly reports
            """


if choice=="Expanders":
    with st.expander("Harmony Biosciences - IT Service Desk"):
        st.write("November 2025 - Present \n\n")
        st.write(Harmony_Text)
        
    with st.expander("AuresTech - Engineer"):
        st.write("June 2024 - September 2025 \n\n")
        st.write(Aures_Text)
        
    with st.expander("New Jersey Institute of Technology - Research Assistant"):
        st.write("May 2023 - May 2024 \n\n")
        st.write(NJIT_text)

        with open("src/files/Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", "rb") as file:
            st.download_button(label="Download a copy of the paper I helped work on", file_name="Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", data=file, mime="application/pdf")

if choice=="Columns":
    col_3, col_4, col_5 = st.columns(3)
    with col_3:
        st.header("Harmony Biosciences - IT Service Desk")
        st.write("November 2025 - Present")
        st.write(Harmony_Text)
        
    with col_4:
        st.header("AuresTech - Engineer")
        st.write("June 2024 - September 2025 \n\n")
        st.write(Aures_Text)

    with col_5:
        st.header("New Jersey Institute of Technology - Research Assistant")
        st.write("May 2023 - May 2024 \n\n")
        st.write(NJIT_text)
        with open("src/files/Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", "rb") as file:
            st.download_button(label="Download a copy of the paper I helped work on", file_name="Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", data=file, mime="application/pdf")


if choice=="Tabs":
    tab_1, tab_2, tab_3 = st.tabs(["Harmony Biosciences", "AuresTech", "New Jersey Institute of Technology"])
    with tab_1:
        st.write("Title: IT Service Desk \n\n Experience")
        st.write(Harmony_Text)
    with tab_2:
        st.write("Title: Engineer \n\n Experience")
        st.write(Aures_Text)
    with tab_3:
        st.write("Title: Research Assistant \n\n Experience")
        st.write(NJIT_text)
        with open("src/files/Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", "rb") as file:
            st.download_button(label="Download a copy of the paper I helped work on", file_name="Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", data=file, mime="application/pdf")

st.divider()

st.title(":material/School: Education", anchor="education")
col_6, col_7 = st.columns(2)
with col_6:
    st.image('src/images/NJIT_simple.png', width="content", link="https://www.njit.edu/")

with col_7:
    st.write("New Jersey Institute of Technology")

st.write(''' May 2023 - BS In Computer Engineering \n\n May 2024 - MS In Computer Engineering
         ''')

st.divider()
st.header(":material/Build_Circle: Skills", anchor="skills")
# Can break this up like Programming Languages, Hardware, IT/Security
st.write("Python, C++, MATLAB, Java")
st.write("Help Desk iPad/PC Repair, Radio Equipment, Spectrum Analysis")
st.write("Active Directory, Intune, Sophos, On-Site & Remote Assistance")

st.divider()

st.header(":material/Verified: Certifications", anchor="certifications")
st.write(":material/Exclamation: Working on it :material/Exclamation:")

st.divider()
# Get latest commit date

# Get the latest commit object from the current active branch
latest_commit = git.Repo().head.commit 

# Access the committed date and convert it to a readable format
commit_date_timestamp = latest_commit.committed_date
commit_date = datetime.datetime.fromtimestamp(commit_date_timestamp)

est_time= commit_date.astimezone(ZoneInfo("America/New_York"))

st.caption(f"Last Updated: {est_time} (EST)")