def count_vowels(text):
    return sum(1 for c in text if c.lower() in "aeiou")
