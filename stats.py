# stats.py
def get_word_count(text):
    words = text.split()
    return len(words)


def get_character_count(text):
    characters = {}
    for c in text:
        if c.isalpha():
            c = c.lower()
            if c in characters:
                characters[c] += 1
            else:
                characters[c] = 1
    return characters

def sort_on(characters):
    sorted_list = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True))
    return sorted_list