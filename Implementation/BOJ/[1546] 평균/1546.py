N = int(input())
scores = list(map(int, input().split(" ")))

max = max(scores)
for i, score in enumerate(scores):
    scores[i] = score/max*100

print(sum(scores) / N)