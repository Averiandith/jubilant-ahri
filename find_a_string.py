def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        sliced = string[i:i + len(sub_string)]
        if sliced == sub_string:
            count += 1
    return count
