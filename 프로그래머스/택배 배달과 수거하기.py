def solution(cap, n, deliveries, pickups):
    answer = 0
    sum = 0
    delivery = 0
    pickup = 0
    for i in range(n):
        delivery += deliveries[n-i-1] #마지막 값부터 반복하도록
        pickup += pickups[n-i-1]
        
        while delivery > 0 or pickup > 0:
            delivery -= cap
            pickup -= cap
            answer += (n-i) *2
    return answer