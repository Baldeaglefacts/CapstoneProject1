from dataclasses import dataclass

""" A quiz program. """

"""This program asks the user to select a topic, then asks them questions related to their selected topic. It informs 
the user if they get each question correct, and tells them the correct answer if they get it wrong. It then records and 
displays their success rate at the end of the quiz."""


# This section sets up the "topic" dataclass and defines how topics (along with their questions and answers) will be
# stored and read.
@dataclass
class Topic:
    name: str
    questions: dict  # Questions and their associated answers are stored in a dictionary. Makes it so they're inherently

    # attributed to each other

    def __getattr__(self, item):  # This sets up how I'll be able to call to get a topic's information
        match item:
            case 'name':
                return self.name  # essentially, if I call topic.__getattr__('name'), it'll give me the topic's name
                # in a str format.
            case 'questions':
                return self.questions.items()  # Replacing name with 'questions' will give me the topic's dictionary
                # of questions and answers


def main():
    topicList = []
    # here are examples of Topics. Each key in the dictionaries are questions, with their values being the answer.
    # I also save the topic's name in a str format, to make printing the topic name easier.
    art = Topic('art', {'Who painted the Mona Lisa?': 'Leonardo Da Vinci',
                        'What precious stone is used to make the artist\'s pigment ultramarine?': 'Lapiz lazuli',
                        'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?': 'Chicago'})
    topicList.append(art)  # as part of adding a new topic, the topic also has to be to the topicList. Otherwise it
    # can't be found and referenced. Ideally, I'd want entries to automatically be found and added to this list.
    # I'm not sure how to go about that though.

    space = Topic('space', {'Which planet is closest to the sun?': 'Mercury',
                            'Which planet spins in the opposite direction to all the others in the solar system?':
                                'Venus', 'How many moons does Mars have?': '2',
                            'What was the first human-made object to leave the solar system?': 'Voyager 1'})
    topicList.append(space)

    # This section handles asking the user for a topic selection.
    choices = []
    for v in topicList:  # this loop finds adds all the topic names to a list, to then be displayed to the user.
        choices.append(v.name.lower())  # the names are saved in lower case, for comparison purposes
    print('What topic would you like questions on? Your choices are: ', end='')
    print(*choices, sep=", ", end=": ")  # All this formatting is to make the list get printed out cleanly.
    # All without needing to write another loop
    choice = input().lower().strip()

    # This section determines if the chosen topic exists in the list of topics. If so, it saves the topic selection
    topic = ''
    while not choices.__contains__(choice):
        # this loop holds the user hostage until their input matches an available option
        print('That is not a valid topic. Your choices are: ', end='')
        print(*choices, sep=", ", end=": ")
        choice = input().lower().strip()
    for v in topicList:  # After the user gets past validation, this loop will find and save the Topic (not topic name)
        # That they chose. Gotta do this because we've been comparing strings up till now, but Topics aren't strings
        if v.name == choice:
            topic = v

    # This section handles the asking of questions, as well as score tracking. Basically this is the game part.
    total_score = 0
    for k, v in topic.__getattr__('questions'):  # This loop extracts questions and answers for the topic.
        print(k)  # Here the dictionary key (question) is asked. "v" (value) is the correct answer
        answer = input('Enter your answer: ')
        if answer.lower() == str.lower(v):  # The inputted answer is then compared to the correct answer (v)
            print('Correct!')
            total_score += 1
        else:
            print('Sorry, the answer is ' + v + '.')

    # This section handles final scoring and game wrap up.
    print('End of quiz!')
    print(f'Your total score on {topic.__getattr__("name")} questions is {total_score} out of '
          f'{topic.__getattr__("questions").__len__()}.')
    # "{topic.__getattr__("name")}" is to retrieve the topic name in str form.
    if total_score == topic.__getattr__("questions").__len__():
        print('You got all the answers correct!')
# "{topic.__getattr__("questions").__len__()}" retrieves the length of the Topic's dictionary to find out how many
# Questions the Topic had.


main()
