import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = "OPENAI_API_KEY"

# Welcome message
st.title("Intelligent Chatbot")
st.write("Welcome to the Intelligent Chatbot! Type your message below.")

# User input
user_input = st.text_input("You:", "")

if user_input:
    # Generate a response using OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can experiment with different engines
        prompt=user_input,
        max_tokens=50  # You can adjust the response length
    )
    
    # Display the bot's response
    bot_response = response.choices[0].text.strip()
    st.text("ChatBot:")
    st.write(bot_response)
