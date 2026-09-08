
# ------------- # -- 🧠 QUIZ GAME 🎮 -- # ------------- #

# To create some delay to simulate the natural program response
import time

# 📚 Questions
questions = [
    {
        "question": "Which is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"],
        "answer": "C" # ✅ Correct Answer
    },
    {
        "question": "What is the capital city of France?",
        "options": ["A. Madrid", "B. Paris", "C. Rome", "D. Berlin"],
        "answer": "B"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["A. 5", "B. 6", "C. 8", "D. 7"],
        "answer": "D"
    },
    {
        "question": "What is the chemical symbol for Gold?",
        "options": ["A. Au", "B. Ag", "C. Fe", "D. Hg"],
        "answer": "A"
    }
]

# 📚 If you want to add another question:
# questions.append({
#     "question": "Which planet is known as the Red Planet?",
#     "options": [
#         "A. Earth",
#         "B. Mars",
#         "C. Jupiter",
#         "D. Venus"
#     ],
#     "answer": "B"
# })


# ──────────────────────────────────────────────────
# 🎨 Visual divider
# ──────────────────────────────────────────────────
divider = "# " + "-" * 50 + " #"


# 🏆 Score counter
score = 0


# 🔄 Loop through all quiz questions
for i, quiz in enumerate(questions, start=1):
    question = quiz["question"]
    options = quiz["options"]
    answer = quiz["answer"]

    # ❓ Display the question number and question
    print(f"\n{i}- {question}")
    print(divider)

    # 🔁 Keep asking until the user enters a valid answer
    while True:

        # 📋 Display the answer options
        for option in options:
            print(option)

        print(divider)

        # ⌨️ Get the user's answer
        guess = input("👉 Choose an answer (A/B/C/D): ").upper().strip()

        # ✅ Check if the answer is valid
        if guess in ("A", "B", "C", "D"):
            break

        # ⚠️ Invalid input
        print("⚠️ Invalid choice! Please choose A, B, C, or D.")
        print(divider) # 🎨 Visual divider
        time.sleep(0.6)

    # 🎯 Check if the answer is correct
    if guess == answer:

        print("✅ Correct Answer! Well done! 🎉")

        # ➕ Increase score
        score += 1

    else:
        print(f"❌ Wrong Answer! The correct answer is: {answer}")

    print(divider)

    # ⏳ Small delay before showing the next question
    time.sleep(0.6)


# 📊 Calculate the final percentage
percentage = int((score / len(questions)) * 100)

# ✅ Quiz Finished!
print("✨ Quiz Finished! ✨")

# ⏳ Small delay before showing the result
time.sleep(0.6)

# 🏁 Final Result
print(
      f"🏆 Your Score: {score}/{len(questions)}\n"
      f"📊 Your Percentage: {percentage}%"
     )

print(divider) # 🎨 Visual divider
# ---------------------------------------------------- #
