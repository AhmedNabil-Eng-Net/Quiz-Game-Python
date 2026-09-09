# 🧠 Quiz Game 🎮

A simple command-line quiz game built with Python.

## ✨ Features

* ❓ Multiple-choice questions
* 🔤 Answer using `A`, `B`, `C`, or `D`
* ✅ Instant feedback for correct and wrong answers
* 🏆 Score tracking
* 📊 Final score and percentage
* ⚠️ Input validation
* 🔄 Easy to add new questions

## 🛠️ Technologies

* Python
* Lists
* Dictionaries
* Loops
* Conditional Statements
* `enumerate()`
* String Methods
* Input Validation

## 🚀 How to Run

Make sure Python is installed on your computer.

Run the game with:

```bash
main.py
```

## 🎮 How to Play

The game displays a question with four possible answers.

Choose your answer by entering:

```text
A
B
C
D
```

For example:

```text
1- Which is the largest ocean on Earth?

A. Atlantic Ocean
B. Indian Ocean
C. Pacific Ocean
D. Arctic Ocean

👉 Choose an answer (A/B/C/D): C

✅ Correct Answer! Well done! 🎉
```

At the end of the quiz, your final score and percentage are displayed:

```text
✨ Quiz Finished! ✨

🏆 Your Score: 4/4
📊 Your Percentage: 100%
```

## ➕ Adding New Questions

You can easily add more questions to the `questions` list.

Example:

```python
questions.append({
    "question": "Which planet is known as the Red Planet?",
    "options": [
        "A. Earth",
        "B. Mars",
        "C. Jupiter",
        "D. Venus"
    ],
    "answer": "B"
})
```

## 📚 What I Practiced

This project helped me practice:

* Lists and dictionaries
* Nested data structures
* `for` and `while` loops
* `if / else` statements
* `enumerate()`
* `.upper()` and `.strip()`
* Input validation
* Basic score calculation
* Percentage calculation
* Working with the `time` module

## 👨‍💻 Author

  **Ahmed Nabil**
