def solution(diffs, times, limit):
    def is_valid(a):
        time = 0
        for b in range(len(diffs)):
            if time > limit:
                return False
            if a >= diffs[b]:
                time += times[b]
            else:
                time += ((diffs[b] - a) * (times[b] + (times[b - 1] if b > 0 else 0)) + times[b])
        return time <= limit

    left, right = 1, max(diffs)
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if is_valid(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer
