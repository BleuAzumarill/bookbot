def word_count(text):
    count = text.split()
    return len(count)

def character_count(text):
    lower = text.lower()
    conversion = {}
    for character in lower:
        if character not in conversion:
            conversion[character] = 1
        else:
            conversion[character] += 1 
    return conversion

def sorted_list(conversion):
    chars_list = [{'char': char, 'count': count} for char, count in conversion.items()]
    chars_list.sort(reverse=True, key=lambda x: x['count'])
    return chars_list
    