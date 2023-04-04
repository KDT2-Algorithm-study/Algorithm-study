def solution(absolutes, signs):
    return sum([x if y else -x for x, y in zip(absolutes, signs)])