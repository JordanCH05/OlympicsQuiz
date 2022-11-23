# The Tokyo Olympics Quiz
The Tokyo Olympics Quiz is a Python terminal quiz, which runs in the Code Institute mock terminal on Heroku.

Users can test their Olympic knowledge from this year's Summer Olympics by answering 10 multiple choice questions about the Tokyo 2021 Olympic Games and compare their scores with other users in a ranked highscores list.

The live app can be found [here](https://tokyo-olympics-quiz.onrender.com)

![Responsive Mockup of site](images/responsive.png)

___

## User Experience

### User stories

As a user I would like to be able to...

* Record my score
* Compare my score to previous attempts
* Be told if I answered correctly after each question
* Quit or restart at any time
* Try again at the end of the quiz
### App Owner Stories
As the app owner I would like to...

* Disply the questions and multiple-choice options clearly
* Store all questions, answers and highscores in easy yo deal with sheets
* Tell the user when invalid inputs have been entered
* Tell the user which inputs are valid and how to quit and restart
* Ask the user "Are you sure?" to prevent unwanted quit or restart

___

## Flowchart

![Flowchart of the app](images/flowchart_snap.png)

___

## Features

### Existing Features

* Welcome message

    * To welcome the user and provide the name for the app
    * A "retrieving questions..." message to ensure the user that the app is loading up

    ![Welcome meassage](images/welcome.png)

* Question and options layout
    * Easy to read layout of Question and mutiple choice options underneath
    * Current Score

    ![Question and mutiple choice layout](images/question.png)

* Input instructions

    * Instructions to tell the user how to provide a valid input
    * Instrcutions on how to quit and restart

    ![Input instructions](images/instructions.png)

* Input Response

    * Instant feedback on answer
    * Current score counter

    ![Incorrect answer message](images/score.png)

    ![Correct score message](images/correct.png)

    * Error message for invalid inputs

    ![Error message](images/invalid.png)

    * "Are you sure?" message to prevent the user from doing an unwanted quit or restart
    * Also accepts whole words as user inputs ("yes", "no", "quit", "restart")

    !["Are you sure?" message](images/sure.png)

* After quiz

    * Final Score out of 10
    * Appropraite message based on performance
    * User can enter their name

    ![Final score and message](images/end.png)

    * Top 10 Highscores listed
    * Try again option

    ![Highscores list](images/highscore.png)

### Google Spreadsheet

* Questions and mutiple choice options
* Correct Answers
* Highscores

### Future Features

* A start input
* Allow user to access Highscores at the start of the quiz
* Tell user what place they came in

___

## Testing

I tested this app by:

* Passing the code through [PEP8](http://pep8online.com/) and confirmed no mistakes
* Giving invalid inputs to test expected error messages
* Testing in my local terminal and the Code Institute Heroku terminal

___

## Bugs and Solutions

* User inputs with spaces and lowercase were considered invalid, so I trimmed the inputs and capitalized them.
* Users would sometimes use whole words such as `"yes"` or `"no"` instead of `"Y"` or `"N"`, so I made these valid inputs.
* When inputting `"N"` after being asked `"Are you sure you want to quit/restart?"` the program did nothing. This was fixed by making sure `validate_ans()` returned `False` when this happened so the program can continue.
* Printing the Highscores would result in an error if there were less than 10 Highscores. To fix this the program now only prints up to the length of the Highscore list (`len(highscores)`) if it is less than 10.

___

## Deployment

This project has been migrated to be deployed on Render

Steps for deployment on Render:

* Fork or clone this repository
* Create a new Web Service on Render.com
* Connect the repository
* Set the environment to **Python 3**
* Set the build command as: **pip install -r requirements.txt && npm install**
* Set the start command as: **node index.js**
* In the advanced tab set these Environmental variables:
   | Key                 | Value     |
   |---------------------|-----------|
   | PORT                | 8000      |
   | PYTHON_VERSION      | 3.10.7    |
* Add your creds.json in secret file
* Click **Create Web Services**


This project was originally depolyed using Code Institue's mock terminal for Heroku

Steps for deployment on Heroku:

* Fork or clone this repository
* Create a new Heroku app
* Set the buildback to **Python** and **NodJS** in that order
* Link th eHeroku app to the repository
* Click on **Deploy**

___

## Language and Programs Used

* Writtn in Python 3.0
* Google Sheets used to store data
* GitHub used for version control
* Google Drive API
* Google Sheets API

___

## Credits

* [Code Institute](https://codeinstitute.net/)'s deployment terminal was used
* [Wikipedia](https://en.wikipedia.org/wiki/2020_Summer_Olympics) and [BBC](https://www.bbc.co.uk/sport/olympics/57240400) was used for information about the Tokyo 2021 Olympic Games
* [W3 Schools](https://www.w3schools.com/) was used for Python reference

