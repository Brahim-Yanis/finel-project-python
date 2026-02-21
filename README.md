# Quiz Game with Timer

A Python quiz game that asks multiple-choice questions with a countdown timer. Built using only Python built-in modules.

## Features

- **Multiple Choice Questions**: Each question has 4 options (A, B, C, D)
- **Timer**: 10-second countdown for each question (configurable)
- **Difficulty Levels**: Easy, Medium, Hard, or All questions
- **Score System**: +1 point for correct answers, 0 for wrong/timeout
- **Randomized Questions**: Questions appear in random order each game
- **High Scores**: Saves scores to a file for tracking progress
- **Retry Option**: Play again immediately after finishing
- **Percentage Display**: Shows your score as a percentage

## Controls

| Action | Input |
|--------|-------|
| Select Answer | Type A, B, C, or D |
| Menu Navigation | Type option number (1-7) |
| Continue | Press Enter |

## Installation

1. Make sure you have Python 3.x installed
2. No external dependencies required - uses only built-in modules!

## How to Run

```bash
python quiz_game.py
```

## Game Rules

1. Enter your name to begin
2. Choose quiz type from the menu:
   - All questions
   - Easy only
   - Medium only
   - Hard only
3. Answer each question by typing A, B, C, or D
4. You have 10 seconds (default) to answer each question
5. Time runs out = wrong answer
6. See your final score and percentage at the end

## Project Structure

```
finel-project-python/
├── quiz_game.py      # Main game file
├── high_scores.txt   # Saved scores (auto-created)
├── requirements.txt  # Python dependencies (none needed)
└── README.md         # This file
```

## Customization

You can adjust settings in `quiz_game.py`:

| Constant | Description | Default |
|----------|-------------|---------|
| `TIME_LIMIT` | Seconds per question | 10 |
| `HIGH_SCORES_FILE` | File to save scores | high_scores.txt |

### Adding More Questions

Add questions to the `QUESTIONS` list in this format:

```python
{
    "question": "Your question here?",
    "choices": {"A": "Option 1", "B": "Option 2", "C": "Option 3", "D": "Option 4"},
    "answer": "B",  # Correct answer letter
    "difficulty": "easy"  # easy, medium, or hard
}
```

## Skills Demonstrated

- Variables and data types
- Lists and dictionaries
- Loops (for, while)
- Conditional statements (if/else)
- Time handling with `time` module
- Threading for timer functionality
- User input validation
- File I/O for high scores
- Functions and classes
- String formatting
