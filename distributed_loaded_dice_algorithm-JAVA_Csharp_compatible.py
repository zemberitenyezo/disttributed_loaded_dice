#The decentralized loaded dice algorithm's executable proof of concept Python script.

import hashlib

def distributed_loaded_dice(candidates, joker):
    previous_hash = 0
    #looping through all candidate names one by one
    for candidate in candidates:
        #creating the chance counter for each candidate
        for chance in range(candidate[1]):
            #concatenating ("adding") a particular value of the chance counter to the candidate's name
            #as well as a commonly known real world random number that changes with time, like a lottery
            s = candidate[0]+str(chance)+str(joker)
            #calculating the pseudo random ("hash") function
            next_hash = hashlib.sha256(s.encode('utf-8'))
            #added integer conversion for compatibility
            next_hash = int.from_bytes(next_hash.digest(), byteorder='big', signed=False)
            #looking for a hash greater than any previously calculated one
            if next_hash > previous_hash:
                #if a candidate has a hash value (relating to the card's value in the card game example)
                #higher than any previvously checked, then this candidate's name is temporarily stored
                #as suggestion for after the algorithm will have finished
                suggested = candidate[0]
                #as well as the hash value is also stored to compare later hash values against while the algorithm is running
                previous_hash = next_hash
    return(suggested)



print("Hány nem listás ellenzéki indul a körzetében?")
indulok_szama = int(input())
print()

indulok = []
for i in range(indulok_szama):
    print(i+1, ". induló neve?")
    neve = input()
    print(i+1, ". induló népszerűsége (%)?")
    eselye = int(float(input())*100)
    indulok.append([neve, eselye])
    print()

print("Kérem adja meg a legfrissebb Joker sorsoláson kihúzott 6 jegyű szelvény számot!")
joker = int(input())
print()
print("Kérem szavazzon", distributed_loaded_dice(indulok, joker), "nevű jelöltre!")
