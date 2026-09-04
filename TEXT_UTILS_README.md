# Text Utils

A comprehensive text manipulation and analysis utility with reverse operations, palindrome detection, and detailed statistics.

## Features

- **Reverse Text** - Reverse characters, words, or lines
- **Palindrome Detection** - Check if text is a palindrome
- **Text Analysis** - Get comprehensive statistics about text
- **Character Codes** - Display ASCII/Unicode values
- **File Processing** - Process text files with various operations

## Requirements

- Python 3.11+
- No external dependencies (uses only standard library)

## Installation

```bash
git clone https://github.com/yourusername/text-utils.git
cd text-utils
python WorldOfReversedScripts.py
```

## Usage

```bash
python WorldOfReversedScripts.py
```

### Menu Options

1. **Reverse Text** - Reverse all characters
2. **Reverse Words** - Reverse word order
3. **Reverse Lines** - Reverse line order
4. **Text Analysis** - Get detailed statistics
5. **Palindrome Check** - Check if text is palindrome
6. **Show Character Codes** - Display ASCII/Unicode values

## Examples

```bash
$ python WorldOfReversedScripts.py
=== WORLD OF REVERSED SCRIPTS ===

1. Reverse text
2. Reverse words
3. Reverse lines
4. Text analysis
5. Palindrome check
6. Show character codes

Choose option (1-6): 1
Enter text to reverse: hello world

Reversed: dlrow olleh
```

### Text Analysis

```
==================================================
📊 TEXT ANALYSIS
==================================================
Total Characters: 25
Characters (no spaces): 20
Total Words: 4
Total Lines: 1
Average Word Length: 5.00
Unique Words: 4
❌ Not a palindrome
==================================================
```

## Docker

```bash
docker build -t text-utils .
docker run -it text-utils:latest
```

## License

MIT
