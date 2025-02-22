from ai import AI

PROMPT = ""

def main() -> None:
    ai = AI()
    print(ai.prompt("Whats in this image?"))


if __name__ == "__main__":
    main()
