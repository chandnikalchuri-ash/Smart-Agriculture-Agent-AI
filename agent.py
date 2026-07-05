import os
import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image 

# Step 1: Setup and API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# New: Extracting the current date, time, month, and year using Python.
now = datetime.datetime.now()
current_date = now.strftime("%d %B %Y")
current_time = now.strftime("%I:%M %p")
current_day = now.strftime("%A")
current_month = now.strftime("%B")
current_year = now.strftime("%Y")

# Step 2: DATA SKILL - Read the CSV file
def get_crop_data():
    with open('crop_data.csv', 'r') as file:
        return file.read()

crop_database = get_crop_data()

# Step 3: RULES AND SECURITY
agent_instruction = f"""
You are an expert smart agriculture agent.
You have this database of soil and crop data:
{crop_database}

CURRENT CONTEXT (DO NOT ASK THE USER FOR THESE DETAILS):
- Today's Date: {current_date}
- Day: {current_day}
- Time: {current_time}
- Current Month: {current_month}
- Current Year: {current_year}

Rule 1 (Data): If the farmer's query relates to this database (such as asking for crop recommendations based on soil and weather conditions), analyze the database and provide an answer.
Rule 2 (General Knowledge & Context): If a farmer asks which crop to grow in ANY specific state or region of India, use your vast general knowledge about Indian states, their soil, and climate. COMBINE this with the 'Current Month' provided above to give a direct, highly accurate crop suggestion. NEVER ask the user what month or season it is. Give them a direct and impressive answer.
Rule 3 (Security): You will strictly talk only about agriculture, farming, and crops. Reject other topics (movies, politics, etc.).
Rule 4 (Language): It is not mandatory to reply only in Hindi. Try to respond in the same language the farmer is using. If you do not know that language, then reply in English.
Rule 5 (Image Analysis): If the user asks to check a photo, identify the disease of the plant or leaf in the image and suggest the correct remedy.
"""

# Starting the agent's chat session
chat = client.chats.create(
    model='gemini-2.5-flash',
    config=types.GenerateContentConfig(
        system_instruction=agent_instruction,
        temperature=0.2 
    )
)

print("=========================================")
print("🌾 The Smart Agriculture Agent has been activated. 🌾")
print("1. Text Chat: Write your question below to speak with an agent.")
print("2. Photo Check: Type 'photo' to check the plant image (leaf.jpg).")
print("3. Exit: Type 'exit' to close.")
print("=========================================\n")

# Step 4: CHAT LOOP (To keep the conversation going)
while True:
    user_input = input("Kisan (Aap): ")
    
    if user_input.lower() == 'exit':
        print("Agent: Goodbye! Best wishes for farming.")
        break
        
    # Photo check karne ka logic
    if user_input.lower() == 'photo':
        try:
            print("The agent is checking the photo...")
            img = Image.open('leaf.jpg')
            photo_prompt = "Identify the disease affecting this plant/leaf and suggest a remedy."
            response = chat.send_message([img, photo_prompt])
            print(f"Agent: {response.text}\n")
        except FileNotFoundError:
            print("Agent: I could not find 'leaf.jpg'. Please download an image and place it in the folder first.\n")
        continue 
        
    print("The agent is thinking...")
    response = chat.send_message(user_input)
    print(f"Agent: {response.text}\n")

