from pathlib import Path
from flask import Flask, request

app = Flask(__name__)


def reverse_text(text: str) -> str:
    return text[::-1]


def reverse_words(text: str) -> str:
    return " ".join(text.split()[::-1])


def reverse_lines(text: str) -> str:
    return "\n".join(text.split("\n")[::-1])


def check_palindrome(text: str) -> bool:
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def get_text_statistics(text: str) -> dict:
    words = text.split()

    return {
        "total_characters": len(text),
        "characters_no_spaces": len(text.replace(" ", "")),
        "total_words": len(words),
        "total_lines": len(text.split("\n")),
        "average_word_length": (
            sum(len(word) for word in words) / len(words)
            if words else 0
        ),
        "unique_words": len(set(word.lower() for word in words))
    }


def get_character_codes(text: str) -> str:
    return " | ".join(
        f"{char}:{ord(char)}" for char in text
    )


def reverse_alternating(text: str) -> str:
    chars = list(text)

    odd_chars = [
        chars[i] for i in range(1, len(chars), 2)
    ]

    result = []
    odd_idx = len(odd_chars) - 1

    for i, char in enumerate(chars):
        if i % 2 == 0:
            result.append(char)
        else:
            result.append(odd_chars[odd_idx])
            odd_idx -= 1

    return "".join(result)


def process_file(
    input_file: str,
    operation: str = "reverse",
    output_file: str = None
):
    file_path = Path(input_file)

    if not file_path.exists():
        return "File not found"

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if operation == "reverse":
        result = reverse_text(content)
    elif operation == "reverse_words":
        result = reverse_words(content)
    elif operation == "reverse_lines":
        result = reverse_lines(content)
    else:
        return "Unknown operation"

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result)

        return f"Saved to {output_file}"

    return result


@app.route("/")
def home():
    return """
    <h1>WORLD OF REVERSED SCRIPTS</h1>

    <form action="/reverse">
        <input name="text" placeholder="Enter text">
        <button type="submit">Reverse Text</button>
    </form>

    <br>

    <form action="/reverse_words">
        <input name="text" placeholder="Enter text">
        <button type="submit">Reverse Words</button>
    </form>

    <br>

    <form action="/palindrome">
        <input name="text" placeholder="Enter text">
        <button type="submit">Check Palindrome</button>
    </form>

    <br>

    <form action="/stats">
        <input name="text" placeholder="Enter text">
        <button type="submit">Text Statistics</button>
    </form>

    <br>

    <form action="/codes">
        <input name="text" placeholder="Enter text">
        <button type="submit">Character Codes</button>
    </form>
    """


@app.route("/reverse")
def reverse():
    text = request.args.get("text", "")
    return reverse_text(text)


@app.route("/reverse_words")
def reverse_words_route():
    text = request.args.get("text", "")
    return reverse_words(text)


@app.route("/palindrome")
def palindrome():
    text = request.args.get("text", "")

    if check_palindrome(text):
        return "✅ YES - Palindrome"

    return "❌ NO - Not a palindrome"


@app.route("/stats")
def stats():
    text = request.args.get("text", "")
    data = get_text_statistics(text)

    return f"""
    Total Characters: {data['total_characters']}<br>
    Characters No Spaces: {data['characters_no_spaces']}<br>
    Total Words: {data['total_words']}<br>
    Total Lines: {data['total_lines']}<br>
    Average Word Length: {data['average_word_length']:.2f}<br>
    Unique Words: {data['unique_words']}
    """


@app.route("/codes")
def codes():
    text = request.args.get("text", "")
    return get_character_codes(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
