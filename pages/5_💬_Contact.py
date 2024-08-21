#Importing Libraries
import streamlit as st
import streamlit.components.v1 as components

#setting page configuration by enitializing that this is the contact page, setting the emoji to the "chat bubble" emoji, and making the page a wide format 
st.set_page_config(page_title="Contact", page_icon=":speech_balloon:", layout='wide')

#Inserting Google Analytics tracking ID
GA_TRACKING_CODE = """
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-EJ8WRG15YL"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-EJ8WRG15YL');
</script>
"""

st.markdown(f'<head>{GA_TRACKING_CODE}</head>', unsafe_allow_html=True)

#Creating header for the contact page
st.header(":mailbox: Report an Issue, Give Suggestions, or Get In Touch With Me!")
#Using markdown to tell the user my name, email address, and telling them to submit message below
st.markdown('##### Ryan Kennedy: Developer of Crawford County Food Insecurity Dashboard')
st.markdown('##### Email: kennedy01@allegheny.edu')

st.markdown('### Submit message, suggestion, or feedback below straight to my email!')

#storing contact form template in a string. This contact template references a html template of how the form should look on the page
contact_form = """
<form action="https://formsubmit.co/kennedy01@allegheny.edu" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here"></textarea>
    <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

#defining function that calls the style.css file to format the functional submition form
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
