from django.shortcuts import render, redirect
import os
import json

def button_class(active_exercise, button):
    if active_exercise == button:
        return 'btn btn-outline-secondary btn-sm active'
    else:
        return 'btn btn-outline-secondary btn-sm'

def exercises(request, active_exercises=0):
    classes = {
        'button1_class': button_class(active_exercises, 102),
        'button2_class': button_class(active_exercises, 106),
        'button3_class': button_class(active_exercises, 103),
        'button4_class': button_class(active_exercises, 110),
        'button5_class': button_class(active_exercises, 111),
        'button6_class': button_class(active_exercises, 112),
        'button7_class': button_class(active_exercises, 113),
        'button8_class': button_class(active_exercises, 114),
        'button9_class': button_class(active_exercises, 117),
        'button10_class': button_class(active_exercises, 118),
        'button11_class': button_class(active_exercises, 120),
        'button12_class': button_class(active_exercises, 121),
        'button13_class': button_class(active_exercises, 119),
        'button14_class': button_class(active_exercises, 101),
        'button15_class': button_class(active_exercises, 104),
    }

    body_diagram = "/static/bodyDiagram/bodyDiagram" + str(active_exercises) + ".png"
    
    exercise_list = []

    with open(os.path.dirname(os.path.realpath(__file__)) + '/Exercises.json') as f:
        data = json.load(f)

    if (active_exercises == 100):
        exercise_list = data
    else:
        for item in data:
            if item["group_code"] == active_exercises:
                exercise_list.append(item)

    context = {
        'exercises': exercise_list,
        'title': 'Exercises',
        'active_exercise': active_exercises,
        'classes': classes,
        'body_diagram': body_diagram,
    }

    return render(request, 'find_exercise.html', context)
