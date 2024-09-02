def get_length(lst):
    return len(lst)

def find_sum_and_carry(num1, num2, carry):
    if num1 == 0:
        if num2 == 0:
            return (carry, 0)
        else: # num1= 0, num2 = 1
            return (1-carry, carry)
    else:
        if num2 == 0:
            return (1-carry, carry)
        else:
            return (carry, 1)

def add(lst1, lst2):
    carry = 0
    sum_list = []
    lst1_len = get_length(lst1)
    lst2_len = get_length(lst2)
    temp = max(lst1_len, lst2_len)
    for i in range(temp):
        num1 = lst1[i] if i < lst1_len else 0
        num2 = lst2[i] if i < lst2_len else 0
        (sum_num, carry) = find_sum_and_carry(num1, num2, carry)
        sum_list.append(sum_num)
    if carry == 1:
        sum_list.append(carry)
    return sum_list

def grade_school_multiply(a, b):
    n, m = len(a), len(b)
    tmp = a
    res = [0]
    for bit in b:
        if bit == 1:
            res = add(res, tmp)
        tmp = [0]+tmp # shift tmp
    return res 

def subtract(a, b):
    # we will use two's complement subtraction
    # this is a very nice and common trick where
    # we can use addition to perform subraction of
    # binary numbers. It is used inside computers.
    # assume a >= b -- this will generally hold for all our use cases
    n = len(a)
    #assert(len(b) <= n)
    k = len(a) - len(b)    
    bcomp = [1-elt for elt in b] + [1]*k # flip the bits in b and pad with 1s
    bcomp2 = add(bcomp, [1]) # add 1
    r = add(a, bcomp2)
    return r[0:n]

def pad(a, k):
    return  [0]*k + a

def karatsuba_multiply(a, b):
    (m, n) = len(a), len(b)
    if m <= 2 or n <= 2:
        # revert to grade school multiplication
        return grade_school_multiply(a, b)
    else:
        mid1 = m//2
        a1 = a[0:mid1]
        a2 = a[mid1:]
        b1 = b[0:mid1]
        b2 = b[mid1:]
        # [a] = 2^{mid1} * [a2] + [a1]
        # [b] = 2^{mid1} * [b2] + [b1]
        # [a]* [b] = 2^{2*mid1} ([a2]*[b2]) + 2^mid1 ([a2]*[b1] + [a2]*[b1]) + [a1]*[b1]
        # [a]* [b] = 2^{2*mid1} r2 + 2^mid1 r4 + r1
        # r3 = ([a1]+[a2]) * ([b1]+[b2])
        # r4a = r3 - r1
        # r4 = ([a2]*[b1] + [a2]*[b1]) = r3 - r4a - r2

        # 3 recursive calls to karatsuba_multiply
        r1 = karatsuba_multiply(a1, b1)  # [a1]*[b1]
        r2 = karatsuba_multiply(a2, b2) # [a2]*[b2]
        r3 = karatsuba_multiply(add(a1, a2), add(b1, b2)) # ([a1]*[a2]) + ([b1]*[b2])
        # Do subtraction
        r4a = subtract(r3, r1)
        r4 = subtract(r4a, r2)
        
        # Do paddding
        s1 = pad(r2, 2*mid1)
        s2 = pad(r4, mid1)
        s3 = add(s1, s2)
        return add(s3, r1)  
    
print(add([1,0,1,1,0], [1, 0, 0, 0, 1])) # [0, 1, 1, 1, 1]
print(subtract([0, 1, 1], [0, 1])) # [0, 0, 1]
print(grade_school_multiply([1, 0, 1], [1, 1])) # [1, 1, 1, 1]]
print(karatsuba_multiply([0, 0, 0, 1], [1, 0, 1])) # [0, 0, 0, 1, 0, 1]
