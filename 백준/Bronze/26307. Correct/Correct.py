from datetime import datetime

start = datetime.strptime("09:00", "%H:%M")
h, m = map(int, input().split())
end = datetime.strptime(f"{h}:{m}", "%H:%M")
print(((end-start) // 60).seconds)