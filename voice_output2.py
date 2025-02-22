from elevenlabs import ElevenLabs
import os
import tempfile
from playsound3 import playsound

key = os.getenv("ELEVEN_LABS_API_KEY")

def generate_response_voice2(text):
    client = ElevenLabs(api_key=key)

    audio_stream = client.text_to_speech.convert_as_stream(
        voice_id="bIQlQ61Q7WgbyZAL7IWj",
        output_format="mp3_44100_128",
        text=text,
        model_id="eleven_multilingual_v2"
    )

    audio_bytes = b''.join([chunk for chunk in audio_stream])

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        temp_file.write(audio_bytes)
        temp_file_path = temp_file.name

    playsound(temp_file_path)

    os.remove(temp_file_path)

