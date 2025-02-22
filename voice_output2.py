import os
from playsound3 import playsound
from elevenlabs import ElevenLabs

def generate_response_voice(prompt) -> None:
    key = os.getenv("ELEVEN_LABS_API_KEY")
    client = ElevenLabs(api_key=key)

    # Generate speech from the prompt
    response = client.text_to_speech.convert(
        voice_id="bIQlQ61Q7WgbyZAL7IWj",
        output_format="mp3_44100_128",
        text=prompt,
        model_id="eleven_multilingual_v2",
    )


    audio_path = os.path.abspath("answer.mp3")
    with open(audio_path, "wb") as f:
        f.write(response)


    try:
        playsound(audio_path)
    finally:
        if os.path.exists(audio_path):
            os.remove(audio_path)

if __name__ == "__main__":
    generate_response_voice("Hello World, how are you!")


