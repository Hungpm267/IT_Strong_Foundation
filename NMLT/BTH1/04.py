a, b,c = map(int, input().split())

max = a if a > b else b
max = max if max > c else c

print(f'so lon nhat trong 3 so la: {max}')