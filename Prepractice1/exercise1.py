list = ['name'] * 5

for i in range(5):
    print("please enter the ", i, "th name: ", sep= '', end = '')
    list[i] = input()

print('list:', list)
print('replacing place:', sep= '', end = '')
i_rep = int(input())
print('new name:', sep= '', end = '')
list[i_rep] = input()
print('list:', list)
print('XieJiongyan, 518021911249')
