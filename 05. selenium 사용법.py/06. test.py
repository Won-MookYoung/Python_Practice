def text_to_num(text):
    #숫자로 변경
    text=text.replace('조회수', '').replace('회','').strip()
    if '억' in text:
        num=float(text.replace('억',''))*100000000
    elif '만' in text:
        num=float(text.replace('만',''))*10000
    elif '천' in text:
        num=float(text.replace('천',''))*1000
    elif '없음'== text:
        num=0
    else:
        num=int(text)

    return num

print(text_to_num('조회수 7천회'))
print(text_to_num('조회수 70만회'))   # 700000
print(text_to_num('조회수 220만회'))   #2200000
print(text_to_num('조회수 3450만회'))   # 34500000
print(text_to_num('조회수 1.5억회'))
print(text_to_num('조회수 156회'))
print(text_to_num('조회수 없음'))

