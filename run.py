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


def print_question(q_number):
    """
    Print question and options from the sheet and request answer input
    """
    data = SHEET.worksheet('Questions').get_all_values()
    headings = data[0]
    questions = data[q_number]

    while True:
        for heading, question in zip(headings, questions):
            print(f'{heading}: {question}')

        print('A, B, C or D')
        user_ans = input('Answer: ')

        if validate_ans(user_ans):
            break

    return user_ans


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


print_question(1)
print_question(2)
