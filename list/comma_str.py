def comma(list):
    res = ""
    for i in range(0, len(list) - 1):
        res+=list[i]+','
    res+='and'+list[len(list) - 1]
    return res

list = ['apples', 'bananas', 'tofu', 'cats']
print(comma(list))