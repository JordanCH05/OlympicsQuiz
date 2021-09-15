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
    print('Retrieving questions...')
    data = SHEET.worksheet('Questions').get_all_values()
    headings = data[0]
    options = data[question]

    while True:
        print('\n')
        for heading, option in zip(headings, options):
            print(f'{heading}: {option}')

        print('A, B, C or D')
        print('Q to quit or R to restart')
        user_ans = input('Answer: \n')
        user_ans = user_ans.strip()
        user_ans = user_ans.capitalize()

        if validate_ans(user_ans):
            break

    return check_answer(user_ans, question, score)


def validate_ans(answer):
    """
    If values are not A, B, C or D then raise a ValueError
    """
    print('Validating answer...')
    try:
        if answer in ('A', 'B', 'C', 'D'):
            print('Valid answer\n')
        elif answer in ('Q', 'Quit'):
            end_program('quit')
            return False
        elif answer in ('R', 'Restart'):
            end_program('restart')
            return False
        else:
            raise ValueError(
                f"{answer} is an invalid answer"
            )
    except ValueError as e:
        print(f'\nError: {e}, please answer with A, B, C or D')
        return False

    return True


def end_program(type):
    while True:
        if type == 'try again':
            sure = input('\nWould you like to try again? Y/N: \n')
        else:
            sure = input(f'\nAre you sure you want to {type}? Y/N: \n')
        sure = sure.strip()
        sure = sure.capitalize()
        if sure in ('Y', 'Yes'):
            if type in ('restart', 'try again'):
                print('Restarting...')
                main()
            elif type == 'quit':
                print('Quitting...')
                quit('Goodbye')
        elif sure in ('N', 'No'):
            break


def check_answer(user_ans, question, score):
    """
    Check if the users answer matches the correct answer in the google sheet
    """
    print('Checking answer...')

    correct_answers = SHEET.worksheet('Answers').get_all_values()
    correct_answer = correct_answers[question][0]

    if user_ans == correct_answer:
        print('You were right!\n')
        score += 1
    else:
        print(f'Sorry, {correct_answer} is the correct answer\n')

    print(f'Current Score: {score}')
    return score


def record_score(score):
    """
    Records username and score then adds it to google sheet.
    The usernames and scores are then sorted highest first.
    """
    print('\nYou completed the quiz!\n')
    print(f'You scored {score} out of 10\n')
    if score == 10:
        print('Wow a perfect score!')
    elif score in range(8, 10):
        print('Wow you really know your stuff')
    elif score in range(6, 8):
        print('Nice')
    elif score == 5:
        print('Halfway there!')
    elif score in range(3, 5):
        print('Better luck next time')
    else:
        print('Did you even watch the Olympics?')
    username = input('\nEnter your name: \n')

    highscores = SHEET.worksheet('Highscores')
    highscores.append_row([username, score])

    hs_list = highscores.get_all_values()
    hs_list.sort(key=lambda hs_list: int(hs_list[1]), reverse=True)

    highscores.update('A1', hs_list)


def print_highscores():
    """
    Print Top 10 Highscores from google sheet
    """
    print('Getting highscores...')
    highscores = SHEET.worksheet('Highscores').get_all_values()

    print('\nHighscores')

    hs_length = len(highscores) if len(highscores) < 10 else 10
    for i in range(0, hs_length):
        print(f'{i+1}. {highscores[i][0]} : {highscores[i][1]}')


def main():
    """
    Run all program functions
    """
    print('\nWelcome to the 2021 Tokyo Olympics Quiz')
    score = 0
    for i in range(1, 11):
        score = print_question(i, score)
    record_score(score)
    print_highscores()
    end_program('try again')
    print('Goodbye')


main()
