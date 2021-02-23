## Pollster API

Simple, without authentication, API for polls and their management.

## Routes

1. 'api/v1/polls/questions/': Get all questions, GET
2. 'api/v1/polls/questions/': Create a question, POST
3. 'api/v1/polls/questions/<int:question_id>': Update a question, PATCH
4. 'api/v1/polls/questions/<int:question_id>/': Get a question and its details by ID, GET
5. 'api/v1/polls/questions/<int:question_id>/': Delete a question, DELETE
6. 'api/v1/polls/questions/<int:question_id>/choices/': Add choice to a question, POST
7. 'api/v1/polls/questions/<int:question_id>/vote/': Vote / Select a choice from a poll/question, PATCH
8. 'api/v1/polls/questions/<int:question_id>/result/': Get result of a poll/question, GET

## Payloads

2. { question_text: value, pub_date: 2021-02-19T00:00 } => Both fields are required
3. { question_text: value }, then append the question_id in the URL as seen above
4. Append the question_id in the URL as seen above
5. Append the question_id in the URL as seen above
6. { choice_text: value }, then append the question_id in the URL as seen above
7. Append the question_id in the URL as seen above
8. Append the question_id in the URL as seen above

## Future Improvement

1. Authentication
2. Permissions

## Setup

1. Run git clone using this url: https://github.com/Benneee/pollster.git
2. You're required to have pipenv installed
3. Run `pipenv shell` to enter virtual environment
4. Run `pipenv install -r requirements.txt` as this would take care of installing all the dependencies from the Pipfile for you
5. Code away!
