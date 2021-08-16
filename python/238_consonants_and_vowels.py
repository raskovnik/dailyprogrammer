from random import randint
import time

def garbage(v_c) -> str:
    start = time.time()
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    for c  in v_c:
        if c == "c" or c == "C":
            if c == "c":
                v_c = v_c.replace(c, consonants[randint(0, len(consonants)-1)], 1)
            else:
                v_c = v_c.replace(c, consonants[randint(0, len(consonants)-1)].upper(), 1)

        if c == "v" or c == "V":
            if c == "v":
                v_c = v_c.replace(c, vowels[randint(0, len(vowels)-1)], 1)
            else:
                v_c = v_c.replace(c, consonants[randint(0, len(vowels)-1)].upper(), 1)

    print(time.time()- start)
    return v_c

garbage("cvvc" * 50000)

def garbage2(v_c) -> str:
    start = time.time()
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    new_str = ""
    for c in v_c:
        if c == "c" or c == "c":
            if c == "c":
                new_str +=  consonants[randint(0, len(consonants)-1)]
            else:
                new_str += consonants[randint(0, len(consonants) -1)].upper()

        if c == "V" or c == "v":
            if c == "v":
                new_str +=  consonants[randint(0, len(vowels)-1)]
            else:
                new_str += consonants[randint(0, len(vowels) -1)].upper()
    print(time.time()-start)
    return v_c

garbage2("cvvc" * 50000)