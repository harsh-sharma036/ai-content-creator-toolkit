# ✨ AI Content Creator Toolkit

A powerful, all-in-one Streamlit app for content creators!  
Generate social media posts, research SEO keywords, create memes, craft YouTube SEO metadata, turn captions into AI art prompts, and even generate YouTube thumbnails using the latest AI models and APIs.

---

## 🚀 Features

### 1. **Content Generation for Social Media**
- Generate catchy, platform-optimized posts for Facebook, Instagram, TikTok, and YouTube.
- Powered by Google Gemini for creative, engaging content with relevant emojis.

### 2. **Niche & Keyword Research**
- Enter any topic or niche idea.
- Get trending keywords from Google Trends (via pytrends).
- Gemini combines trends with actionable SEO suggestions, niche ideas, long-tail keywords, and tips.
- Export results to CSV or DOCX.

### 3. **Meme Generation**
- Choose from dozens of meme templates.
- Enter your own top/bottom text, or let Gemini generate witty captions based on trends.
- Instantly generate memes using the Memegen.link API.

### 4. **YouTube SEO Metadata Generator**
- Input a rough video title and script/outline.
- Fetches trending YouTube keywords for your topic.
- Gemini generates an optimized title, detailed description, and 15–21 tags, all formatted in markdown with emojis.
- Copy metadata with one click.

### 5. **Caption-to-Image Prompt Generator**
- Turn any caption or idea into a detailed, creative prompt for AI art (MidJourney, Stable Diffusion, etc.).
- Gemini crafts vivid, style-aware prompts for stunning AI images.
- Copy prompts easily.

### 6. **YouTube Thumbnail Generator**
- Paste your YouTube metadata (title, description, tags).
- Gemini creates a concise, visually descriptive thumbnail prompt tailored to your video’s theme and comparison.
- Pollinations API generates a unique thumbnail image from the prompt.
- Download or copy the prompt and image.

---

## 🖥️ UI & User Experience

- Modern dark theme with custom CSS for a professional look.
- Sidebar navigation with branding and feature selection.
- All user inputs and outputs are preserved using Streamlit session state—switch between features without losing progress.
- Native copy-to-clipboard for all outputs.
- Download options for keyword research results.

---

## 🛠️ Setup Instructions

### 1. **Clone the Repository**
```bash
git clone https://github.com/harsh-036-sharma/ai-content-creator-toolkit.git
cd ai-content-creator-toolkit
```

### 2. **Install Dependencies**
```bash
pip install -r requirements.txt
```
If you don’t have a `requirements.txt`, install these:
```bash
pip install streamlit google-generativeai python-dotenv pytrends pandas python-docx requests
```

### 3. **Set Up Your Environment Variables**
- Create a `.env` file in the project root:
  ```
  GEMINI_API_KEY=your_gemini_api_key_here
  ```
- Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 4. **Run the App**
```bash
streamlit run app.py
```

---

## 🌐 APIs & Technologies Used

- **[Google Gemini API](https://aistudio.google.com/app/apikey):** For all creative text generation.
- **[Google Trends (pytrends)](https://github.com/GeneralMills/pytrends):** For real-time trending keywords and topics.
- **[Memegen.link API](https://memegen.link/):** For instant meme image generation.
- **[Pollinations API](https://pollinations.ai/):** For AI-generated YouTube thumbnails and art from prompts.
- **[Streamlit](https://streamlit.io/):** For the interactive web UI.
- **[python-docx](https://python-docx.readthedocs.io/en/latest/):** For exporting research results to DOCX.

---

## 📝 Example Inputs

### Content Generation
- **Platform:** Instagram
- **Prompt:** "Announce our new AI-powered photo editor that makes every selfie pop! Highlight its one-click background removal and fun filters. Encourage followers to try it and share their results."

### Niche & Keyword Research
- **Topic:** "AI tools for YouTube creators"

### Meme Generation
- **Template:** "Distracted Boyfriend"
- **Top Text:** "Me"
- **Bottom Text:** "New AI tool releases"

### YouTube SEO Metadata
- **Rough Video Title:** "Best Free AI Tools for YouTube Thumbnails"
- **Video Script:** "In this video, I test and compare the top free AI tools for making YouTube thumbnails. I show the results, discuss the pros and cons, and reveal which tool is best for beginners. Includes a step-by-step tutorial and real examples."

### Caption-to-Image Prompt
- **Caption:** "A futuristic city skyline at sunset, with flying cars and neon lights, in the style of a digital painting"

### YouTube Thumbnail Generator
- **Metadata:**  
  ```
  ### 📢 Optimized Title
  - AI Thumbnail Showdown: Canva vs VidIQ vs Copilot vs ChatGPT!

  ### 📝 Description
  Which AI tool makes the best YouTube thumbnail? I compare Canva, VidIQ, Copilot, and ChatGPT using the same photo and text. See which one nails the look and which one fails! Includes side-by-side results, tips for creators, and my honest verdict.

  ### 🏷️ Tags
  AI, YouTube Thumbnails, Canva, VidIQ, Copilot, ChatGPT, Thumbnail Design, Free Tools, YouTube Tips
  ```

---

## 💡 Tips for Best Results

- For memes, leave text fields blank to let the AI generate trending captions.
- For thumbnails, use metadata that clearly describes the comparison or main subject.
- For SEO, provide a detailed script/outline for richer metadata.
- Use the copy and download buttons for easy content reuse.

---

## 📄 License

This project is open source and free to use under the MIT License.

---

## 🙏 Credits

- [Streamlit](https://streamlit.io/)
- [Google Gemini](https://aistudio.google.com/)
- [Memegen.link](https://memegen.link/)
- [Pollinations](https://pollinations.ai/)
- [pytrends](https://github.com/GeneralMills/pytrends)
- [python-docx](https://python-docx.readthedocs.io/en/latest/)

---

## ✉️ Feedback & Contributions

Feel free to open issues or pull requests for improvements, new features, or bug fixes.  
Happy creating!
