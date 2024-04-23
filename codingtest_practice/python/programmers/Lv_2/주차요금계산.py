"""
fees	records	result
[180, 5000, 10, 600]	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	[14600, 34400, 5000]
[120, 0, 60, 591]	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	[0, 591]
[1, 461, 1, 10]	["00:00 1234 IN"]	[14841]
"""
import math 

def solution(fees, records):
    def minute(time):
        h, m = time.split(":")
        ttl = int(h) * 60 + int(m)
        return ttl
    answer = []
    car_check = []
    res =[]
    for i in records:
        clock, num, car = i.split()
        total = minute(clock)
        if car == "IN" and num not in car_check:
            car_check.append(num)
            res.append([total, num, car, 0])
        elif car == "OUT":
            for j in res:
                if j[1] == num:
                    j[3] += total - j[0]
                    j[0] = 0
        elif car == "IN" and num in car_check:
            for j in res:
                if j[1] == num:
                    j[0] = total

    for i in res:
        if i[0] != 0 or i[3] == 0:
            i[3] += 1439 - i[0]

    res.sort(key=lambda x:x[1])
    for i in res:
        if i[3] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((i[3]-fees[0])/fees[2])*fees[3])

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))