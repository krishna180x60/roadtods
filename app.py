from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

#for emojis-> [ https://webfx.com/tools/emoji-cheat-sheet/ ]😼
st.set_page_config(page_title='Road to ds',page_icon=":😼:",layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css('style/style.css')

#---load assets---
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_ngzwzxib.json")
img_contact_form= Image.open("image/mcafee.png")
img_lottie_animation = Image.open("image/mcafee2.png")
img_contact_form2= Image.open("image/pubg.png")
#----header section----
with st.container():
     st.subheader(" Hi, I am Nikhil :🙃: ")
     st.title("A Data Scientist From India")
     st.write("I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings.")
     st.write("[learn more >](https://gamegamesimsim.netlify.app/)")

#---what i do----
with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("What I want to do")
        st.write("##")
        st.write("""I want to become data scientist. i am not become data scientist yet.
        -well this year i will pass out 12th then i will take admission in university to
        become a data scientist
        """)
        st.write("[my other projects >](https://checkspot4.wordpress.com/)")
    with right_column:
        st_lottie(lottie_coding,height=300,key="coding")
    
#---projects--
with st.container():
    st.write("---")
    st.header("My Youtube Videos ▶")
    st.write("##")
    image_column,text_column=st.columns((1,2))
    with image_column:
        #insert image
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Activate MCAfee antivirus for life time.")
        st.write(
            '''
             you can access the life time premium anti virus for free..
             also subscribe my youtube channel for more content like this. :)
            '''
        )
        st.markdown("[watch video...](https://youtu.be/mwB0PJKMtT8)")

with st.container():
    image_column,text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form2)
    with text_column:
        st.subheader("My funny pubg mobile game play watch and have fun.")
        st.write(
            '''
             I Love to play online multiplayer battleground games like pubg,cod,apex,fortinite and more
             before my passion i was a true gamer :)
            '''
        )
        st.markdown("[watch video...](https://youtu.be/wWR4rKhI_Hs)")
        
#---contact---
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    #documentation https://formsubmit.co/  !change email address
    contact_form= '''
    <form action="https://formsubmit.co/divinexdeo2003@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder= "Your Name" required>
        <input type="email" name="email" placeholder= "Your Email" required>
        <textarea name="message" placeholder= "Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    '''
    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()
