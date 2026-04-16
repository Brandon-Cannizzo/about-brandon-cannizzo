import streamlit as st

st.title("Contact Me!")


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