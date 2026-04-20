import streamlit as st
import datetime
import git
from datetime import timezone
from zoneinfo import ZoneInfo

# Page Header
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image("src/images/LinkedIn_pfp_cropped.jpg", width=300)

with col2:
    st.title("Brandon Cannizzo", anchor=False)
    st.subheader("IT Service Desk", anchor=False)
    with open("src/files/Brandon Cannizzo Resume 2026.pdf", "rb") as file:
        st.download_button(label=":material/Download: Download my Resume", file_name="Brandon Cannizzo Resume 2026.pdf", data=file, mime="application/pdf")
    if st.button(":material/mail: Contact Me"):
        st.switch_page("2_contact_form.py")

# Social Links
ico_width = 60
with st.container(horizontal="True", horizontal_alignment="distribute"):
        st.image('src/images/LinkedIn_logo.png', width=ico_width, link="https://www.linkedin.com/in/brandoncannizzo/")
        st.image('src/images/github_logo.png', width=ico_width, link="https://github.com/Brandon-Cannizzo")
        st.image('src/images/tryhackme_logo.jpg', width=ico_width, link="https://tryhackme.com/p/Brandoon")

# Sidebar with sections links for easy navigation
with st.sidebar:
    st.title("Sections")
    st.markdown('''
        [About Me](#about-me)\n\n
        [Experience](#experience)\n\n
        [Education](#education)\n\n
        [Skills](#skills)\n\n
        [Certifications](#certifications)''')

st.divider()
# About Me introduction 
st.header(":material/Info: About Me", anchor="about-me")

st.write('''
        NJIT graduate with an M.S. in Computer Engineering, currently
        working in IT at the service desk level but always searching for
        opportunites to learn and grow. Past experience working with Radar and
        machine learning research, cellular communication, computer networking, 
        and IT help desk services.
        ''')

st.divider()
# Work Experience Section
st.title(":material/Work: Experience", anchor="experience")

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

# Create tabbed view of work experience
tab_1, tab_2, tab_3 = st.tabs(["Harmony Biosciences", "AuresTech", "New Jersey Institute of Technology"])
with tab_1:
    st.text(f"IT Service Desk\nNovember 2025 - Present\n{Harmony_Text}")
with tab_2:
    st.text(f"Engineer\nJune 2024 - September 2025\n{Aures_Text}")
with tab_3:
    st.text(f"Research Assistant\nMay 2023 - May 2024\n{NJIT_Text}\nAssisted PHD student with Radar and Machine Learning research, which led to a published paper. You can download a copy or view it online below.")
    with st.container(horizontal="True"):
        with open("src/files/Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", "rb") as file:
            st.download_button(icon=":material/download:", label="Download Paper", file_name="Machine Learning Doppler-Tolerant One-Bit Radar Detectors.pdf", data=file, mime="application/pdf", help="Machine Learning Doppler-Tolerant One-Bit Radar Detectors")
        st.link_button(help="IET Online Library",icon=":material/book:", label="Read Online", url="https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/rsn2.70011?af=R")

st.divider()
# Education history
st.title(":material/School: Education", anchor="education")
st.header("New Jersey Institute of Technology", anchor=False)
col_1, col_2 = st.columns(2)
with col_1:
    st.subheader("May 2023", anchor=False)
    st.write("BS In Computer Engineering")
with col_2:
    st.subheader("May 2024", anchor=False)
    st.write("MS In Computer Engineering")


st.divider()
# Skills list
st.header(":material/Build_Circle: Skills", anchor="skills")
st.write("**Programming:** Python, C++, MATLAB, Java")
st.write("**IT Related Software:** Active Directory, Intune, Sophos")
st.write("**Hands on:** On-Site & Remote IT Assistance, Radio Equipment, Spectrum Analysis")

st.divider()
# Certifications list
st.header(":material/Verified: Certifications", anchor="certifications")
st.write("Currently In Progress")

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