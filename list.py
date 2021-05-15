li = [3, 1, '배가', 4, '고파요', 5, 1]

#리스트 인덱싱
print(li[2])

#리스트 슬라이싱
print(li[0:2])

#리스트의 길이를 구해주는 내장함수 : len(리스트 변수)
print(len(li))

#리스트의 원소를 오름차순으로 정렬해주는 함수 : sort()
li2 = [3, 1, 4, 5, 2]
#print(li2.sort())
# li2.sort()
# print(li2)

# 참고 sort와 sorted
# print(sorted(li2))

# print(li2)
# li2.sort()
# print(li2)

# sort()로 내림차순 하는 법을 구글링해서 알아보기
li2.sort(reverse= True)
print(li2)

#리스트 내의 특정 원소 인덱스 반환해주는 함수 : 리스트변수.index()
print(li.index("배가"))

#리스트 내의 특정 원소의 갯수 세어주는 함수 : 리스트변수.count(요소)
print(li.count(1))