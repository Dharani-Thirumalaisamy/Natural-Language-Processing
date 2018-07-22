import random
import time
import speech_recognition as sr
def sst(recognizer , microphone):

    #if not isinstance(recognizer,sr.Recognizer):
    #    raise TypeError('create a proper instance for recognizer')
    #if not isinstance(microphone,sr.Microphone):
    #    raise TypeError('create proper instance for microphone input')

    with microphone as source :
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # creating the response
    output = {
        'error' : None,
        'correct' : True,
        'text' : None
    }

    recognizer['text'] = recognizer.recognize_google(audio)

    return output

if __name__ == "__main__" :
    words = ['ape','baboon','cat','dog','elephant','frog','giraffe']
    nb_trails = 2
    nb_prompt = 4

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    random_pick = random.choice(words)

    instructions = (
        "I'm thinking of one of these words:\n"
        "{words}\n"
        "You have {n} tries to guess which one.\n"
    ).format(words=', '.join(words), n=nb_trails)

    print(instructions)
    time.sleep(2)

for i in range (nb_trails):
    for n in range (nb_prompt):
        answer = sst(recognizer,microphone)
        if answer['text']:
            break;
        if answer['success']:
            break;
        if answer['error']:
            print('wrong guess')

    print('THe animal you guessed was : '.format(answer['text']))

    is_the_guess_correct = answer['text'].lower() == random_pick.lower()
    remaining_attempts = i < nb_trails -1

    if is_the_guess_correct:
        print('You win. The correct guess is :'.format(answer['text']))
    elif remaining_attempts:
        print('you have more attempts to guess the  answer')
    else :
        print('you lose!')
