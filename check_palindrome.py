
# Check if a single string is palindrome
def check_palindrome(string):
    if string == string[::-1]:
        return f"this string {string} is palindrome"
    else:
        return f" No this string {string} is not palindrome"
    
string = "121"
print(check_palindrome(string))

# Check palindromes in a list
def check_palindrome_in_list(list1):
  palindrome = []
  for num in list1:
      if str(num)==str(num)[::-1]:
        palindrome.append(num)
  return palindrome
list1 = [121,232,142,454,787,897]
print("list of palindrome ",check_palindrome_in_list(list1))
  
list1 = [121,232,142,454,787,897]
palindrome = []
for num in list1:
    if str(num)==str(num)[::-1]:
        palindrome.append(num)
    
print(palindrome)