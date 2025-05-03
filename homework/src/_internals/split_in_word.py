def split_in_word(all_lines):
    words = []
    for line in all_lines:
        words.extend(word.strip(",.!?") for word in line.split())
    return words
