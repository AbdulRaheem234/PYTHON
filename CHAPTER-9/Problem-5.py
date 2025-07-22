words = ["Donkey", "bad", "ganda"]
with open("C:\\Users\\Admin\\OneDrive\\Desktop\\PYTHON\\CHAPTER-9\\file-1.txt", "r")as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))
with open("C:\\Users\\Admin\\OneDrive\\Desktop\\PYTHON\\CHAPTER-9\\file-1.txt", "w")as f:
    f.write(content)
