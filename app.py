# # import streamlit as st
# # import google.generativeai as genai
# # import requests
# # import os

# # from dotenv import load_dotenv  # <-- Add this line

# # load_dotenv()  # <-- Add this line to load .env variables


# # st.title("AI Content Generator")

# # # Load Gemini API Key from environment variable
# # gemini_api_key = os.getenv("GEMINI_API_KEY")

# # if not gemini_api_key:
# #     st.error("Please set your GEMINI_API_KEY environment variable to use AI features. For example, export GEMINI_API_KEY=your_key_here")

# # # Function to configure Gemini if key is provided
# # def get_gemini_model():
# #     if gemini_api_key:
# #         genai.configure(api_key=gemini_api_key)
# #         return genai.GenerativeModel('gemini-1.5-flash')
# #     return None

# # # Function to fetch meme templates from Memegen.link (cached)
# # @st.cache_data
# # def get_meme_templates():
# #     response = requests.get("https://api.memegen.link/templates/")
# #     if response.status_code == 200:
# #         return response.json()
# #     else:
# #         st.error("Failed to fetch meme templates from Memegen.link.")
# #         return []

# # # Tabs for features
# # tab1, tab2, tab3, tab4 = st.tabs([
# #     "Content Generation",
# #     "Niche & Keyword Research",
# #     "Meme Generation",
# #     "YouTube SEO Metadata"
# # ])

# # # Tab 1: Content Generation for Social Media
# # with tab1:
# #     st.header("Content Generation for Social Media")
# #     platforms = ["Facebook", "Instagram", "TikTok", "YouTube"]
# #     selected_platform = st.selectbox("Select Platform", platforms)
# #     prompt = st.text_area("Enter your content prompt or idea")
# #     if st.button("Generate Content"):
# #         model = get_gemini_model()
# #         if model and prompt:
# #             with st.spinner("Generating content..."):
# #                 response = model.generate_content(
# #                     f"Generate engaging content tailored for {selected_platform} based on this prompt: {prompt}. "
# #                     "Keep it concise and optimized for the platform."
# #                 )
# #                 st.subheader("Generated Content:")
# #                 st.write(response.text)
# #         elif not prompt:
# #             st.error("Please enter a prompt.")

# # # Tab 2: Niche and Keyword Research for SEO
# # with tab2:
# #     st.header("Niche and Keyword Research for SEO")
# #     topic = st.text_input("Enter a topic or niche idea")
# #     if st.button("Research Niches & Keywords"):
# #         model = get_gemini_model()
# #         if model and topic:
# #             with st.spinner("Researching..."):
# #                 response = model.generate_content(
# #                     f"Conduct niche research and suggest SEO-optimized keywords for the topic: {topic}. "
# #                     "Include 5-10 niche ideas, top keywords with search volume estimates (low/medium/high), "
# #                     "and long-tail keyword suggestions."
# #                 )
# #                 st.subheader("Research Results:")
# #                 st.write(response.text)
# #         elif not topic:
# #             st.error("Please enter a topic.")

# # # ...existing code...

# # with tab3:
# #     st.header("Meme Generation")
# #     # st.info("Using Memegen.link, a free API alternative to Imgflip. No authentication required. For special characters (e.g., ? as ~q), see docs at https://memegen.link.")
# #     templates = get_meme_templates()
# #     if templates:
# #         template_names = [template['name'] for template in templates]
# #         selected_template = st.selectbox("Select Meme Template", template_names)
# #         top_text = st.text_input("Top Text (optional)")
# #         bottom_text = st.text_input("Bottom Text (optional)")
# #         if st.button("Generate Meme"):
# #             if selected_template:
# #                 template_id = next((t['id'] for t in templates if t['name'] == selected_template), None)
# #                 if template_id:
# #                     # Replace spaces with underscores and encode special characters
# #                     def format_text(text, default):
# #                         if not text:
# #                             return default
# #                         return (
# #                             text.replace("-", "--")
# #                                 .replace("_", "__")
# #                                 .replace(" ", "_")
# #                                 .replace("?", "~q")
# #                                 .replace("%", "~p")
# #                                 .replace("#", "~h")
# #                                 .replace("/", "~s")
# #                                 .replace("\"", "''")
# #                         )
# #                     # Use default text if not provided
# #                     top_text_formatted = format_text(top_text, "Top_Text")
# #                     bottom_text_formatted = format_text(bottom_text, "Bottom_Text")
# #                     meme_url = f"https://api.memegen.link/images/{template_id}/{top_text_formatted}/{bottom_text_formatted}.png"
# #                     st.subheader("Generated Meme:")
# #                     st.image(meme_url)
# #                     st.write(f"[View Meme]({meme_url})")
# #                     st.write(f"**Debug URL:** {meme_url}")  # Show the URL for debugging
# #                 else:
# #                     st.error("Template ID not found.")
# #             else:
# #                 st.error("Please select a meme template.")
# # # ...existing code...

