import pyperclip
fp=open("cogs/words.txt","r")
everything=fp.read().split('\n')
typee = input("Which tea are we drinking?")
used = []
if typee == "yellow" or typee == "y":
    while True:
        
        words=[]        
        answer = ""
        substr=input("Substring:")
        for i in everything:
            if substr in i:
                words.append(i)
        words=sorted(words, key=lambda x:len(x), reverse=False)
        curr = 0
        resolved = 0
        for i in words:
            
            if curr >= 2001:
                pyperclip.copy(answer)
                resolved = 1
                break

            else:
                curr += len(i)
                curr += 1
                if curr <= 2000:
                    answer += i 
                    answer += " "
        
        pyperclip.copy(answer)

elif typee == "black" or typee == "b" or typee == "green" or typee == "g":
    while True:
        
        words=[]        
        answer = ""
        substr=input("Substring:")
        for i in everything and i not in used:
            if substr in i:
                pyperclip.copy(" ")
                pyperclip.copy(i)
                used.append(i)
                break
elif typee == "red" or typee == "r":
    while True:

        words=[]        
        answer = ""
        substr=input("Substring:")
        for i in everything:
            
            if substr in i:
                words.append(i)
        words=sorted(words, key=lambda x:len(x), reverse=False)
        curr = 0
        
        pyperclip.copy(words[-1])
