def remove_adjacent_duplicates(s):
    for _ in range(len(s)):
        temp = ''
        index = 0
        for i in s:
            temp += i
            if temp[index] == temp[index-1] and index > 0:
                s = s[0:index-1] + s[index+1::]
                break
            index += 1
        index = 0
        temp = ''
    return s