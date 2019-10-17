word = input('enter the word')
h = int(input('enter the height '))
for c, i in enumerate(range(1, h+1, len(word)//2)):
    print(' '*(h-i+len(word)//2)+word*(c+1), end='\n')
