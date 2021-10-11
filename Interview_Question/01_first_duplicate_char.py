# Deteksi char yang duplikasi
def duplicate_detect(string_1):
    dict_1 = {}
    for i in range(len(string_1)):
        if string_1[i] in dict_1:
            return string_1[i]
        dict_1[string_1[i]] = 1 


res = duplicate_detect("ABCA")
print(res)




