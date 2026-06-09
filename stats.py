def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_num_characters(text: str) -> dict[str, int]:
    tracked_characters = {}
    for char in text:
        char = char.lower()
        if char in tracked_characters:
            tracked_characters[char] += 1
        else:
            tracked_characters[char] = 1

    return tracked_characters

def chars_dict_to_sorted_list(d: dict[str, int]) -> list[tuple[str, int]]:
    character_counts = []
    for char, num in d.items():
        character_counts.append((char, num))
    
    return sorted(character_counts, key=sort_on, reverse=True)

def sort_on(char_count: tuple[str, int]) -> int:
    return char_count[1]
