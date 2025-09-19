# import streamlit as st
# import google.generativeai as genai
# import requests
# import os

# from dotenv import load_dotenv  # <-- Add this line

# load_dotenv()  # <-- Add this line to load .env variables


# st.title("AI Content Generator")

# # Load Gemini API Key from environment variable
# gemini_api_key = os.getenv("GEMINI_API_KEY")

# if not gemini_api_key:
#     st.error("Please set your GEMINI_API_KEY environment variable to use AI features. For example, export GEMINI_API_KEY=your_key_here")

# # Function to configure Gemini if key is provided
# def get_gemini_model():
#     if gemini_api_key:
#         genai.configure(api_key=gemini_api_key)
#         return genai.GenerativeModel('gemini-1.5-flash')
#     return None

# # Function to fetch meme templates from Memegen.link (cached)
# @st.cache_data
# def get_meme_templates():
#     response = requests.get("https://api.memegen.link/templates/")
#     if response.status_code == 200:
#         return response.json()
#     else:
#         st.error("Failed to fetch meme templates from Memegen.link.")
#         return []

# # Tabs for features
# tab1, tab2, tab3, tab4 = st.tabs([
#     "Content Generation",
#     "Niche & Keyword Research",
#     "Meme Generation",
#     "YouTube SEO Metadata"
# ])

# # Tab 1: Content Generation for Social Media
# with tab1:
#     st.header("Content Generation for Social Media")
#     platforms = ["Facebook", "Instagram", "TikTok", "YouTube"]
#     selected_platform = st.selectbox("Select Platform", platforms)
#     prompt = st.text_area("Enter your content prompt or idea")
#     if st.button("Generate Content"):
#         model = get_gemini_model()
#         if model and prompt:
#             with st.spinner("Generating content..."):
#                 response = model.generate_content(
#                     f"Generate engaging content tailored for {selected_platform} based on this prompt: {prompt}. "
#                     "Keep it concise and optimized for the platform."
#                 )
#                 st.subheader("Generated Content:")
#                 st.write(response.text)
#         elif not prompt:
#             st.error("Please enter a prompt.")

# # Tab 2: Niche and Keyword Research for SEO
# with tab2:
#     st.header("Niche and Keyword Research for SEO")
#     topic = st.text_input("Enter a topic or niche idea")
#     if st.button("Research Niches & Keywords"):
#         model = get_gemini_model()
#         if model and topic:
#             with st.spinner("Researching..."):
#                 response = model.generate_content(
#                     f"Conduct niche research and suggest SEO-optimized keywords for the topic: {topic}. "
#                     "Include 5-10 niche ideas, top keywords with search volume estimates (low/medium/high), "
#                     "and long-tail keyword suggestions."
#                 )
#                 st.subheader("Research Results:")
#                 st.write(response.text)
#         elif not topic:
#             st.error("Please enter a topic.")

# # ...existing code...

# with tab3:
#     st.header("Meme Generation")
#     # st.info("Using Memegen.link, a free API alternative to Imgflip. No authentication required. For special characters (e.g., ? as ~q), see docs at https://memegen.link.")
#     templates = get_meme_templates()
#     if templates:
#         template_names = [template['name'] for template in templates]
#         selected_template = st.selectbox("Select Meme Template", template_names)
#         top_text = st.text_input("Top Text (optional)")
#         bottom_text = st.text_input("Bottom Text (optional)")
#         if st.button("Generate Meme"):
#             if selected_template:
#                 template_id = next((t['id'] for t in templates if t['name'] == selected_template), None)
#                 if template_id:
#                     # Replace spaces with underscores and encode special characters
#                     def format_text(text, default):
#                         if not text:
#                             return default
#                         return (
#                             text.replace("-", "--")
#                                 .replace("_", "__")
#                                 .replace(" ", "_")
#                                 .replace("?", "~q")
#                                 .replace("%", "~p")
#                                 .replace("#", "~h")
#                                 .replace("/", "~s")
#                                 .replace("\"", "''")
#                         )
#                     # Use default text if not provided
#                     top_text_formatted = format_text(top_text, "Top_Text")
#                     bottom_text_formatted = format_text(bottom_text, "Bottom_Text")
#                     meme_url = f"https://api.memegen.link/images/{template_id}/{top_text_formatted}/{bottom_text_formatted}.png"
#                     st.subheader("Generated Meme:")
#                     st.image(meme_url)
#                     st.write(f"[View Meme]({meme_url})")
#                     st.write(f"**Debug URL:** {meme_url}")  # Show the URL for debugging
#                 else:
#                     st.error("Template ID not found.")
#             else:
#                 st.error("Please select a meme template.")
# # ...existing code...

# # Tab 4: Generate SEO Metadata for YouTube Videos
# with tab4:
#     st.header("YouTube SEO Metadata Generator")
#     rough_title = st.text_input("Rough Video Title")
#     video_script = st.text_area("Video Script or Description Outline")
#     if st.button("Generate SEO Metadata"):
#         model = get_gemini_model()
#         if model and rough_title and video_script:
#             with st.spinner("Generating metadata..."):
#                 response = model.generate_content(
#                     f"Generate SEO-optimized YouTube metadata based on this rough title: '{rough_title}' "
#                     f"and video script: '{video_script}'. Include: "
#                     "1. Optimized Title (under 60 characters, keyword-rich). "
#                     "2. Detailed Description (150-200 words, with timestamps if applicable, keywords, calls to action). "
#                     "3. 10-15 Tags (mix of broad and specific keywords)."
#                 )
#                 st.subheader("Generated Metadata:")
#                 st.write(response.text)
#         elif not rough_title or not video_script:
#             st.error("Please provide both a rough title and video script.")


