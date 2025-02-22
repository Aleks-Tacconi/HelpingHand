from ai import AI

PROMPT = """
Given the image provided

- identify the most central item in the image
- reply only with the name of the item
- ignore all other details or description
"""


def main() -> None:
    # ai = AI()
    # response = ai.prompt(PROMPT)
    response = "Birch tree"

    print(response)


if __name__ == "__main__":
    main()
