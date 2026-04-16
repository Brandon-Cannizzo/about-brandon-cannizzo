import streamlit as st
import datetime
import git
from datetime import timezone
from zoneinfo import ZoneInfo


col1, col2 = st.columns(2, gap="small")
with col1:
    st.image("src/images/LinkedIn_pfp_cropped.jpg", width=300)

with col2:
    st.title("Brandon Cannizzo")
    st.write("IT Service Desk")
    with open("src/files/Brandon Cannizzo Resume 2026.pdf", "rb") as file:
        st.download_button(label=":material/Download: Download my Resume", file_name="Brandon Cannizzo Resume 2026.pdf", data=file, mime="application/pdf")
    if st.button(":material/mail: Contact Me"):
        st.switch_page("2_contact_form.py")


# --- SOCIAL LINKS ---
st.write('\n')
ico_width = 60
with st.container():
    col_1, col_2, col_3 = st.columns(3)
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
    st.markdown("[Experience](#experience)")
    st.markdown("[Education](#education)")
    st.markdown("[Skills](#skills)")
    st.markdown("[Certifications](#certifications)")

st.divider()
st.header(":material/Info: About Me", anchor="about-me")

st.write('''
        NJIT graduate with an M.S. in Computer Engineering, currently
        working in IT at the service desk level but always searching for
        opportunites to learn and grow. I have experience working with Radar and
        machine learning research, cellular communication, and computer networking.
        ''')

st.divider()

# Work Experience Section
st.title(":material/Work: Experience", anchor="experience")

# Offer different views for Experience for testing purposes
choice = st.selectbox("Choose formatting option for realtime comparison", 
                      ("Expanders", "Columns", "Tabs", "Timeline"))

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

NJIT_Text = """ 
● Lab work – Extensive use of Lab View and MATLAB, alongside hardware simulating Radar
● Research primarily focused on Radar and Machine learning
● Generate figures and supply comments for monthly reports
            """


if choice=="Expanders":
    with st.expander("Harmony Biosciences - IT Service Desk"):
        st.text(f"November 2025 - Present\n{Harmony_Text}")
        
    with st.expander("AuresTech - Engineer"):
        st.text(f"June 2024 - September 2025\n{Aures_Text}")
        
    with st.expander("New Jersey Institute of Technology - Research Assistant"):
        st.text(f"May 2023 - May 2024\n{NJIT_Text}")

        with open("src/files/Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", "rb") as file:
            st.download_button(label="Download a copy of the paper I helped work on", file_name="Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", data=file, mime="application/pdf")

if choice=="Columns":
    col_3, col_4, col_5 = st.columns(3)
    with col_3:
        st.header("Harmony Biosciences - IT Service Desk")
        st.text(f"November 2025 - Present\n{Harmony_Text}")

    with col_4:
        st.header("AuresTech - Engineer")
        st.text(f"June 2024 - September 2025\n{Aures_Text}")

    with col_5:
        st.header("New Jersey Institute of Technology - Research Assistant")
        st.text(f"May 2023 - May 2024\n{NJIT_Text}")
        with open("src/files/Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", "rb") as file:
            st.download_button(label="Download a copy of the paper I helped work on", file_name="Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", data=file, mime="application/pdf")


if choice=="Tabs":
    tab_1, tab_2, tab_3 = st.tabs(["Harmony Biosciences", "AuresTech", "New Jersey Institute of Technology"])
    with tab_1:
        st.text(f"Title: IT Service Desk\nExperience\n{Harmony_Text}")
    with tab_2:
        st.text(f"Title: Engineer\nExperience\n{Aures_Text}")
    with tab_3:
        st.text(f"Title: Research Assistant\nExperience\n{NJIT_Text}\nAssisted PHD student with Radar and Machine Learning research, which led to a published paper. You can download a PDF of said paper below.")
        with open("src/files/Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", "rb") as file:
            st.download_button(label="Machine Learning Doppler-Tolerant Download", file_name="Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", data=file, mime="application/pdf")


if choice=="Timeline":
    st.write("test")

st.divider()

st.title(":material/School: Education", anchor="education")
col_6, col_7 = st.columns(2)
with col_7:
    st.image('src/images/NJIT_simple.png', width="content", link="https://www.njit.edu/")

with col_6:
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

# Access the time of the last commit and convert it to a readable format
commit_date_timestamp = latest_commit.committed_date
commit_date = datetime.datetime.fromtimestamp(commit_date_timestamp)

# Convert from UTC to EST
est_time= commit_date.astimezone(ZoneInfo("America/New_York"))

# Create a formatted string with the date/time data I want to display
formatted_str = est_time.strftime("%B %d, %Y %-I:%M:%S %p")
st.caption(f"Last Updated: {formatted_str} (EST)")