import streamlit as st
from gtts import gTTS
import base64

# Page Setup
st.set_page_config(page_title="Even or Odd Game 🎮", page_icon="🎲")
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🔢 Even or Odd Fun Game for Kids!</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #FF9800;'>Learn numbers and languages with sound and smiles 😊</h4>", unsafe_allow_html=True)

# Language options and codes
language_map = {
    "English 🇬🇧": "en",
    "French 🇫🇷": "fr",
    "Spanish 🇪🇸": "es",
    "Igbo 🇳🇬": "ig",
    "Yoruba 🥁": "yo"
}

# Translated sentence function
def get_translated_sentence(num, name, is_even, language):
    if "English" in language:
        return f"{num} is an {'even' if is_even else 'odd'} number, {name}! 🎉"
    elif "French" in language:
        return f"{num} est un {'nombre pair' if is_even else 'nombre impair'}, {name}! 🎈"
    elif "Spanish" in language:
        return f"{num} es un {'número par' if is_even else 'número impar'}, {name}! 🎊"
    elif "Igbo" in language:
        return f"{num} bụ {'ọnụọgụgụ dị ọbụ' if is_even else 'ọnụọgụgụ dị ntakịrị'}, {name}! 🧁"
    elif "Yoruba" in language:
        return f"{num} jẹ {'nọmba alagbeka' if is_even else 'nọmba alailesin'}, {name}! 🍭"
    else:
        return f"{num} is a number, {name}."

# Input Section
st.markdown("---")
name = st.text_input("🧒 What is your name?")
number_input = st.text_input("🔢 Type any number:")

# Helper function
def generate_audio_and_play(sentence, language_code):
    tts = gTTS(text=sentence, lang=language_code)
    tts.save("result.mp3")
    audio_bytes = open("result.mp3", "rb").read()
    st.audio(audio_bytes, format="audio/mp3")
    b64 = base64.b64encode(audio_bytes).decode()
    st.markdown(f'<a href="data:audio/mp3;base64,{b64}" download="result.mp3">📥 Download Audio</a>', unsafe_allow_html=True)

# When inputs are ready
if name and number_input:
    try:
        num = int(number_input)
        is_even = (num % 2 == 0)
        st.markdown("---")
        st.markdown("<h4 style='color: #009688;'>🎤 Click a language to hear your result!</h4>", unsafe_allow_html=True)

        for lang_label, lang_code in language_map.items():
            if st.button(f"🔊 {lang_label}"):
                sentence = get_translated_sentence(num, name, is_even, lang_label)
                st.success(sentence)

                if lang_code in ["en", "fr", "es"]:
                    try:
                        generate_audio_and_play(sentence, lang_code)
                    except:
                        st.error("⚠️ Oops! Could not play audio.")
                else:
                    st.warning("🔇 Voice is not yet available for this language. Text only for now.")
                
                # Educational tip
                if is_even:
                    st.info("✅ An even number is divisible by 2. Example: 2, 4, 6...")
                else:
                    st.info("🧐 An odd number is NOT divisible by 2. Example: 1, 3, 5...")

    except ValueError:
        st.error("🚫 Please enter a valid whole number.")
