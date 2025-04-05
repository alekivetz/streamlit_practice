import streamlit as st 
import pandas as pd 
import numpy as np 
import altair as alt 

st.header('st.write')

st.write('Hello *World*, :smile: **COOL**')
st.write("""
        * Bullet 1
         * Bullet 2
"""
)
st.write(5*10)

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)
st.write(df)

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c'
)
st.write(c)