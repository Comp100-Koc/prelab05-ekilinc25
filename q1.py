def longest_palindromic_substring(s):
    string = ''
    longest = ''
    for i in range(len(s)):
        for char in s[i::]:
            if string == string[::-1] and len(string) > len(longest) and len(string) > 1:
                longest = string
            string += char
        string = ''
    return longest