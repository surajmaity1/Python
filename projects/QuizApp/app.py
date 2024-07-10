from Question import Question as q

question_list = [
    "What is the capital of India?:\na)Haldia, \nb)New Delhi, \nc)Chennai, \nd)Kolaghat\n\n",
    "What is the big river of India?:\na)Ganges, \nb)Sindhu, \nc)Godabory, \nd)Narmada\n\n",
    "What is the color of apple?:\na)Pink, \nb)Yellow, \nc)Green/Red, \nd)Purple\n\n"
]
right_answers = [
    q(question_list[0], "b"),
    q(question_list[1], "a"),
    q(question_list[2], "c")
]


def ask_questions(questions):
    total_score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            total_score += 1
    print(f"You got : {total_score}/ {len(questions)} correct.\nTry again.")


ask_questions(right_answers)