from random import randint 

for i in range(5):
    score = randint(60, 100)
    char_add = (100 - score) // 10
    print(score, chr(ord('A') + char_add))

print('XieJiongyan, 518021911249')
