
def ceasar(text, shift, direction): #Creates a function
  if direction == 'left': #If direction is left, reverses the way in which shift goes by adding a negative
    shift = -shift
  if direction == 'Left':
    shift = -shift
  result = '' #Base variable for finished text
  for char in text:
    if char.isalpha(): #If char is with alphabet
      num = ord(char) + shift #Shifts the actual letter
      if char.isupper(): #If char is upper
        if num > ord('Z'): #if the char surpasses the alphabet, it subtracts the number or adds the number by 26 to reset it. It's done with both capital and lowercase letters
          num -= 26
        elif num < ord('A'):
          num += 26
      elif char.islower():
        if num > ord('z'):
          num -= 26
        elif num < ord ('a'):
          num += 26
      result += chr(num) #Adds the shifted result to the new phrase
    else: #If the chr isnt in alphabet it'll add it without changes
      result += char
  return result

#Collects data from the user, asking them questions
phrase = input('Please enter your you text that you want to be encoded: ')
shiftt = input('Please enter the shift that you want: ')
directions = input('Please enter the direction you want it to be shifted: ')

#Checks to see if shift is a number
if shiftt.isdigit() is False:
  print('You have not entered a valid shift, please try again')
else:
  print(ceasar(phrase, int(shiftt), directions))
