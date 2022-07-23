import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Visualização do gapminder')


df = px.data.gapminder()
fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)
fig.show()