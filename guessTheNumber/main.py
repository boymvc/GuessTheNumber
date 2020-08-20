import math

possibleAnswers = ['Y', 'y', 'yes', 'Yes', 'N', 'n', 'no', 'No']
error = 'This is not an answer of either Y, y, yes, Yes, N, n, no, or No '
print('Please answer all question with >, <, Yes or No')

def checkAnswer (answer):
  for i in range(4):
    if possibleAnswers[i] == answer:
      return '>'
    elif possibleAnswers[4 + i] == answer:
      return '<'
  return error

def findMidPoint (lowPoint, highPoint):
  return math.floor((highPoint + lowPoint) // 2)

def askQuestion (lowestInRange, highestInRange):
  if lowestInRange == highestInRange:
    print('Your number is', lowestInRange)
    return
  midPoint = findMidPoint(lowestInRange, highestInRange)
  print(lowestInRange, highestInRange, midPoint)
  answer = input('Is your number > ' + str(midPoint) + '? ')
  answer = checkAnswer(answer)
  if answer == '>':
    lowestInRange = midPoint + 1
  elif answer == '<':
    highestInRange = midPoint
  else:
    print(answer)
  askQuestion(lowestInRange, highestInRange)
  # Is range down to 1 number
  #     Confirm the answer
  # else reiterate with new range

askQuestion(0,100)