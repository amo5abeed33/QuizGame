# Quiz Application

A simple interactive **Quiz Application** built with Python and Tkinter. Users can answer a series of quiz questions, and their scores are calculated based on correct or incorrect answers.

---

## Features

- **Graphical Interface**: Built using Tkinter for an intuitive user experience.
- **Dynamic Scoring**:
  - Correct Answer: **+5 points**
  - Incorrect Answer: **-2 points**
- **Quiz Logic**: Contains 5 predefined quiz questions.
- **Score Evaluation**: Pass or fail based on 60% of the total score.
- **Play Again Option**: Restart the quiz after completion.

---

## Requirements

Make sure you have the following:

- **Python 3.x** installed.
- Required modules:
  - `tkinter` (Standard library with Python, no installation required).

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/quiz-application.git
   ```
2. Navigate to the project folder:
   ```bash
   cd quiz-application
   ```
3. Run the script:
   ```bash
   python quiz_app.py
   ```

---

## How to Play

1. Start the application by running the script.
2. A question will appear on the screen.
3. Type your answer in the input box and click **"Submit Answer"**.
4. You will get:
   - **5 points** for a correct answer.
   - **-2 points** for an incorrect answer.
5. After completing all questions, the app will display your score and whether you passed or failed.
6. You can choose to **play again** or **exit**.

---

## Example Questions

The following questions are included:
1. What is the full form of CPU? **(Answer: Central Processing Unit)**
2. Which gate gives low in both HIGH input? **(Answer: NAND)**
3. What does HTML stand for? **(Answer: HyperText Markup Language)**
4. What is the capital of USA? **(Answer: Washington DC)**
5. Who is known as the father of the computer? **(Answer: Charles Babbage)**

---

## Code Structure

- **Class `QuizApp`**: Handles the main logic of the quiz.
- **Methods**:
   - `check_answer()`: Validates the user's input and updates the score.
   - `show_result()`: Displays the final score and pass/fail message.
   - `reset_quiz()`: Resets the quiz for replay.
- **GUI Elements**:
   - Labels for questions and results.
   - Entry box for user input.
   - Buttons to submit answers.

---

## Future Enhancements

- Add more questions or randomize question order.
- Include a timer for each question.
- Store high scores or user history.

---

## Screenshot

![Quiz App Screenshot](https://via.placeholder.com/400x300.png?text=Quiz+App+Screenshot) *(Add actual screenshot here)*

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Feel free to fork this repository, improve the app, and submit a pull request.

---

## Author

**Your Name**

LinkedIn: [Your Profile](#) | GitHub: [Your Profile](#)

---

Enjoy playing the quiz! 
