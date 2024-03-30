#--------------------------------------------------------------------------------------
#--------------------------  Problem 1   ----------------------------------------------
#--------------------------------------------------------------------------------------
def fibonacci(n, remember = None):
    if remember is None:
        remember = dict()
    if n <= 2:
        return 1
    if n in remember:
        return remember[n]
    result = fibonacci(n-1, remember) + fibonacci(n-2, remember)

    remember[n] = result
    return result
print("\n=========== PROBLEM 1 TESTS ===========")
print(fibonacci(1))    # 1
print(fibonacci(2))    # 1
print(fibonacci(3))    # 2
print(fibonacci(4))    # 3
print(fibonacci(10))   # 55
print(fibonacci(100))  # 354224848179261915075 (This one will
                       # not work if you don't have the 
                       # 'remember' dictionary implemented).



#--------------------------------------------------------------------------------------
#--------------------------  Problem 2   ----------------------------------------------
#--------------------------------------------------------------------------------------
print("\n=========== PROBLEM 2 TESTS ===========")
def permutations(letters, word=""):

	if len(letters) == 0:   # Base Case
		print(word)  

	else:
		# Try adding each of the available letters
		# to the 'word_so_far' and add up all the
		# resulting permutations.

		for index in range(len(letters)):
			# Make a copy of the letters to pass to the
			# the next call to permutations.  We need
			# to remove the letter we just added before
			# we call permutations again.

			letters_left = letters[:]
			del letters_left[index]

			# Add the new letter to the word we have so far
			permutations(letters_left, word + letters[index])

permutations(list("ABC"))
""" 
Results:
ABC
ACB
BAC
BCA
CAB
CBA
"""
print("\n=========== Part 2 ===========")

permutations(list("ABCD"))
"""
Results:
ABCD
ABDC
ACBD
ACDB
ADBC
ADCB
BACD
BADC
BCAD
BCDA
BDAC
BDCA
CABD
CADB
CBAD
CBDA
CDAB
CDBA
DABC
DACB
DBAC
DBCA
DCAB
DCBA
"""
#--------------------------------------------------------------------------------------
#--------------------------  Problem 3   ----------------------------------------------
#--------------------------------------------------------------------------------------
# recursive algorithm is O(log n)
def binary_search(sorted_list, target):
    if len(sorted_list) == 1:
        return target == sorted_list[0]
    else:
        middle = len(sorted_list) // 2
        if target == sorted_list[middle]:
            return True
        elif target < sorted_list[middle]:
            # print(sorted_list[middle]) #shows how the list is split
            return binary_search(sorted_list[:middle], target)
        else:
            # print(sorted_list[middle]) #shows how the list is split
            return binary_search(sorted_list[middle:], target)

print("\n=========== test 3 ===========")
print(binary_search([1, 3, 6, 18, 20, 25, 34, 38, 89, 95, 99, 100], 89)) # True
print(binary_search([1, 3, 6, 18, 20, 25, 34, 38, 89, 95, 99, 100], 1))  # True
print(binary_search([1, 3, 6, 18, 20, 25, 34, 38, 89, 95, 99, 100], 17)) # False

#--------------------------------------------------------------------------------------
#--------------------------  key terms   ----------------------------------------------
#--------------------------------------------------------------------------------------
# base case - The scenario that will terminate (or stop) the recursive calls. If this is not designed properly, then the recursion will run forever.

# memoization - The technique of remembering previous results found through recursion so that repetitive recursion can be avoided.

# ecursion - The calling of a function with the same function. This can be used to solve problems by identifying a solution 
# which is written in terms of solving the same problem using smaller values. A base case is needed to ensure that the recursion 
# eventually stops. The base cases are solved in the function without using recursion.
