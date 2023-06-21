import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'what', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('u should play or do anything else', ['what', 'should', 'i', 'do'], required_words=['do'])
    response('I am fine 🙂 what about you?', ['how','is','your', 'health'], required_words=['health'])
    response('I am a bot ', ['what', 'is', 'your', 'gender'], required_words=['gender'])
    response('I don\'t sleep at all ',['how','much','when', 'do','you', 'sleep'], required_words=['sleep'])
    response('Nope 😔', ['do', 'friends', 'you', 'have'], required_words=['friends'])



    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_MASTER, ['master', 'mentor', 'your'], required_words=['master'])
    response(long.R_MENTOR, ['mentor', 'is', 'your', 'who'], required_words=['mentor'])
    response(long.R_TEACHER, ['teacher', 'is', 'your', 'who'], required_words=['teacher'])
    response(long.R_CRICKET, ['greatest', 'cricket', 'best'], required_words=['cricket'])
    response(long.R_player2, ['goat', 'football', 'best'], required_words=['football'])

    response(long.R_AGE, ['what', 'is', 'your', 'age'], required_words=['age'])
    response(long.R_MOOD, ['how', 'is', 'your', 'mood'], required_words=['mood'])
    response(long.R_STUDY, ['what', 'do', 'you', 'study'], required_words=['study'])
    response(long.R_JOB, ['what', 'is', 'your', 'job'], required_words=['job'])
    response(long.R_GAME, ['which', 'game', 'do', 'you', 'play'], required_words=['game'])
    response(long.R_weather, ['how', 'is', 'weather'], required_words=['weather'])
    response(long.R_PARENT, ['where', 'are', 'your', 'parents'], required_words=['parents'])
    response(long.R_CONTACT, ['how', 'can', 'i', 'contact', 'you'], required_words=['contact'])





    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))
