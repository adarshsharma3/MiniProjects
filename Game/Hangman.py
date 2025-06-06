import random


while True:
 play=False   
 Check=input("Would you like to play the game: Y/N")
 if Check=='Y' or Check=='y':
    play=True


 words=["IRONMAN","LUFFY","RORONOA","ROBIN"]
 total_chances=7
 word=random.choice(words)
 guessed_word=['_']*len(word)
 print(guessed_word)
 while play==True: 
  
  
  

  chr=input("Enter the letter").upper()

  if chr in word:
    for i in range(0,len(word)):
        if word[i]==chr:
          guessed_word[i]=chr
          
    if ''.join(guessed_word) == word:
        print("Congratulations you won")
        play=False 

    print(guessed_word)       
  else:
    total_chances-=1
    print("No Wrong guesss")
    if total_chances<=0:

        print(guessed_word)
        print("You lost !!!!  Bloodyy Loser!!!")
        play=False

