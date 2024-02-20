name = input("What is your name: ")

with open("/home/vee/Personal/15-Days-of-Python/day-07/Submission/user_info.txt", "a") as f:
    f.write(f"{name}\n")
    f.close()