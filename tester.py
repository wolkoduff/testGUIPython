def replace_any_delimeters(string):
    string_act = string.strip()
    for ch in ('\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '>', '#', '+', '-', '.', '!', '$', '\'', ':', '\n',
               ','):
        if ch in string_act:
            string_act = string_act.replace(ch, "")
    return string_act


def count_words(string, word):
    cnt = 0
    for x in string:
        for y in (x.split(" ")):
            if replace_any_delimeters(y).lower() == word:
                cnt += 1
    return cnt


with open("claim.txt", "r", encoding="utf-8") as file:
    print(count_words(file.readlines(), "поле".lower()))
