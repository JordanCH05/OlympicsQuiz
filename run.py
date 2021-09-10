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

    for heading, question in zip(headings, questions):
        print(f'{heading}: {question}')
    print('A, B, C or D')
    input('Answer: ')


print_question(1)