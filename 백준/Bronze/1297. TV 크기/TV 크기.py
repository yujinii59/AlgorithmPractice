d, h, w = map(int, input().split())
d_rate = d / (h ** 2 + w ** 2) ** 0.5
print(int(h * d_rate), int(w * d_rate))