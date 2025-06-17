
from gtts import gTTS
from IPython.display import Audio, display

# Step 3: Function to convert Hindi text to speech
def hindi_text_to_speech(text, slow=False, filename='hindi_output.mp3'):
    tts = gTTS(text=text, lang='hi', slow=slow)
    tts.save(filename)
    print(f"✅ Audio saved as: {filename}")
    return filename

# Step 4: Input from user
hindi_text = input("🔤 हिंदी में कुछ लिखें:\n")

# Step 5: Convert and play
filename = hindi_text_to_speech(hindi_text, slow=False)
display(Audio(filename))
