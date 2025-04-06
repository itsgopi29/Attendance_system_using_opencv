import streamlit as st
import pandas as pd
import time 
from  datetime import datetime

ts=time.time()
date=datetime.fromtimestamp(ts).strftime("%d-%m-%y")
timestamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S")

from streamlit_autorefresh import st_autorefresh

count = st_autorefresh(interval=2000,limit=100, key="fizzbuzzcounter")
if count == 0:
    st.write("Count is zero")
elif count %  3 == 0 and count % 5 == 0:
    st.write("FixxBuzz")
elif count % 3 == 0:
    st.write("FizzBuzz")
elif count % 5 == 0:
    st.write("Buzz")
else:
    st.write(f"count: {count}")
df=pd.read_csv("Attendance/Attendance_" + date + ".csv")

st.dataframe(df.style.highlight_max(axis=0))