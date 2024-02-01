# Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests. 
# Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory. Each contest is described
# by two integers,  and :

#  is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will decrease by ; 
# if she loses it, her luck balance will increase by .
#  denotes the contest's importance rating. It's equal to  if the contest is important, and it's equal to  if it's unimportant.
# If Lena loses no more than  important contests, what is the maximum amount of luck she can have after competing in all
# the preliminary contests? This value may be negative.

def luck_balance(k, contests):
    import_contests = []
    total = 0

    for luck, importance in contests:
        if importance == 0:
            total += luck
        else:
            import_contests.append(luck)
    
    import_contests.sort(reverse=True)

    for i in range(min(k, len(import_contests))):
        total += import_contests[i]

    for i in range(k, len(import_contests)):
        total -= import_contests[i]

    return total

print(luck_balance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))