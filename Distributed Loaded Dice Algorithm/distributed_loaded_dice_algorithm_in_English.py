# The decentralized loaded dice algorithm's executable proof of concept Python script.

import hashlib

# input parameters:
# 'candidates' is a list of lists with two entries each: [[name1, chance1],[name2, chance2], ..., [nameN, chanceN]]
# 'joker' is a simple integer
def distributed_loaded_dice(candidates, joker):
    previous_hash = 0
    # looping through all candidate names one by one
    for candidate in candidates:
        # creating the chance counter for each candidate
        for chance in range(candidate[1]):
            # concatenating ("adding") a particular value of the chance counter to the candidate's name
            # as well as a commonly known real world random number that changes with time, like a lottery
            s = candidate[0]+str(chance)+str(joker)
            # calculating the pseudo random ("hash") function
            next_hash = hashlib.sha256(s.encode('utf-8'))
            # added integer conversion for compatibility
            next_hash = int.from_bytes(next_hash.digest(), byteorder='big', signed=False)
            # looking for a hash greater than any previously calculated one
            if next_hash > previous_hash:
                # if a candidate has a hash value (relating to the card's value in the card game example)
                # higher than any previvously checked, then this candidate's name is temporarily stored
                # as suggestion for after the algorithm will have finished
                suggested = candidate[0]
                # as well as the hash value is also stored to compare later hash values against while the algorithm is running
                previous_hash = next_hash
    return(suggested)

 
print("How many oppositional candidates run in your local district?")
number_of_candidates = int(input())
print()

candidates_list = []
# collecting candidates' data
for i in range(number_of_candidates):
    print("What is the name of candidate number", i+1, "?")
    its_name = input()
    print("Please enter the popularity of the party that candidate number", i+1, "belongs to:")
    its_chance = int(float(input())*100)
    # extend list of locally runing candidates
    candidates_list.append([its_name, its_chance])
    print()

# Refer to README for details over the random number's role.
print("Please add the publicly widely agreed upon random number, like a lottery, that has been randomly generated closely before election:")
common_real_life_random_number = int(input())
print()

print("Please cast your vote to the following local candidate in your voting district:", distributed_loaded_dice(candidates_list, common_real_life_random_number))
