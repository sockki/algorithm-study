def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    while bridge:
        a = bridge.pop(0)
        answer += 1
        weight += a
        if truck_weights:
            if truck_weights[0] <= weight:
                b = truck_weights.pop(0)
                bridge.append(b)
                weight -= b
            else:
                bridge.append(0)
    return answer