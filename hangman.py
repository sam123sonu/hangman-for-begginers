print("                          **********************")
print("                          welcome to family game")
print("lets start now:")
score=0
wordlist=["suman","nirmala","krish","jasmin","dharanidhar","haramani"]
print("guess the name of ur family members:")
for i in range(0,6):
    guesslist=[]
    print("your {} member name is:".format(i+1))
    for j in range(0,len(wordlist[i])):
        print("*",end=" ")
        guesslist.append("*")
    print("\n")
    print("guess the letters:")
    count=0
    print("u have {} turns".format(len(wordlist[i])+5))
    for k in range(0,len(wordlist[i])+5):
        g_letter=input("your {} turn:".format(k+1))
        for j in range(0,len(wordlist[i])):
             if(wordlist[i][j]==g_letter):
                  guesslist[j]=g_letter
                  count=count+1
        print(guesslist)
        print(count)
        if(count==len(wordlist[i])):
           print("hurray! u win this round")
           score=score+1
           print("your current score is :{}".format(score))
           break;
        else:  
          if(k==len(wordlist[i])+4):
               print("oh no...u lose this  round")
               print("your score is: {}".format(score))          
    print("\n")

if(score==6):
    print("congrats!!!u win the game:")
else:
    print("better luck next time:")
