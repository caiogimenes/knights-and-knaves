from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
sentence0 = Symbol("A is both")
knowledge0 = And(
    # From the rules
    Or(AKnight, AKnave),
    Implication(AKnight, sentence0),
    Implication(AKnave, Not(sentence0)),
    # From the puzzle
    Implication(sentence0, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
sentence1_a = Symbol("A and B knaves")
knowledge1 = And(
    # From the rules
    And(Or(AKnight, AKnave), Or(BKnight, BKnave)),
    Biconditional(AKnight, sentence1_a),
    Implication(AKnave, Not(sentence1_a)),
    # From the puzzle
    Biconditional(sentence1_a, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
sentence2_a = Symbol("Same kind")
sentence2_b = Symbol("Different kind")
knowledge2 = And(
    # From the rules
    And(Or(AKnight, AKnave), Or(BKnight, BKnave)),
    Biconditional(AKnight, sentence2_a),
    Implication(AKnave, Not(sentence2_a)),
    Biconditional(BKnight, sentence2_b),
    Implication(BKnave, Not(sentence2_b)),
    # From the puzzle
    Biconditional(sentence2_a, And(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Biconditional(sentence2_b, And(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
sentence3_a = Symbol("A said knight")
sentence3_a_2 = Symbol("A said knave")
sentence3_b = Symbol("B said A said knave")
sentence3_b_2 = Symbol("C is knave")
sentence3_c = Symbol("A is knight")
knowledge3 = And(
    # From the rules
    And(Or(AKnight, AKnave), Or(BKnight, BKnave), Or(CKnight, CKnave)),
    Biconditional(AKnight, sentence3_a),
    Implication(AKnave, Not(sentence3_a)),
    Biconditional(AKnight, sentence3_a_2),
    Implication(AKnave, Not(sentence3_a_2)),
    Biconditional(BKnight, sentence3_b),
    Implication(BKnave, Not(sentence3_b)),
    Biconditional(CKnight, sentence3_c),
    Implication(CKnave, Not(sentence3_c)),
    # From the puzzle
    Or(sentence3_a, sentence3_a_2),
    Biconditional(sentence3_b, Not(sentence3_a)),
    Implication(sentence3_b, sentence3_a_2),
    Biconditional(sentence3_b_2, CKnave),
    Implication(Not(sentence3_b_2), CKnight),
    Biconditional(sentence3_c, AKnight),
    Implication(Not(sentence3_c), AKnave)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
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
