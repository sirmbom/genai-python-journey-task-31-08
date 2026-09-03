"""Small script-style string challenges.

There are seven TODOs in this file. The first six are single-line holes marked
with `# TODO: fill this line`. The final block (at the end) is 1-3 lines you
must complete to produce the final printed output.

Hints: use string methods like `.upper()`, `.lower()`, `.startswith()`,
`.split()`, `.isalpha()`, `.isdigit()`, `.strip()` and slicing.
"""

# Sample input string students will work with
s = "  Hello 123 World  "

# 1) Uppercase version of the string
# TODO: fill this line
s_upper = s.upper()  # TODO: replace None with s.upper()

# 2) Lowercase version of the string
# TODO: fill this line
s_lower = s.lower()  # TODO: replace None with s.lower()

# 3) Does the original string start with two spaces?
# TODO: fill this line
starts_with_two_spaces = s.startswith('  ')  # TODO: replace None with s.startswith('  ')

# 4) Tokenize into words (split on whitespace)
# TODO: fill this line
words = s.split()  # TODO: replace None with s.split()

# 5) Is the first token purely alphabetic?
# TODO: fill this line
first_is_alpha = words[0].isalpha()  # TODO: replace None with words[0].isalpha()

# 6) Is there a numeric token (e.g. '123') present and is it numeric?
# TODO: fill this line
numeric_token_is_digit = any(tok.isdigit() for tok in words)  # TODO: replace None with any(tok.isdigit() for tok in words)

# Final block (1-3 lines): create a normalized string (collapse whitespace)
# and print a short summary. Replace the placeholders below.
# TODO: complete the block below (1-3 lines)
normalized = ' '.join(s.split()).strip()  # TODO: set to ' '.join(s.split()).strip()
print(s_upper, s_lower)
print(starts_with_two_spaces, words, first_is_alpha, numeric_token_is_digit)
print("normalized:", normalized)
