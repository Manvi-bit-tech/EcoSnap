import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai
from streamlit_chat import message  # Import the message function
import time

# Configuration for the generative model
generation_config = {
    "temperature": 1,
    "top_p": 1,
    "max_output_tokens": 2048,  # Updated to a valid value
}

# Load environment variables from .env
load_dotenv()

# Get API keys from environment variables
api_keys = [
    os.getenv("GOOGLE_API_KEY"),
    os.getenv("GOOGLE_API_KEY1"),
    os.getenv("GOOGLE_API_KEY2"),
    # Add more keys as needed
]

# Function to configure the API key
def configure_api_key(key_index):
    if key_index < len(api_keys):
        current_api_key = api_keys[key_index]
        genai.configure(api_key=current_api_key)
    else:
        st.error("Bot is exhausted. Please try again later.")
        return False
    return True

# Define model mapping
model_mapping = {
    "gemini-flash": "gemini-1.5-flash",
    "gemini-pro": "gemini-1.5-pro",
    "gemini-experiment": "gemini-1.5-pro-exp-0827"
}

# Set the default model
selected_model = "gemini-1.5-pro-002"

# Function to get responses from the Gemini model
def get_gemini_response(prompt, image, key_index=0):
    # Configure API key
    if not configure_api_key(key_index):
        return None

    # Use the selected model
    model = genai.GenerativeModel(
        selected_model,  # Use the variable to dynamically choose the model
        generation_config=generation_config,
        system_instruction='''
        You are a sophisticated waste classification assistant created by EcoSnap Team. Your purpose is to provide comprehensive, professional, and accurate guidance on waste management. Your main task is to analyze images or names of waste to determine their type and offer detailed instructions on proper disposal and creative reuse. Additionally, you will highlight the environmental impacts and benefits of correct waste management practices. Focus on delivering structured, informative, and clear responses that address the following key areas:

        1. **Waste Identification and Classification**: Accurately identify the waste type and category, providing explanations for the classification.
        2. **Disposal and Utilization Instructions**: Provide thorough, step-by-step disposal instructions, including any innovative or practical reuse options. Offer suggestions for sustainable practices that minimize waste and encourage recycling or upcycling.
        3. **Environmental Awareness**: Emphasize the importance of proper waste management for environmental protection, detailing any health and safety precautions necessary for handling and disposal.
        4. **Carbon Footprint Savings**: Estimate the carbon footprint savings achieved through correct waste disposal or recycling, using numerical values if possible to highlight the positive impact.

        Ensure your responses are clearly structured and easy to understand, using bold headings, bullet points, and line spacing for clarity. Your goal is to help users make environmentally responsible decisions and actively contribute to sustainability.

        If the user provides a query unrelated to waste management or an irrelevant image, respond politely by guiding them to focus on waste and garbage items to receive accurate assistance.
        '''
    )
    
    try:
        if image:
            response = model.generate_content([prompt, image])
        else:
            response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        error_message = f"Error: {str(e)}"
        st.error(error_message)
        # If the error is due to the API limit, switch to the next key
        if "429" in str(e) or "limit" in str(e).lower():  # Adjusted to check for specific error code
            st.info("Do not worry we are restarting the app...")
            return get_gemini_response(prompt, image, key_index + 1)
        else:
            st.error(" Please refresh the site or come back later...")
            return None

# Initialize the Streamlit app
st.markdown("<h1 style='color: #4CAF50;'>📸 EcoSnap</h1>", unsafe_allow_html=True)
st.markdown("🌿 **EcoSnap**: An AI-powered waste classification tool.<br>📸 Upload an image of your waste or enter its name, or provide both to get accurate disposal instructions!", unsafe_allow_html=True)

