
#  using pre-built python library : itertools 

# import itertools as it 

# s = 'ABC'
    
# nums = list(s)
# permutations = list(it.permutations(nums))
 
# # Output: ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
# print([''.join(permutation) for permutation in permutations])



## ----------------

## without using pre-built python library 

# # Function to swap two characters in a character array
# def swap(ch, i, j):
#     temp = ch[i]
#     ch[i] = ch[j]
#     ch[j] = temp
 
 
# # Recursive function to generate all permutations of a string
# def permutations(ch, curr_index=0):
 
#     if curr_index == len(ch) - 1:
#         print(''.join(ch))
 
#     for i in range(curr_index, len(ch)):
#         swap(ch, curr_index, i)
#         permutations(ch, curr_index + 1)
#         swap(ch, curr_index, i)
 
 
# if __name__ == '__main__':
 
#     s = 'ABC'
#     permutations(list(s))
 
## ----------------

## without using pre-built python library -- Version 2

# Recursive function to generate all permutations of a string
def permutations(remaining, candidate=''):
 
    if len(remaining) == 0:
        print(candidate)
 
    for i in range(len(remaining)):
 
        newCandidate = candidate + remaining[i]
        newRemaining = remaining[0:i] + remaining[i+1:]
 
        permutations(newRemaining, newCandidate)
 
 
if __name__ == '__main__':
 
    s = 'ABC'
    permutations(s)

