from jarvis import voice
from word2number import w2n
from functions import calculator_gui
from brain.brainV1 import brain


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def normal_calculator():
    global result
    voice.speak("Normal calculator started say a number to start calculation")
    number_1 = 0
    number_2 = 0
    add = 0
    subtract = 0
    multiply = 0
    divide = 0
    counter = 0
    c = 0
    activity = []
    while True:
        try:
            command = voice.take_command()
            if "exit" in command or 'back' in command:
                voice.speak("Exiting math mode")
                activity.append('exit')
                break
            elif "gui" in command or "app" in command:
                calculator_gui.normal_calculator_gui()
                activity.append('gui')
                break
            try:
                result = eval(command)
                activity.append(f'calculated={result}')
            except:
                command = command.split()
                for i in command:
                    if "add" in i or "plus" in i or "+" in i:
                        add = 1
                        activity.append('add')
                    elif "sub" in i or "subtract" in i or "minus" in i or "-" in i:
                        subtract = 1
                        activity.append('subtract')
                    elif "multi" in i or "*" in i or "x" in i:
                        multiply = 1
                        activity.append('multiply')
                    elif "divi" in i or "/" in i:
                        divide = 1
                        activity.append('divide')
                    else:
                        if number_1 == 0:
                                number_1 = float(w2n.word_to_num(i))
                                counter = 1
                        elif counter == 1:
                                number_2 = float(w2n.word_to_num(i))
                                counter = 2
                        if counter == 2 and add == 1:
                            result = addition(number_1, number_2)
                            number_1 = result
                            add = 0
                            counter = 1
                        if counter == 2 and subtract == 1:
                            result = subtraction(number_1, number_2)
                            number_1 = result
                            subtract = 0
                            counter = 1
                        elif counter == 2 and multiply == 1:
                            result = multiplication(number_1, number_2)
                            number_1 = result
                            multiply = 0
                            counter = 1
                        elif counter == 2 and divide == 1:
                            result = division(number_1, number_2)
                            number_1 = result
                            divide = 0
                            counter = 1
            voice.speak(result)
            activity.append(result)
            number_1 = 0
        except:
            voice.speak("Normal calculator started say a number to start calculation")
            c += 1
            if c > 3:
                voice.speak("Sir if you want i can start calculator app")
                command = voice.take_command()
                condition = brain(command)
                if 'accept' in condition[1]:
                    activity.append('accept')
                    voice.speak(condition[0])
                    calculator_gui.normal_calculator_gui()
                elif 'reject' in condition[1]:
                    activity.append('reject')
                    voice.speak(condition[0])
                else:
                    activity.append("can't understand")
                    voice.speak(condition[0])
    return activity


def scientific():
    pass


def main(command):
    if 'normal' in command:
        activity = normal_calculator()
    elif 'scien' in command:
        scientific()
        activity = 'scientific'
    else:
        voice.speak("Which type of calculator would you prefer\nnormal calculator or scientific")
        command = voice.take_command()
        if 'normal' in command:
            activity = normal_calculator()
        elif 'scien' in command:
            scientific()
            activity = 'scientific'
        else:
            voice.speak("I can't understand Sir")
            activity = "can't understand"
    return activity
