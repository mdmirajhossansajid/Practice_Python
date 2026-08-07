s = input()
words = s.split()
count = 0
keywords = ["ai", "data", "model", "learn", "train", "neural"]
for word in keywords:
    if word in words:
        count += 1

if count >= 2:
    print("AI Detected")
else:
    print("Not AI Related")