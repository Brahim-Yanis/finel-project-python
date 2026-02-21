"""
Quiz Game with Timer
A Python quiz game that asks multiple-choice questions with a time limit.
Uses only built-in modules (time, random, threading).
"""

import time
import random
import threading
import os

# Game Constants
TIME_LIMIT = 10  # seconds per question
HIGH_SCORES_FILE = "high_scores.txt"

# Quiz Questions Database
QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "choices": {"A": "London", "B": "Berlin", "C": "Paris", "D": "Madrid"},
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": {"A": "Venus", "B": "Mars", "C": "Jupiter", "D": "Saturn"},
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "What is the largest mammal in the world?",
        "choices": {"A": "Elephant", "B": "Giraffe", "C": "Blue Whale", "D": "Hippopotamus"},
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": {"A": "Vincent van Gogh", "B": "Pablo Picasso", "C": "Leonardo da Vinci", "D": "Michelangelo"},
        "answer": "C",
        "difficulty": "medium"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": {"A": "Go", "B": "Gd", "C": "Ag", "D": "Au"},
        "answer": "D",
        "difficulty": "medium"
    },
    {
        "question": "In which year did World War II end?",
        "choices": {"A": "1943", "B": "1944", "C": "1945", "D": "1946"},
        "answer": "C",
        "difficulty": "medium"
    },
    {
        "question": "What is the square root of 144?",
        "choices": {"A": "10", "B": "11", "C": "12", "D": "14"},
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "Which element has the atomic number 1?",
        "choices": {"A": "Helium", "B": "Hydrogen", "C": "Oxygen", "D": "Carbon"},
        "answer": "B",
        "difficulty": "medium"
    },
    {
        "question": "What is the longest river in the world?",
        "choices": {"A": "Amazon", "B": "Mississippi", "C": "Yangtze", "D": "Nile"},
        "answer": "D",
        "difficulty": "medium"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "choices": {"A": "Charles Dickens", "B": "William Shakespeare", "C": "Jane Austen", "D": "Mark Twain"},
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "What is the speed of light in km/s (approximately)?",
        "choices": {"A": "100,000", "B": "200,000", "C": "300,000", "D": "400,000"},
        "answer": "C",
        "difficulty": "hard"
    },
    {
        "question": "Which country has the largest population?",
        "choices": {"A": "USA", "B": "India", "C": "China", "D": "Indonesia"},
        "answer": "B",
        "difficulty": "medium"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "choices": {"A": "Gold", "B": "Iron", "C": "Diamond", "D": "Platinum"},
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "How many bones are in the adult human body?",
        "choices": {"A": "186", "B": "206", "C": "226", "D": "246"},
        "answer": "B",
        "difficulty": "hard"
    },
    {
        "question": "What programming language was Python named after?",
        "choices": {"A": "A snake", "B": "Monty Python", "C": "A Greek god", "D": "A mathematician"},
        "answer": "B",
        "difficulty": "medium"
    }
]


