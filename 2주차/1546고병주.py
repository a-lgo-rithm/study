test = int(input())
score = list(map(int, input().split()))
maxScore = max(score)

scoreList = []
for i in score:
    scoreList.append(i/maxScore * 100)

average = sum(scoreList)/test
print(average)