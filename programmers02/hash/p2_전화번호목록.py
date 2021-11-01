def solution(pb):
    pb.sort()

    for i in range(len(pb) - 1):
        n = len(pb[i])
        if pb[i] == pb[i + 1][:n]:
            return False

    return True