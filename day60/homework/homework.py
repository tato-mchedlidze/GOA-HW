
# https://www.codewars.com/kata/59441520102eaa25260000bf
# https://www.codewars.com/kata/559d2284b5bb6799e9000047

# hw 1 The Wide-Mouthed frog!
def mouth_size(animal):
    if animal.lower() == "alligator":
        return "small"
    else:
        return "wide"


# hw 2 Get Nth Even Number
def nth_even(n):
    return (n - 1) * 2


# hw 3 Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence
def replace_exclamation(st):
    return ''.join('!' if st in 'aeiouAEIOU' else st for st in st)

