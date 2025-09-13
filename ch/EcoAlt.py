import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

# Load environment variables from .env file
load_dotenv()

model="gemma2-9b-it"
#"llama-3.1-8b-instant", "llama-3.1-70b-versatile", "gemma-7b-it", "gemma2-9b-it"

# Get the API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize the Groq client with the API key
client = Groq(api_key=GROQ_API_KEY)


# Streamlit page title
st.markdown("<h1 style='color: rgb(106, 90, 205);'>🌱 EcoAlt</h1>", unsafe_allow_html=True)
st.markdown("🌱 **EcoAlt**: Discover eco-friendly alternatives for everyday products.<br>🔍 Simply enter the name of a product, and EcoAlt will suggest sustainable options for a greener lifestyle!",unsafe_allow_html=True)
st.write("---")

input_prompt_template = '''
List eco-friendly alternatives for the following item: {item_name}. 
For each alternative, provide a bullet point with a concise description that highlights its sustainability and environmental benefits.
Use the appropriate emojis.
Response Guidelines:
1. Include 6-10 specific and relevant alternatives.
2. Explain why each alternative is sustainable and environmentally friendly.
3. Describe the materials, production methods, or practices that contribute to its sustainability.
4. Note if the alternative is reusable, recyclable, or has a low environmental impact.
5. Highlight specific benefits such as reduced carbon footprint, biodegradability, or non-toxicity.
6. Ensure each alternative is practical and implementable for the average user.
Do not provide irrelevant or unsure names.

Do not respond if the input is unclear or not a valid item name. Focus on providing accurate and actionable eco-friendly suggestions.
'''

# Use st.chat_input for user input
user_input = st.chat_input("Enter the name of the item:")

# Check if user has entered an item name
if user_input:
    # Format the input prompt with the item name
    input_prompt = input_prompt_template.format(item_name=user_input)

    # Send the formatted prompt to the LLM and get a response
    messages = [
       {"role": "system", "content": '''
You are an eco-friendly assistant specialized in suggesting sustainable alternatives to everyday items. Your responses should only address valid item names provided by the user and offer eco-friendly alternatives in bullet points. Each alternative should include a brief description to help the user understand why it's a sustainable choice.

Guidelines:
1. If the user provides a valid item name, respond with a list of accurate and relevant eco-friendly alternatives, along with short descriptions for each option.
2. If the user input is unclear, irrelevant, or does not seem to be a valid item name, respond politely by guiding the user to specify a particular item name for which they seek eco-friendly alternatives.
3. Keep responses focused and concise, ensuring that the information is helpful and promotes environmentally conscious choices.
4. Avoid responding to inputs that do not relate to items or do not require eco-friendly alternatives, maintaining a strict focus on the topic of sustainability.
5. Provide as many names as you can.
Remember, your goal is to assist users in making informed, environmentally friendly choices by providing clear, actionable suggestions.
'''},

        {"role": "user", "content": input_prompt}
    ]

    response = client.chat.completions.create(
        model=model,
        temperature=1,
        max_tokens=8000,
        top_p=1,
        messages=messages
    )

    # Get the assistant's response
    assistant_response = response.choices[0].message.content

    # Display the bot's response using st.chat_message

    if assistant_response.strip():
        with st.chat_message("user"):
            st.markdown(assistant_response)
