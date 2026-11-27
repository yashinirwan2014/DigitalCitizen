import csv
from pathlib import Path
from datetime import datetime

QUESTIONS = [
 ("A message asks for your one-time password to claim a prize. What should you do?", ["Share it", "Do not share it and verify through the official service", "Post it publicly"], 1, "A one-time password is private. Do not share it."),
 ("A forwarded message makes a surprising claim. What is a responsible step?", ["Forward immediately", "Check reliable sources first", "Assume it is true"], 1, "Verify information before sharing it."),
 ("Which password habit is safer?", ["Reuse one password everywhere", "Use unique long passwords", "Tell a friend"], 1, "Unique passwords help limit the impact of an exposed account."),
 ("A group chat is mocking someone. What should you do?", ["Join in", "Spread screenshots", "Do not amplify it and seek trusted help"], 2, "Do not spread harmful content. Seek appropriate support."),
 ("What is a digital footprint?", ["Only profile pictures", "Records left through online activity", "Only public posts"], 1, "Posts, comments and other online activity can leave records.")
]
HISTORY = Path("data/quiz_history.csv")

def run_quiz():
    score = 0
    for number, (question, options, answer, explanation) in enumerate(QUESTIONS, 1):
        print(f"\n{number}. {question}")
        for i, option in enumerate(options, 1):
            print(i, option)
        try:
            choice = int(input("Answer number: ")) - 1
        except ValueError:
            choice = -1
        if choice == answer:
            score += 1
            print("Correct.")
        else:
            print("Suggested answer:", options[answer])
        print(explanation)
    HISTORY.parent.mkdir(parents=True, exist_ok=True)
    new_file = not HISTORY.exists()
    with open(HISTORY, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["date", "score", "total"])
        writer.writerow([datetime.now().isoformat(timespec="minutes"), score, len(QUESTIONS)])
    print("Final score:", score, "/", len(QUESTIONS))

def show_history():
    if not HISTORY.exists():
        print("No saved attempts.")
        return
    with open(HISTORY, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            print(row["date"], row["score"] + "/" + row["total"])

def main():
    while True:
        print("\nDIGITALCITIZEN: 1 Start quiz | 2 History | 0 Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            run_quiz()
        elif choice == "2":
            show_history()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()