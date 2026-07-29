def arcade_score():
    while True:
        score = input("Enter your score or type 'stop': ")

        if score == "stop".strip().lower():
            print("Game session ended!")
            break

        results = int(score)

        if results > 100:
            print("Wow! That is a new high score!")
        else:
            print("Good try, keep playing!")

arcade_score()