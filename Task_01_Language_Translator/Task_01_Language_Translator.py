import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌐 Language Translator Tool")

text = st.text_area("Enter text")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Arabic": "ar",
    "Bengali": "bn",
    "Urdu": "ur",
    "Tamil": "ta",
    "Telugu": "te"
}
# Dropdown instead of text input
source_lang = st.selectbox("Source Language", list(languages.keys()))
target_lang = st.selectbox("Target Language", list(languages.keys()), index=1)

if st.button("Translate"):
    if text:
        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.success("Translated Text")
        st.write(translated)

        st.text_area("Copy Output", translated)
    else:
        st.warning("Please enter text")