fruit = { '배' : [2000, 3], '사과' : [1500, 5], '딸기' : [1800, 2], '참외' : [2300, 5]}
sum = 0
if (fruit['배'][1]) < 5 :
    sum = (5 - fruit['배'][1]) * fruit['배'][0]
    print("배", 5 - fruit['배'][1], "개를", (5 - fruit['배'][1]) * fruit['배'][0], '원에 사야 합니다.')
else :
    print("배는 안 사도 됩니다.")
if (fruit['사과'][1]) < 5 :
    sum += (5 - fruit['사과'][1]) * fruit['사과'][0]
    print("사과", 5 - fruit['사과'][1], "개를", (5 - fruit['사과'][1]) * fruit['사과'][0], '원에 사야 합니다.')
else :
    print("사과는 안 사도 됩니다.")
if (fruit['딸기'][1]) < 5 :
    sum += (5 - fruit['딸기'][1]) * fruit['딸기'][0]
    print("딸기", 5 - fruit['딸기'][1], "개를", (5 - fruit['딸기'][1]) * fruit['딸기'][0], '원에 사야 합니다.')
else :
    print("딸기는 안 사도 됩니다.")
if (fruit['참외'][1]) < 5 :
    sum += (5 - fruit['참외'][1]) * fruit['참외'][0]
    print("참외", 5 - fruit['참외'][1], "개를", (5 - fruit['참외'][1]) * fruit['참외'][0], '원에 사야 합니다.')
else :
    print("참외는 안 사도 됩니다.")
print("총합은", sum, '원 입니다.')

print("201710272 이상준 입니다.")
