class CascadingPalindrome:
  def __init__(self):
    # the varible to be used to store the results
    self.parameter = []

  #  check if the parameter is a palindrome
  def isPalindrome(self, word):
    return word == word[::-1]

  #  check if the parameter is satisfy the cascading conditions
  def checkCascading(self, words):
    try:
    # splitting the words into a list of words
      for word in words.split():

        # check if the word in the list is a palindrome
        if self.isPalindrome(word):
            self.parameter.append(word)

        result = " ".join(self.parameter)
        return result if result else "This does not have a palindrome in it."

    except AttributeError:
      return "Only a parameter of the string type is supported."

# time complexity: O(N)
# space complexity: O(N)
word1 = CascadingPalindrome().checkCascading("1230321")
word2 = CascadingPalindrome().checkCascading("1230321 09234 0124210")
word3 = CascadingPalindrome().checkCascading("abcd5dcba 1230321 09234 0124210")

# this ensures that the function returns the correct output when the parameter is not a string
word4 = CascadingPalindrome().checkCascading({})

# this ensures that the function returns the correct output when the parameter is not a string
word5 = CascadingPalindrome().checkCascading([])

word6 = CascadingPalindrome().checkCascading("racecar")
word7 = CascadingPalindrome().checkCascading("madam")

# this ensures that the function returns the correct output when the parameter is not a string
word8 = CascadingPalindrome().checkCascading(1)

# this ensures that the function returns the correct output when the parameter is not a palindrome
word9 = CascadingPalindrome().checkCascading("king")
word10 = CascadingPalindrome().checkCascading("01.121")

print(word1)
print(word2)
print(word3)
print(word4)
print(word5)
print(word6)
print(word7)
print(word8)
print(word9)
print(word10)