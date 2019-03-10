import random
def make_word(word1):
    words = ['есть','делать','пытаться','готовить']
    while True:
        word2 = random.choice(words)
        word3 = random.choice(words)
        print('+')
        if word1 != word2 and word1 != word3 and word2 != word3:
            print(f"word1 ={word1}; word2 = {word2}; word3 = {word3}")
            break

make_word('делать')
