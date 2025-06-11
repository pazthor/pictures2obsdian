from typing import Union
from openai import OpenAI
from back_end.definitions import OPEN_AI_SYSTEM_PROMPT

class OpenAIHandler:
    def __init__(self):
        self.client = OpenAI()
        self.initial_prompt = OPEN_AI_SYSTEM_PROMPT

    def process_markdown(self, markdown_text: str) -> dict[str, Union[int, str, list]]:
        try:
            response = self.client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": self.initial_prompt},
                    {"role": "user", "content": markdown_text}
                ],
                temperature=0,
            )
            return {
                "status": 200,
                "message": "",
                "content": eval(response.choices[0].message.content),
                "metadata": []
            }
        except Exception as e:
            return {
                "status": 500,
                "message": str(e),
                "content": "",
                "metadata": []
            }