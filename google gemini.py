#this is a program which takes input and give a output with and also
# voice it is made with google ai api and python and pyttsx3 packege.
import os
import google.generativeai as genai
import pyttsx3
print("hello world")

# api_key
api_key = "AIzaSyCTLC2WYTSlgh8nUn8D0BCTj_jOXnb4PnI"

# Configure the generative AI client
genai.configure(api_key=api_key)

# Instantiate the generative model (assuming this is the correct method)
model = genai.GenerativeModel('gemini-1.5-flash')

# Define the prompt for content generation
prompt = input("Enter Your Text: ")
print("\ninitillizing...\n")
# Generate content based on the prompt
response = model.generate_content(prompt)

# Print the generated content
print("\n",response.text)

# text to speech
engine = pyttsx3.init()
engine.say(response.text)
engine.runAndWait()

# write the text in a new file "text.md"
with open("text.md","w") as f:
    f.write(response.trxt)
