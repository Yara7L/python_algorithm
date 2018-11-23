def hammingdistance(s1,s2):
    if len(s1)!=len(s2):
        raise ValueError("Undefined for sequence of unequal length")
    return sum(el1 != el2 for el1,el2 in zip(s1,s2))
# zip(A,B)=>(a1,b1),(a2,b2)

s1='hamming'
s2='hanming'
print(hammingdistance(s1,s2))