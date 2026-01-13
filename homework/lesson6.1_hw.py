# task_1
text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
words = text.split()
result_words = []
for word in words:
    if word[-1] in ',.':
        modified_word = word[:-1] + 'ing' + word[-1]
    else:
        modified_word = word + 'ing'
    result_words.append(modified_word)
new_text = ' '.join(result_words)
print(new_text)
