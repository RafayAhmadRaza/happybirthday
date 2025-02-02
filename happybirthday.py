import streamlit as st
import datetime
import time

unlock_time = datetime.datetime(2025,2,3,0,0)
current_time = datetime.datetime.now()


while current_time<unlock_time:
    st.session_state.clear()  
    
    remaining_time = unlock_time-current_time
    st.warning("This Page is locked until i say so 😎")

    days, seconds = divmod(remaining_time.total_seconds(),86400)
    hours,seconds = divmod(seconds,3600)
    minutes,seconds = divmod(seconds,60)

    st.write(f"⏳ Time remaining: {int(days)}d {int(hours)}h {int(minutes)}m {int(seconds)}s")
  
    time.sleep(1)
    current_time = datetime.datetime.now()


st.title("🎉 Happy Birthday! Rameesa! 🎂")

st.image("https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif")

st.write("Treat Khab Deni Ha? 🥳")

st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

if st.button("Click for a Surprise 🎊"):
    st.balloons()
    st.success("May this year bring you happiness and success! 🎂")

