def solution(str1, str2):
    answer = 0
    set_str = set()
    str1_dict = {}
    str2_dict = {}
    for i in range(0, len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            atom = str1[i:i+2].lower()
            set_str.add(atom)
            if atom not in str1_dict.keys():
                str1_dict[atom] = 1
            else:
                str1_dict[atom] += 1
    for i in range(0, len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            atom = str2[i:i+2].lower()
            set_str.add(atom)
            if atom not in str2_dict.keys():
                str2_dict[atom] = 1
            else:
                str2_dict[atom] += 1
    inter_cnt = 0
    sum_cnt = 0
    lst_str = list(set_str)
    for i in range(len(lst_str)):
        if lst_str[i] in str1_dict.keys() and lst_str[i] in str2_dict.keys():
            sum_cnt += max(str1_dict[lst_str[i]], str2_dict[lst_str[i]])
            inter_cnt += min(str1_dict[lst_str[i]], str2_dict[lst_str[i]])
        elif lst_str[i] in str1_dict.keys() and lst_str[i] not in str2_dict.keys():
            sum_cnt += str1_dict[lst_str[i]]
        elif lst_str[i] not in str1_dict.keys() and lst_str[i] in str2_dict.keys():
            sum_cnt += str2_dict[lst_str[i]]
    
    if sum_cnt == 0:
        answer = 65536
    else:
        answer = int(inter_cnt / (sum_cnt) * 65536)
    return answer