# # # Tab 4: Generate SEO Metadata for YouTube Videos
# # with tab4:
# #     st.header("YouTube SEO Metadata Generator")
# #     rough_title = st.text_input("Rough Video Title")
# #     video_script = st.text_area("Video Script or Description Outline")
# #     if st.button("Generate SEO Metadata"):
# #         model = get_gemini_model()
# #         if model and rough_title and video_script:
# #             with st.spinner("Generating metadata..."):
# #                 response = model.generate_content(
# #                     f"Generate SEO-optimized YouTube metadata based on this rough title: '{rough_title}' "
# #                     f"and video script: '{video_script}'. Include: "
# #                     "1. Optimized Title (under 60 characters, keyword-rich). "
# #                     "2. Detailed Description (150-200 words, with timestamps if applicable, keywords, calls to action). "
# #                     "3. 10-15 Tags (mix of broad and specific keywords)."
# #                 )
# #                 st.subheader("Generated Metadata:")
# #                 st.write(response.text)
# #         elif not rough_title or not video_script:
# #             st.error("Please provide both a rough title and video script.")


# import streamlit as st
# import google.generativeai as genai
# import requests
# import os

# from dotenv import load_dotenv

# load_dotenv()

# st.title("AI Content Generator")

# # Load Gemini API Key from environment variable
# gemini_api_key = os.getenv("GEMINI_API_KEY")

# if not gemini_api_key:
#     st.error("Please set your GEMINI_API_KEY environment variable to use AI features. For example, export GEMINI_API_KEY=your_key_here")

# def get_gemini_model():
#     if gemini_api_key:
#         genai.configure(api_key=gemini_api_key)
#         return genai.GenerativeModel('gemini-1.5-flash')
#     return None

# @st.cache_data
# def get_meme_templates():
#     response = requests.get("https://api.memegen.link/templates/")
#     if response.status_code == 200:
#         return response.json()
#     else:
#         st.error("Failed to fetch meme templates from Memegen.link.")
#         return []

# # Sidebar navigation
# st.sidebar.title("Features")
# feature = st.sidebar.radio(
#     "Select a feature:",
#     [
#         "Content Generation",
#         "Niche & Keyword Research",
#         "Meme Generation",
#         "YouTube SEO Metadata"
#     ]
# )

# if feature == "Content Generation":
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

# elif feature == "Niche & Keyword Research":
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

# elif feature == "Meme Generation":
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
#                     top_text_formatted = format_text(top_text, "Top_Text")
#                     bottom_text_formatted = format_text(bottom_text, "Bottom_Text")
#                     meme_url = f"https://api.memegen.link/images/{template_id}/{top_text_formatted}/{bottom_text_formatted}.png"
#                     st.subheader("Generated Meme:")
#                     st.image(meme_url)
#                     st.write(f"[View Meme]({meme_url})")
#                     st.write(f"**Debug URL:** {meme_url}")
#                 else:
#                     st.error("Template ID not found.")
#             else:
#                 st.error("Please select a meme template.")

# elif feature == "YouTube SEO Metadata":
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
from pytrends.request import TrendReq

load_dotenv()

