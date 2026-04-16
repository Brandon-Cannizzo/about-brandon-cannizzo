import streamlit as st


main_page = st.Page("1_main_page.py", title="About Me")
contact_form = st.Page("2_contact_form.py", title="Contact Form")
pg = st.navigation([main_page, contact_form], position="top")
pg.run()