class QuizGame:
    """Main Quiz Game class with timer functionality."""
    
    def __init__(self):
        """Initialize the quiz game."""
        self.questions = QUESTIONS.copy()
        self.score = 0
        self.total_questions = 0
        self.correct_answers = 0
        self.timed_out_answers = 0
        self.wrong_answers = 0
        self.time_limit = TIME_LIMIT
        self.player_name = ""
        self.answer_received = False
        self.current_answer = None
        self.timer_expired = False
    
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self):
        """Print the game header."""
        print("=" * 60)
        print("           QUIZ GAME WITH TIMER")
        print("=" * 60)
        print()
    
    def print_separator(self):
        """Print a separator line."""
        print("-" * 60)
    
    def get_player_name(self):
        """Get the player's name."""
        self.clear_screen()
        self.print_header()
        self.player_name = input("Enter your name: ").strip()
        if not self.player_name:
            self.player_name = "Player"
        print(f"\nWelcome, {self.player_name}!")
    
    def show_menu(self):
        """Display the main menu and get user choice."""
        while True:
            self.clear_screen()
            self.print_header()
            print(f"Hello, {self.player_name}!")
            print()
            print("MAIN MENU")
            self.print_separator()
            print("1. Start Quiz (All Questions)")
            print("2. Start Quiz (Easy)")
            print("3. Start Quiz (Medium)")
            print("4. Start Quiz (Hard)")
            print("5. View High Scores")
            print("6. Change Time Limit (Current: {} seconds)".format(self.time_limit))
            print("7. Exit")
            self.print_separator()
            
            choice = input("\nEnter your choice (1-7): ").strip()
            
            if choice == "1":
                self.start_quiz()
            elif choice == "2":
                self.start_quiz("easy")
            elif choice == "3":
                self.start_quiz("medium")
            elif choice == "4":
                self.start_quiz("hard")
            elif choice == "5":
                self.view_high_scores()
            elif choice == "6":
                self.change_time_limit()
            elif choice == "7":
                self.clear_screen()
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")
                time.sleep(1)
    
    def change_time_limit(self):
        """Allow user to change the time limit per question."""
        self.clear_screen()
        self.print_header()
        print("CHANGE TIME LIMIT")
        self.print_separator()
        print(f"Current time limit: {self.time_limit} seconds")
        print()
        
        try:
            new_limit = int(input("Enter new time limit (5-60 seconds): ").strip())
            if 5 <= new_limit <= 60:
                self.time_limit = new_limit
                print(f"\nTime limit changed to {self.time_limit} seconds!")
            else:
                print("\nPlease enter a value between 5 and 60.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")
        
        input("\nPress Enter to continue...")
    
    def get_questions_by_difficulty(self, difficulty=None):
        """Get questions filtered by difficulty."""
        if difficulty is None:
            return self.questions.copy()
        return [q for q in self.questions if q["difficulty"] == difficulty]
    
    def input_with_timeout(self):
        """Get input with timeout using threading."""
        self.answer_received = False
        self.current_answer = None
        self.timer_expired = False
        
        def get_input():
            try:
                answer = input().strip().upper()
                if not self.timer_expired:
                    self.current_answer = answer
                    self.answer_received = True
            except EOFError:
                pass
        
        # Start input thread
        input_thread = threading.Thread(target=get_input, daemon=True)
        input_thread.start()
        
        # Wait for input or timeout
        start_time = time.time()
        while time.time() - start_time < self.time_limit:
            if self.answer_received:
                return self.current_answer
            
            # Display countdown every second
            remaining = int(self.time_limit - (time.time() - start_time))
            if remaining >= 0:
                print(f"\rTime remaining: {remaining:2d} seconds | Your answer (A/B/C/D): ", end="", flush=True)
            time.sleep(0.1)
        
        self.timer_expired = True
        return None
    
    def ask_question(self, question_data, question_num, total):
        """Ask a single question and return if answered correctly."""
        self.clear_screen()
        self.print_header()
        
        print(f"Question {question_num} of {total}")
        print(f"Difficulty: {question_data['difficulty'].upper()}")
        print(f"Time Limit: {self.time_limit} seconds")
        self.print_separator()
        print()
        print(f"Q: {question_data['question']}")
        print()
        
        # Display choices
        for letter, choice in question_data["choices"].items():
            print(f"   {letter}. {choice}")
        
        print()
        self.print_separator()
        
        # Get answer with timeout
        answer = self.input_with_timeout()
        
        print()  # New line after input
        
        correct_answer = question_data["answer"]
        correct_text = question_data["choices"][correct_answer]
        
        if answer is None:
            # Time ran out
            print("\n" + "!" * 60)
            print("  TIME'S UP! You ran out of time.")
            print(f"  The correct answer was: {correct_answer}. {correct_text}")
            print("!" * 60)
            self.timed_out_answers += 1
            return False
        elif answer == correct_answer:
            # Correct answer
            print("\n" + "*" * 60)
            print("  CORRECT! Great job!")
            print("*" * 60)
            self.correct_answers += 1
            return True
        elif answer in ["A", "B", "C", "D"]:
            # Wrong answer
            print("\n" + "X" * 60)
            print(f"  WRONG! You answered: {answer}")
            print(f"  The correct answer was: {correct_answer}. {correct_text}")
            print("X" * 60)
            self.wrong_answers += 1
            return False
        else:
            # Invalid input
            print("\n" + "?" * 60)
            print(f"  INVALID INPUT! '{answer}' is not a valid option.")
            print(f"  The correct answer was: {correct_answer}. {correct_text}")
            print("?" * 60)
            self.wrong_answers += 1
            return False
    
    def start_quiz(self, difficulty=None):
        """Start a quiz session."""
        # Get questions based on difficulty
        quiz_questions = self.get_questions_by_difficulty(difficulty)
        
        if not quiz_questions:
            print(f"\nNo questions available for {difficulty} difficulty!")
            input("\nPress Enter to continue...")
            return
        
        # Randomize question order
        random.shuffle(quiz_questions)
        
        # Reset counters
        self.score = 0
        self.correct_answers = 0
        self.wrong_answers = 0
        self.timed_out_answers = 0
        self.total_questions = len(quiz_questions)
        
        # Display quiz start message
        self.clear_screen()
        self.print_header()
        diff_text = difficulty.upper() if difficulty else "ALL"
        print(f"Starting Quiz: {diff_text} Questions")
        print(f"Total Questions: {self.total_questions}")
        print(f"Time per Question: {self.time_limit} seconds")
        self.print_separator()
        print("\nGet ready!")
        print("\nPress Enter to start...")
        input()
        
        # Ask each question
        for i, question in enumerate(quiz_questions, 1):
            if self.ask_question(question, i, self.total_questions):
                self.score += 1
            
            # Brief pause between questions
            if i < self.total_questions:
                print(f"\nCurrent Score: {self.score}/{i}")
                input("\nPress Enter for next question...")
        
        # Show final results
        self.show_results()
        
        # Save high score
        self.save_high_score()
        
        # Ask to retry
        self.ask_retry(difficulty)
    
    def show_results(self):
        """Display the final quiz results."""
        self.clear_screen()
        self.print_header()
        
        print("QUIZ COMPLETED!")
        self.print_separator()
        print()
        print(f"Player: {self.player_name}")
        print()
        print("FINAL RESULTS")
        print("-" * 40)
        print(f"  Total Questions:    {self.total_questions}")
        print(f"  Correct Answers:    {self.correct_answers}")
        print(f"  Wrong Answers:      {self.wrong_answers}")
        print(f"  Timed Out:          {self.timed_out_answers}")
        print("-" * 40)
        print(f"  FINAL SCORE:        {self.score}/{self.total_questions}")
        
        # Calculate percentage
        percentage = (self.score / self.total_questions) * 100 if self.total_questions > 0 else 0
        print(f"  PERCENTAGE:         {percentage:.1f}%")
        print("-" * 40)
        
        # Display grade/message based on score
        print()
        if percentage == 100:
            print("  PERFECT SCORE! You're a genius!")
        elif percentage >= 80:
            print("  EXCELLENT! Great knowledge!")
        elif percentage >= 60:
            print("  GOOD JOB! Keep learning!")
        elif percentage >= 40:
            print("  NOT BAD! Room for improvement.")
        else:
            print("  KEEP TRYING! Practice makes perfect!")
        
        self.print_separator()
    
    def save_high_score(self):
        """Save the high score to a file."""
        try:
            percentage = (self.score / self.total_questions) * 100 if self.total_questions > 0 else 0
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            
            with open(HIGH_SCORES_FILE, "a") as f:
                f.write(f"{self.player_name},{self.score},{self.total_questions},{percentage:.1f},{timestamp}\n")
            
            print("\nScore saved to high scores!")
        except Exception as e:
            print(f"\nCould not save score: {e}")
    
    def view_high_scores(self):
        """View saved high scores."""
        self.clear_screen()
        self.print_header()
        print("HIGH SCORES")
        self.print_separator()
        
        try:
            with open(HIGH_SCORES_FILE, "r") as f:
                lines = f.readlines()
            
            if not lines:
                print("\nNo high scores recorded yet!")
            else:
                # Parse and sort scores
                scores = []
                for line in lines:
                    parts = line.strip().split(",")
                    if len(parts) >= 5:
                        name, score, total, percentage, timestamp = parts[0], parts[1], parts[2], parts[3], parts[4]
                        scores.append({
                            "name": name,
                            "score": int(score),
                            "total": int(total),
                            "percentage": float(percentage),
                            "timestamp": timestamp
                        })
                
                # Sort by percentage (highest first)
                scores.sort(key=lambda x: x["percentage"], reverse=True)
                
                # Display top 10 scores
                print()
                print(f"{'Rank':<6}{'Name':<15}{'Score':<12}{'Percentage':<12}{'Date'}")
                print("-" * 60)
                
                for i, s in enumerate(scores[:10], 1):
                    print(f"{i:<6}{s['name']:<15}{s['score']}/{s['total']:<9}{s['percentage']:.1f}%{'':<7}{s['timestamp']}")
                
                if len(scores) > 10:
                    print(f"\n... and {len(scores) - 10} more scores")
        
        except FileNotFoundError:
            print("\nNo high scores recorded yet!")
        except Exception as e:
            print(f"\nError reading high scores: {e}")
        
        input("\nPress Enter to continue...")
    
    def ask_retry(self, difficulty=None):
        """Ask the player if they want to retry the quiz."""
        print()
        retry = input("Would you like to play again? (Y/N): ").strip().upper()
        
        if retry == "Y":
            self.start_quiz(difficulty)
    
    def run(self):
        """Run the quiz game."""
        self.get_player_name()
        self.show_menu()


def main():
    """Entry point for the quiz game."""
    game = QuizGame()
    game.run()


if __name__ == "__main__":
    main()
