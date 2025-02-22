from openai import OpenAI
import os
from playsound3 import playsound

def generate_response_voice(prompt) -> None:
    key = os.getenv("OPENAI_API_KEY")
    gpt = OpenAI(api_key=key)

    response = gpt.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=prompt
    )

    audio_path = os.path.abspath("answer.wav")
    with open(audio_path, "wb") as f:
        f.write(response.content)

    try:
        playsound(audio_path)
    finally:
        # Ensure the file is deleted after playback (even if an error occurs)
        if os.path.exists(audio_path):
            os.remove(audio_path)

if __name__ == "__main__":
    generate_response_voice("Hello World, how are you!")

