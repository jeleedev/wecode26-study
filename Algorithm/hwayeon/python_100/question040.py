# 놀이동산에 가자

# 테마파크에 온 원범이와 친구들은 놀이기구를 타려고 합니다. 모든 놀이기구는 한번에 타는 인원수에는 제한이 없지만 제한 무게를 넘으면 무조건 다음 기구를 타야 합니다. 

# 원범이와 친구들이 총 몇 명 탈 수 있는지 알 수 있는 프로그램을 작성해 주세요.

# 첫번째 줄에서 제한 무게가 주어지고 두번째 줄에서는 함께한 친구들의 수 n이 주어집니다. 
# 그 다음 차례대로 탑승할 친구들의 몸무게가 주어집니다. 몸무게는 무작위로 주어집니다.

# 단, 놀이기구는 선착순으로만 탈 수 있습니다.
# 두 명 이상의 인원이 항상 탑승합니다.

# 입력
50
5
20
20
20
20
20

# 출력
# 2

# 답안
limit = int(input())
num = int(input())
l = [int(input()) for i in range(num)]

weight = 0
for i in range(num):
    if weight > limit:
        print(i-1)
        break    
    else:
        weight += l[i]

# 답안
total = 0
count = 0
limit = int(input('제한무게는 얼마인가요? : '))
n = int(input('몇명이 탈 수 있나요? : '))

for i in range(n):
    total += int(input('몸무게를 입력해주세요 : '))
    if total <= limit:
        count += 1
        
print(count)