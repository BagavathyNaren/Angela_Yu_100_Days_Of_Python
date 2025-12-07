"""
Robust International Morse Code encoder/decoder
Handles letters, numbers, common punctuation, prosigns, and is forgiving on input spacing.
"""

MORSE_CODE = {
    'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',  'E': '.',    'F': '..-.',
    'G': '--.',  'H': '....', 'I': '..',   'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--',   'N': '-.',   'O': '---',  'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...',  'T': '-',    'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..',  '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.',  '(': '-.--.',  ')': '-.--.-', '&': '.-...',  ':': '---...',
    ';': '-.-.-.', '=': '-...-',  '+': '.-.-.',  '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    # Common prosigns – encoded without spaces, decoded with <>
    '<AR>': '.-.-.', '<SK>': '...-.-', '<BT>': '-...-', '<HH>': '........',
    '<SOS>': '...---...'
}

# Reverse dictionary (Morse → character/prosign)
REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}


def text_to_morse(text: str) -> str:
    """Convert text → Morse code (3 spaces between words, 1 space between letters)."""
    if not text.strip():
        return ""

    words = text.split()
    morse_words = []

    for word in words:
        morse_chars = []
        for ch in word.upper():                # we use uppercase keys now
            if ch in MORSE_CODE:
                morse_chars.append(MORSE_CODE[ch])
            else:
                morse_chars.append('?')        # unknown character → visible error
        morse_words.append(' '.join(morse_chars))

    return '   '.join(morse_words)


def morse_to_text(morse: str) -> str:
    """Convert Morse code → text. Extremely forgiving on spacing."""
    if not morse.strip():
        return ""

    # Split on any sequence of 2+ spaces to separate words reliably
    raw_words = [part.strip() for part in morse.split('  ') if part.strip()]

    decoded_words = []
    for raw_word in raw_words:
        symbols = raw_word.split()              # handles 1 or more spaces between letters
        word_chars = []
        for sym in symbols:
            not_found = REVERSE_MORSE.get(sym, '?')
            word_chars.append(not_found)
        decoded_words.append(''.join(word_chars))

    result = ' '.join(decoded_words)

    # Replace prosign placeholders with proper <> notation (case-insensitive)
    for prosign in ['<AR>', '<SK>', '<BT>', '<HH>', '<SOS>']:
        placeholder = prosign[1:-1].lower()
        result = result.replace(placeholder, prosign)

    # Capitalize only the very first letter of the whole message (standard practice)
    return result.capitalize() if result else ""


def main() -> None:
    print("\nMorse Code Converter & Decoder")
    print("  • Letters, numbers, punctuation, and common prosigns supported")
    print("  • Type 'quit' or press Ctrl+C to exit\n")

    while True:
        try:
            choice = input("Convert to Morse (c) or Decode from Morse (d)? [c/d]: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n\nGoodbye!")
            break

        if choice not in {'c', 'convert', 'd', 'decode', ''}:
            print("Please type 'c' or 'd'\n")
            continue

        if choice.startswith('c') or choice == '':
            message = input("\nEnter text to convert: ").strip()
            if message.lower() == 'quit':
                print("Goodbye!\n")
                break
            print(f"\nMorse code:\n{text_to_morse(message) or '(empty)'}\n")

        else:
            code = input("\nEnter/paste Morse code: ").strip()
            if code.lower() == 'quit':
                print("Goodbye!\n")
                break
            print(f"\nDecoded text:\n{morse_to_text(code) or '(empty)'}\n")

        print("-" * 60)


if __name__ == "__main__":
    main()