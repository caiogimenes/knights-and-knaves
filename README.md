# Knights and Knaves Puzzles Solver

This repository contains a script to solve variations of the classic Knights and Knaves logic puzzles using propositional logic. In these puzzles, knights always tell the truth and knaves always lie. You will encounter different puzzles where characters make statements, and you must determine whether each character is a knight or a knave.

## Dependencies

- Python 3.x
- The `logic.py` library file from the [CS50’s Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/2023/) course by Harvard University..

## Usage

1. Clone the repository to your local machine.
```bash
git clone https://github.com/yourusername/knights-and-knaves.git
cd knights-and-knaves
```

2. Ensure you have the `logic.py` library file from the CS50 AI course in the same directory as the script.

3. Run the script using Python.
```bash
python script.py
```

4. The script will output the solutions to the specified puzzles, indicating whether each character is a knight or a knave.

## Code Overview

The script defines symbols to represent whether each character (A, B, and C) is a knight or a knave. It then constructs knowledge bases for each puzzle using the statements made by the characters. The `main` function iterates through each puzzle, checking the knowledge base against each possible assignment of truth values to the symbols to find solutions that satisfy the knowledge base.

Here's a brief explanation of the major components of the code:

- Symbols are defined using the `Symbol` class from the `logic.py` library:
```python
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")
# ... and so on for B and C
```

- Knowledge bases are constructed using logical operators (`And`, `Or`, `Implication`, and `Biconditional`) to represent the rules of the puzzles and the statements made by the characters:
```python
knowledge0 = And(
    # From the rules
    Or(AKnight, AKnave),
    Implication(AKnight, sentence0),
    Implication(AKnave, Not(sentence0)),
    # From the puzzle
    Implication(sentence0, And(AKnight, AKnave))
)
# ... and so on for other puzzles
```

- The `main` function iterates through each puzzle, checking the knowledge base against each possible assignment of truth values to the symbols using the `model_check` function from the `logic.py` library:
```python
def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        # ... and so on for other puzzles
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")

if __name__ == "__main__":
    main()
```

## License

[MIT](LICENSE)