# Set Streamlit page config for better UI
st.set_page_config(
    page_title="AI Content Generator",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for a modern dark theme and better UI
st.markdown("""
    <style>
        body, .stApp {
            background-color: #181824;
            color: #f1f1f1;
        }
        .stButton>button {
            background-color: #ff4b4b;
            color: white;
            border-radius: 8px;
            font-weight: bold;
        }
        .stTextInput>div>input, .stTextArea>div>textarea, .stSelectbox>div>div>div>div {
            background-color: #232339;
            color: #f1f1f1;
            border-radius: 6px;
        }
        .stSidebar {
            background-color: #232339;
        }
        .stRadio > div {
            gap: 0.5rem;
        }
        .stMarkdown a {
            color: #ff4b4b;
        }
    </style>
""", unsafe_allow_html=True)

# 4. Sidebar branding and navigation
st.sidebar.markdown("""
<div style="text-align:center">
    <img src="https://img.icons8.com/color/96/000000/youtube-play.png" width="60"/>
    <h2 style="color:#ff4b4b;">Creator Toolkit</h2>
    <p style="font-size:15px;">Your all-in-one AI-powered content lab.<br>Generate, research, and optimize for every platform!</p>
    <hr>
</div>
""", unsafe_allow_html=True)

st.title("✨ AI Content Generator")

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
st.sidebar.title("🛠️ Features")
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
    st.header("📝 Content Generation for Social Media")
    platforms = ["Facebook", "Instagram", "TikTok", "YouTube"]
    selected_platform = st.selectbox("Select Platform", platforms)
    prompt = st.text_area("Enter your content prompt or idea")
    if st.button("Generate Content"):
        model = get_gemini_model()
        if model and prompt:
            with st.spinner("Generating content..."):
                response = model.generate_content(
                    f"Generate engaging, creative, and platform-optimized content for {selected_platform} based on this prompt: {prompt}. "
                    "Make it catchy, concise, and include a relevant emoji."
                )
                st.subheader("Generated Content:")
                st.success(response.text)
        elif not prompt:
            st.error("Please enter a prompt.")

elif feature == "Niche & Keyword Research":
    st.header("🔍 Niche and Keyword Research for SEO")
    topic = st.text_input("Enter a topic or niche idea")
    if st.button("Research Niches & Keywords"):
        model = get_gemini_model()
        if model and topic:
            with st.spinner("Researching..."):
                response = model.generate_content(
                    f"Conduct niche research and suggest SEO-optimized keywords for the topic: {topic}. "
                    "Include 5-10 niche ideas, top keywords with search volume estimates (low/medium/high), "
                    "and long-tail keyword suggestions. Present the results in a neat markdown table."
                )
                st.subheader("Research Results:")
                st.markdown(response.text)
        elif not topic:
            st.error("Please enter a topic.")

elif feature == "Meme Generation":
    st.header("😂 Meme Generation")
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
                    # If both fields are empty, use prompt engineering to generate fun meme text
                    if not top_text and not bottom_text:
                        model = get_gemini_model()
                        if model:
                            meme_prompt = (
                                f"Suggest a funny and relevant meme caption (top and bottom text) for the meme template '{selected_template}'. "
                                "Return your answer as two lines: first line for top text, second line for bottom text. Avoid special characters."
                            )
                            meme_response = model.generate_content(meme_prompt)
                            meme_lines = meme_response.text.strip().split('\n')
                            top_text = meme_lines[0] if len(meme_lines) > 0 else "When you see AI"
                            bottom_text = meme_lines[1] if len(meme_lines) > 1 else "And it actually works"
                    elif not top_text:
                        model = get_gemini_model()
                        if model:
                            meme_prompt = (
                                f"Suggest a witty top meme caption for the template '{selected_template}' given the bottom text: '{bottom_text}'. "
                                "Avoid special characters."
                            )
                            meme_response = model.generate_content(meme_prompt)
                            top_text = meme_response.text.strip().split('\n')[0]
                    elif not bottom_text:
                        model = get_gemini_model()
                        if model:
                            meme_prompt = (
                                f"Suggest a witty bottom meme caption for the template '{selected_template}' given the top text: '{top_text}'. "
                                "Avoid special characters."
                            )
                            meme_response = model.generate_content(meme_prompt)
                            bottom_text = meme_response.text.strip().split('\n')[0]

                    def format_text(text):
                        if not text:
                            return "_"
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
                    top_text_formatted = format_text(top_text)
                    bottom_text_formatted = format_text(bottom_text)
                    meme_url = f"https://api.memegen.link/images/{template_id}/{top_text_formatted}/{bottom_text_formatted}.png"
                    st.subheader("Generated Meme:")
                    st.image(meme_url, use_column_width=True)
                    st.markdown(f"[🔗 View Meme]({meme_url})")
                else:
                    st.error("Template ID not found.")
            else:
                st.error("Please select a meme template.")

elif feature == "YouTube SEO Metadata":
    st.header("🎬 YouTube SEO Metadata Generator")
    rough_title = st.text_input("Rough Video Title")
    video_script = st.text_area("Video Script or Description Outline")
    if st.button("Generate SEO Metadata"):
        model = get_gemini_model()
        if model and rough_title and video_script:
            with st.spinner("Generating metadata..."):
                response = model.generate_content(
                    f"Generate SEO-optimized YouTube metadata for the following video:\n"
                    f"Title: {rough_title}\n"
                    f"Script/Outline: {video_script}\n"
                    "Return the result in this markdown format with relevant emojis:\n\n"
                    "### 📢 Optimized Title\n"
                    "- (title here)\n\n"
                    "### 📝 Description\n"
                    "- (250-300 words, include keywords, calls to action, and use emojis)\n\n"
                    "### 🏷️ Tags\n"
                    "- tag1, tag2, tag3, ... (10-15 tags, comma separated)\n"
                )
                st.markdown(response.text)
        elif not rough_title or not video_script:
            st.error("Please provide both a rough title and video script.")