import streamlit as st
import google.generativeai as genai
import requests
import os

from dotenv import load_dotenv

load_dotenv()

st.title("AI Content Generator")

# Load Gemini API Key from environment variable
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    st.error("Please set your GEMINI_API_KEY environment variable to use AI features. For example, export GEMINI_API_KEY=your_key_here")

def get_gemini_model():
    if gemini_api_key:
        genai.configure(api_key=gemini_api_key)
        return genai.GenerativeModel('gemini-1.5-flash')
    return None

@st.cache_data
def get_meme_templates():
    response = requests.get("https://api.memegen.link/templates/")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch meme templates from Memegen.link.")
        return []

# Sidebar navigation
st.sidebar.title("Features")
feature = st.sidebar.radio(
    "Select a feature:",
    [
        "Content Generation",
        "Niche & Keyword Research",
        "Meme Generation",
        "YouTube SEO Metadata"
    ]
)

if feature == "Content Generation":
    st.header("Content Generation for Social Media")
    platforms = ["Facebook", "Instagram", "TikTok", "YouTube"]
    selected_platform = st.selectbox("Select Platform", platforms)
    prompt = st.text_area("Enter your content prompt or idea")
    if st.button("Generate Content"):
        model = get_gemini_model()
        if model and prompt:
            with st.spinner("Generating content..."):
                response = model.generate_content(
                    f"Generate engaging content tailored for {selected_platform} based on this prompt: {prompt}. "
                    "Keep it concise and optimized for the platform."
                )
                st.subheader("Generated Content:")
                st.write(response.text)
        elif not prompt:
            st.error("Please enter a prompt.")

elif feature == "Niche & Keyword Research":
    st.header("Niche and Keyword Research for SEO")
    topic = st.text_input("Enter a topic or niche idea")
    if st.button("Research Niches & Keywords"):
        model = get_gemini_model()
        if model and topic:
            with st.spinner("Researching..."):
                response = model.generate_content(
                    f"Conduct niche research and suggest SEO-optimized keywords for the topic: {topic}. "
                    "Include 5-10 niche ideas, top keywords with search volume estimates (low/medium/high), "
                    "and long-tail keyword suggestions."
                )
                st.subheader("Research Results:")
                st.write(response.text)
        elif not topic:
            st.error("Please enter a topic.")

elif feature == "Meme Generation":
    st.header("Meme Generation")
    # st.info("Using Memegen.link, a free API alternative to Imgflip. No authentication required. For special characters (e.g., ? as ~q), see docs at https://memegen.link.")
    templates = get_meme_templates()
    if templates:
        template_names = [template['name'] for template in templates]
        selected_template = st.selectbox("Select Meme Template", template_names)
        top_text = st.text_input("Top Text (optional)")
        bottom_text = st.text_input("Bottom Text (optional)")
        if st.button("Generate Meme"):
            if selected_template:
                template_id = next((t['id'] for t in templates if t['name'] == selected_template), None)
                if template_id:
                    def format_text(text, default):
                        if not text:
                            return default
                        return (
                            text.replace("-", "--")
                                .replace("_", "__")
                                .replace(" ", "_")
                                .replace("?", "~q")
                                .replace("%", "~p")
                                .replace("#", "~h")
                                .replace("/", "~s")
                                .replace("\"", "''")
                        )
                    top_text_formatted = format_text(top_text, "Top_Text")
                    bottom_text_formatted = format_text(bottom_text, "Bottom_Text")
                    meme_url = f"https://api.memegen.link/images/{template_id}/{top_text_formatted}/{bottom_text_formatted}.png"
                    st.subheader("Generated Meme:")
                    st.image(meme_url)
                    st.write(f"[View Meme]({meme_url})")
                    st.write(f"**Debug URL:** {meme_url}")
                else:
                    st.error("Template ID not found.")
            else:
                st.error("Please select a meme template.")

elif feature == "YouTube SEO Metadata":
    st.header("YouTube SEO Metadata Generator")
    rough_title = st.text_input("Rough Video Title")
    video_script = st.text_area("Video Script or Description Outline")
    if st.button("Generate SEO Metadata"):
        model = get_gemini_model()
        if model and rough_title and video_script:
            with st.spinner("Generating metadata..."):
                response = model.generate_content(
                    f"Generate SEO-optimized YouTube metadata based on this rough title: '{rough_title}' "
                    f"and video script: '{video_script}'. Include: "
                    "1. Optimized Title (under 60 characters, keyword-rich). "
                    "2. Detailed Description (150-200 words, with timestamps if applicable, keywords, calls to action). "
                    "3. 10-15 Tags (mix of broad and specific keywords)."
                )
                st.subheader("Generated Metadata:")
                st.write(response.text)
        elif not rough_title or not video_script:
            st.error("Please provide both a rough title and video script.")