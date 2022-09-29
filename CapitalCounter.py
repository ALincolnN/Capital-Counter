"""
The project is aimed at checking for uppercase and lowercase letters in the input string and returning both counts
"""


def check(input):

    countu = 0
    countl = 0

    for i in input:
        if i.isupper():
            countu += 1

        else:
            countl += 1

    return '\nUPPERCASE '+str(countu) + '\nLOWERCASE '+str(countl)


x = input('Enter a phrase of mixed Capital AND Small letters: ')
print(check(x))
