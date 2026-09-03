"""[LEARNING LOGS] BigFrame"""
maximum = 0
ans = []
def main():
    """find max"""
for _ in range(5):
    text = input().strip()
    ans.append(text)
    if len(text) > maximum:
        maximum = len(text)
frame = maximum + 4
print("*" * frame)
for text in ans:
    print(f"* {text.ljust(maximum)} *")
print("*" * frame)
main()
