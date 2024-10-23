def single_root_words (root_word, *other_words):
    same_words = []
    is_symbol = False
    for word in other_words:
        if word.count(root_word) != 0:
            is_symbol = True
    if is_symbol:
        for word in other_words:
            if root_word.lower() in word.lower():
                same_words.append(word)
        return same_words
    else:
        for word in other_words:
            if word.lower() in root_word.lower():
                same_words.append(word)
        return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('гиперактивный', 'актив', 'ГИПЕР', 'зИмовать', 'активный')
print(result1)
print(result2)
print(result3)