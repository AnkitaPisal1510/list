question=[
    "1.how many continents are there ?",
    "2.what is the capital of india ?",
"3.ng mai kon se course phadhaya jata hai ?"
]
option=[
    ["1.four","2.nine","3.seven","4.eight"],
["1.kopi","2.bhopal","3.pune","4.delhi"],
["1.software Engineering/cooding","2.zagda karna truth and dare khelna","3.bavarchi/blmajduri","4.zadhu poccha"]
]
solution=[3,4,1]
Z=[["1.four","3.seven"],["1.khopi","4.delhi"],["1.software Engineering/cooding","4.zadu pochha"]]
print(                       " πππ€π€π€ WELCOME TO KBCπ€π€π€ππ                              ")
i=0
count=0
sum=0
while i<len(question):
    print(question[i]) 
    j=0
    while j<len(option[i]):
        print(option[i][j])
        j+=1
    num=int(input("enter your answer"))
    j=input("π©βπ»are you sure about your answer I don't thik soπ©βπ»ππ")
    if j=="no":
        print("ok")
        lifeline=input("π©βπ»π©βdo to you want any lifelineπ©βπ»π©β")
        if lifeline=="yes":
                use=int(input("π€π€which lifeline you wantπ€π€ "))
                if use==5050:
                    print("πokπ")
                if count<1:
                    print(Z[i])
                    count+=1
                    num=int(input("πππ€π€enter the answerπ€π€ππ"))
                    if num==solution[i]:
                        print("πyour answer is correctπ")
                        print()
                        sum+=10000
                        print(sum,"π€π€π€πππyou won that much amountππππ€π€π€")
                        print()
                    else:
                        print("ππ₯Ίgame overπ₯Ίπ")
                        print("you have to return with this amount",sum)
                        break
                else:
                    print(" opps! ππyou cant use lifeline againππ")
                    num=int(input("enter your answer"))
                    if num==solution[i]:
                        print("right answerπ")
                        print()
                        sum+=100000
                        print(sum,"π€π€π€πππcongrats you wonππππ€π€π€")
                        print()
                    else:
                        print('π₯Ίyou lostπ₯Ί')
                        print('you have to return with this amount',sum)
                        break
                        
    else:
        if num==solution[i]:
            print("right answerπβ")
            print()
            sum+=1000000
            print(sum,"π€π€π€π₯³π€π€ππcongratsπππ€π€π₯³π€π€π€")
            print()
        else:
            print("π₯Ίππgame overπ₯Ίππ")
            print("you have to return with this amount",sum)
            break
    i+=1
else:
    print()
    print("π₯³π₯³π₯³π₯³ππππ€©π€©π€©πππcongrats you won the KBCππππ€©π€©π€© ππππ₯³π₯³π₯³π₯³")
    

        

    
        