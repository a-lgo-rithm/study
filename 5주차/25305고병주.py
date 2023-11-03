arr = []

n , k = map(int, input().split())

score = input().split()
score = list(map(int , score))
score.sort(reverse=True)

print(score[k-1])