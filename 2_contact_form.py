import streamlit as st

st.title("Contact Me!")

# Contact Form
html_form = """
<form action="https://formsubmit.co/89c50d2258f5ec9fe7830f361aa775ef" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required style="width: 100%; margin-bottom: 10px;">
     <input type="email" name="email" placeholder="Your Email" required style="width: 100%; margin-bottom: 10px;">
     <textarea name="message" placeholder="Your Message" required style="width: 100%; margin-bottom: 10px;"></textarea>
     <button type="submit" style="background-color: #ff4b4b; color: white; border: none; padding: 10px 20px; border-radius: 5px;">Send</button>
</form>
"""

st.markdown(html_form, unsafe_allow_html=True)



st.space(size="xxlarge")
# Return button centered in the middle of the page
col1, col2, col3 = st.columns(3)
with col2:
     if st.button("Return To Main Page", type="tertiary", width="stretch"):
          st.switch_page("1_main_page.py")



