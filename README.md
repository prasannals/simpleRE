# simpleRE
A library to simplify usage of Regular Expressions in Python.


# Usage
import simplere

matches = simplere.match(text, pattern, limit=num)

### examples
print(simplere.match('Hello World', r'[a-zA-Z]+'))

Output: [('Hello', 0, 5), ('World', 6, 11)]

print(simplere.match('Hello World', r'[a-zA-Z]+', limit=1))

Output: [('Hello', 0, 5)]

### Refer docstrings for documentation