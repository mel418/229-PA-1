""" ---------------- PROBLEM 1 ----------------"""
def equiv_to(a, m, low, high):
    k_low = low
    k_high = high
    k_vals = list(range(k_low,k_high + 1))
    x_vals = [i for i in k_vals if (i-a)%m==0]
    return x_vals

""" ---------------- PROBLEM 2 ----------------"""
def b_expansion(n, b):
    digits = [] # stores the digits of the b-expansion
    q = n
    while q != 0:
        digit = q % b
        if b == 16 and digit > 9:
            hex_dict = {10: 'A', 11 : 'B', 12: 'C', 13: 'D', 14: 'E', 15 : 'F'}
            digit = hex_dict[digit]
        digits.append(str(digit))
        q //= b
    return ''.join(digits[::-1])
        

""" ---------------- PROBLEM 3 ----------------"""
def binary_add(a, b): 
    # removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')
    
    # padding the strings with 0's so they are the same length
    if len(a) < len(b):
        diff = len(b) - len(a)
        a = "0" *diff + a
    elif len(a) > len(b):
        diff = len(a) - len(b)
        b = "0" *diff + b  #011011 = "0" * 1 +b
    
    # addition algorithm
    result = ""
    carry = 0
    for i in reversed(range(len(a))):
        a_i = int(a[i])
        b_i = int(b[i])
    
        result += str((a_i + b_i + int(carry)) % 2)
        carry = str((a_i + b_i + int(carry)) // 2)
    if carry == '1':
        result += (carry)
    return (result[::-1])

""" ---------------- PROBLEM 4 ----------------"""
def binary_mul(a, b):
    # removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')
    
    # multiplication algorithm
    partial_products = [] # initialize empty container to store partial products
    
    i = 0 # index of the current binary bit of string 'a' beginning at 0, right-to-left
    for bit in reversed(a):
        if bit == '1':
          # FIXME: See next line
          partial_products.append(b+('0'*i))
        i += 1

    result = '0'
    while len(partial_products) > 0:
        # FIXME: See next line
        result = binary_add(result, partial_products[0])
        del partial_products[0]
    return result 

print(equiv_to(43, 23, -22, 0))