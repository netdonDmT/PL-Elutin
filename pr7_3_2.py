def alph(text):
    text_list = text.split()
    text_list_sort = ["".join(sorted(text_list[i])) for i in range(len(text_list))]

    return " ".join(text_list_sort)
text = input()
print(alph(text))
