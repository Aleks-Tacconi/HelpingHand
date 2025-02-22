import os
import base64
import openai


class AI:
    def __init__(self) -> None:
        api_key = os.getenv("OPENAI_API_KEY")

        self.__model = openai.OpenAI(api_key=api_key)
        self.__image_path = os.path.join("assets", "image.jpg")

    def __encode_image(self) -> str:
        with open(file=self.__image_path, mode="rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")

    def prompt(self, prompt: str):
        image = self.__encode_image()
        response = self.__model.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{image}"},
                        },
                    ],
                }
            ],
            max_tokens=100,
        )

        return response.usage
