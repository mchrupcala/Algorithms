
    # Sprint recursion tmrw - looping is repeating a pattern. How can you avoid looping, and use recursion instead, to accomplish the same goal?




def geekscopy(s1, s2):
    if s1 == s2:
        print(s2)
        return s2
    else:
        print("yay!")
        s2 = s1
    return geekscopy(s1, s2)

# geekscopy("hello", "geeks")