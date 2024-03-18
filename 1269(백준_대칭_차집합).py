a, b = map(int, input().split())

aa = set(map(int, input().split()))
bb = set(map(int, input().split()))

print(abs(len(aa - bb)) + abs(len(bb - aa)))
