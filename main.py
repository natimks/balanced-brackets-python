
def is_balanced(s):
    if len(s) % 2 != 0:
        return 'NO'

    list_characters = list(s)
    final_list = []

    for character in list_characters:
        if is_brackets_open(character):
            final_list.append(character)
        else:
            if not final_list:
                return 'NO'
            final_character = final_list.pop()
            if not is_character_pair(final_character, character):
                return 'NO'

    if final_list:
        return 'NO'
    return 'YES'


def is_brackets_open(character):
    if character == "{" or character == "[" or character == "(":
        return True
    return False


def is_character_pair(open_character, last_character):
    dictionary_pairs = {
        "]": "[",
        "}": "{",
        ")": "("
    }
    try:
        if dictionary_pairs[last_character] == open_character:
            return True
    except KeyError:
        return False
    return False


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = is_balanced(s)

        print(result + '\n')
