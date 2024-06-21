nums = [4,1,2,1,2]

# Method One
s = {}

for ele in nums:
    if ele in s:
        s[ele] += 1
    else:
        s[ele] = 1

for key, val in s.items():
    if val == 1:
        print(key)
        break

# Method Two using xor

"""
XOR property
XOR of two same numbers is always 0 i.e. a ^ a = 0. ←Property 1.
XOR of a number with 0 will result in the number itself i.e. 0 ^ a = a.  ←Property 2
"""

# Approach
# We will just perform the XOR of all elements of the array using a loop and the final XOR will be the answer.
"""
1. XOR all the elements of the array.
2. XOR of two same numbers is always 0 i.e. a ^ a = 0.
3. XOR of a number with 0 will result in the number itself i.e. 0 ^ a = a.
4. XOR of two different numbers is non-zero i.e. a ^ b!= 0.
"""

xor = 0

for ele in nums:
    xor ^= ele

print(xor)