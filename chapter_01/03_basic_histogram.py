import streamlit as st
import matplotlib.pyplot as pyplot
import numpy as np
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.error("The OPENAI_API_KEY environment variable is not set. Please add it to your .env file.")
    st.stop()

openai = OpenAI(api_key=openai_api_key)
nums = np.random.normal(1, 1, size=5000)
figure, subplot = pyplot.subplots()

bins = st.number_input("Number of bins", min_value=1, max_value=100)
subplot.hist(nums, bins=bins)
st.pyplot(figure)