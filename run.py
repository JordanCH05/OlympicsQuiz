import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Olympics Quiz')


def print_question(question, score):
    """
    Print question and options from the sheet and request answer input
    """
    data = SHEET.worksheet('Questions').get_all_values()
    headings = data[0]
    options = data[question]

    while True:
        for heading, option in zip(headings, options):
            print(f'{heading}: {option}')

        print('A, B, C or D')
        user_ans = input('Answer: ')

        if validate_ans(user_ans):
            break

    return check_answer(user_ans, question, score)


def validate_ans(answer):
    """
    If values are not A, B, C or D then raise a ValueError
    """
    try:
        if answer.capitalize() in ('A', 'B', 'C', 'D'):
            print('Valid answer\n')
        else:
            raise ValueError(
                f"{answer} is an invalid answer"
            )
    except ValueError as e:
        print(f'Error: {e}, please answer with A, B, C or D\n')
        return False

    return True


def check_answer(user_ans, question, score):
    """
    Check if the users answer matches the correct answer in the google sheet
    """
    correct_answers = SHEET.worksheet('Answers').get_all_values()
    correct_answer = correct_answers[question][0]

    if user_ans == correct_answer:
        print('You were right!\n')
        score += 1
    else:
        print(f'Sorry, {correct_answer} is the correct answer\n')

    print(f'Current Score: {score}\n')
    return score


def main():
    """
    Run all program functions
    """
    score = 0
    print('Welcome to the Olympics Quiz\n')
    for i in range(1, 11):
        score = print_question(i, score)


main()