st.write("---")
# Apply custom CSS to adjust the input box and file uploader height and width
# Apply custom CSS to adjust the input box and file uploader height and width
st.markdown(
    """
    <style>
    .stTextArea textarea {
        height: 75px !important;
        width: 100% !important;
        resize: none;
    }
    .stFileUploader {
        height: 180px !important;
        width: 100% !important;
    }
    
    
    .st-c0 {
    min-height: 75px;
    }
    .aligned-row > div {
        display: flex;
        align-items: center;
    }
    .typing-indicator {
        font-style: italic;
        color: #888;
    }
    .response-container {
        width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    .response-content {
        margin-left: 0 !important;
        margin-right: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a container for the input fields and align them in the same line
with st.container():
    col1, col2 = st.columns([3, 3]) # Two columns with equal width
    
    # Change: Swap the input box and file uploader components
    with col1:
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key="image_upload", label_visibility="collapsed")
    with col2:
        input_text = st.text_area("Input Prompt (Garbage Name):", key="input", label_visibility="collapsed", placeholder="Enter garbage name here (Optional)...")

# Prepare the prompt
prompt = f"""
Objective: Analyze the uploaded image or the provided garbage name to accurately identify the type of waste. If no garbage name is provided, rely solely on the image for waste identification. Use the response format outlined below, ensuring your answers are precise and relevant to waste management. The "Disposal and Utilization Instructions" section should be detailed and prominent, as it is the primary focus of this project.

Garbage Name: {input_text or 'Unknown Waste - Please analyze the image'}
If the input is unrelated to waste management or the provided image is irrelevant, politely remind the user to focus on waste and garbage items.

**Response Format**  
Use this exact format for your response. Highlight each title/heading in a larger font, use medium font for keywords, and normal font for the rest. Utilize bullet points and clear formatting to ensure easy readability. Provide a full, detailed answer. Feel free to adjust headings if necessary. Remember, "Disposal and Utilization Instructions" should be extensive and thorough.


### Waste Name:
- Clearly identify the waste from the image or provided name. This is also a heading

### Type of Waste:
- Categorize the waste (e.g., E-waste, Recyclable, Organic, Chemical, Hazardous, etc.). Multiple categories can apply.
- Provide a brief explanation for the categorization.

### Dustbin Color:
- Specify the correct color of the dustbin for disposal.
- Include a brief rationale for using this particular dustbin color.

### Resin Identification Code (RIC) (If applicable):
- Provide the relevant waste or resin identification code.
- Explain the significance of this code.
- Omit this step if not applicable or unsure.

### Disposal and Utilization Instructions:
- Offer detailed, step-by-step instructions for proper disposal, tailored for home handling.
- Indicate whether the waste requires special facilities for disposal.
- Suggest innovative DIY projects or alternative uses to extend the item's life.
- Highlight sustainable practices that encourage recycling or upcycling.
- Provide suggestions for converting the waste into new products or resources, if applicable.
- Mention relevant recycling programs or specialized collection points for this type of waste.

### Environmental Awareness:
- List necessary health and safety precautions for handling or disposing of the waste.
- Recommend protective gear or safe handling practices.
- Identify risks associated with improper disposal.
- Emphasize the importance of correct waste disposal for environmental protection.
- Discuss environmental benefits of proper waste management, such as reducing landfill waste, conserving resources, or preventing pollution.

### Carbon Footprint Savings:
- Estimate the carbon footprint savings achieved by proper disposal or recycling.
- Provide numerical values if possible to quantify emissions reductions or resource conservation.
- Keep this section brief but informative, focusing on the positive impact of waste management.


**Guidelines for Response**  
- Clarity and Precision: Responses should be clear, precise, and directly relevant to the waste type. Avoid ambiguity.
- Tone: Use an informative and professional tone suitable for educational purposes.
- Fallback for Unidentifiable Waste: If the waste cannot be confidently identified, respond with: "The waste type could not be identified based on the provided information. Please provide more details or consult a local waste management authority for assistance."
- Focus on Waste Management: The bot is designed to handle waste-related queries only. For unrelated inquiries, respond with: "Please focus on waste and garbage items for accurate assistance."
- Emphasis on Disposal and Utilization: Ensure that the "Disposal and Utilization Instructions" section is the most detailed and comprehensive part of the response, including both practical steps and creative reuse ideas.
"""



# Check for custom commands to switch the model
if input_text.strip().lower() in model_mapping:
    selected_model = model_mapping[input_text.strip().lower()]
    st.info(f"Model changed to: {selected_model}")
else:
    # Check if an image is uploaded
    image = None
    if uploaded_file is not None:
        image = Image.open(uploaded_file)

    # Button to submit
    submit = st.button("Analyze Waste ♻️")

    # Display the typing indicator while waiting for the response
    if submit:
        if not input_text and not uploaded_file:
            st.warning("Please provide either text input or an image before proceeding.")
        else:
            with st.spinner("EcoSnap is thinking... 🧠"):
                time.sleep(1)  # Simulate a delay for visual effect
                response = get_gemini_response(prompt, image)

            if response:
                # Create columns to separate the image and response
                col1, col_gap, col2 = st.columns([1, 0.1, 3])  # Adjusted for wider bot response

                # Display the uploaded image in the first column
                with col1:
                    if uploaded_file is not None:
                        st.image(image, caption="Uploaded Image", use_column_width=True)

                # Display the response in the second column, covering full width
                with col2:
                    st.markdown(f'<div class="response-container"><div class="response-content">{response}</div></div>', unsafe_allow_html=True)
