n, m = map(int, input().split())

cards = list(map(int, input().split()))

# 매번 오름차순으로 정렬하면 항상 제일 앞 두 숫자가 최소가 됨
for i in range(m):
    cards.sort()

    cards[0] = cards[1] = cards[0] + cards[1]

print(sum(cards))