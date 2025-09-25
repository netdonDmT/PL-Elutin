text = input()


sp = [text[i] for i in range(len(text))]
print("Количество замен: ",sp.count("."))

while "." in text:
    text = text.replace(".", "")
print(text)

  
