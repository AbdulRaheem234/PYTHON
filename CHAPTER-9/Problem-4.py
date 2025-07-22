word = "Donkey"
with open("C:\\Users\\Admin\\OneDrive\\Desktop\\PYTHON\\CHAPTER-9\\file-1.txt", "r")as f:
    content = f.read()
contentNew = content.replace(word, "######")
with open("C:\\Users\\Admin\\OneDrive\\Desktop\\PYTHON\\CHAPTER-9\\file-1.txt", "w")as f:
    f.write(contentNew)
