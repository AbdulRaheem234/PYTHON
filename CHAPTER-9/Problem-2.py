import random


def game():
    print("You are the playing the game..")
    score = random.randint(1, 62)
    with open("C:\\Users\\Admin\\OneDrive\\Desktop\\PYTHON\\CHAPTER-9\\hiscore.txt", "r") as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score: {score}")
    if (score > hiscore):
        with open("C:\\Users\\Admin\\OneDrive\\Desktop\\PYTHON\\CHAPTER-9\\hiscore.txt", "w") as f:
            f.write(str(score))
    return score


game()
