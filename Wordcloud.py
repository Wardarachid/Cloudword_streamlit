import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Ask the user for input text
user_input = st.text_area("Enter the words you want to display in the WordCloud:")

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(user_input)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()
#hide errors interpretations 
st.set_option('deprecation.showPyplotGlobalUse', False)