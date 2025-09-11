n, w, l = list(map(int, input().split()))
weight = list(map(int, input().split()))

bridge = [0] * w
time = 0 
while bridge:
    time += 1
    bridge.pop(0)
    if weight:
        # 현재 다리 위 무게 + 트럭 무게 <= 다리 최대 하중
        if sum(bridge) + weight[0] <= l:
            # 가능하면 현재 트럭 무게 큐에 저장
            bridge.append(weight.pop(0))
        else:
            # 불가능하면 0
            bridge.append(0)

print(time)