import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidely so'
    elif answerNumber == 3: 
        return 'Yes'
    elif answerNumber == 4:
        return 'The future is hazy and uncertain, try again.'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'Ask again later'
    elif answerNumber == 8:
        return 'My reply is no'
    elif answerNumber == 9:
        return 'Very doubtful'

#r = random.randint(1, 9)
#fortune = getAnswer(r)
print(getAnswer(random.randint(1,9)))

