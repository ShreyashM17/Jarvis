from brain.command_lineV1 import commands
from random import random


def brain(heard):
    tag_found = " "
    count = 0
    percentage = 0
    data = commands.command_lines
    found_index = None
    found = False
    searching = True
    command = heard.lower()
    command = command.split()
    query_length = len(command)
    tags = commands.tags
    data_size = len(data['commands'])
    for tag in tags:
        if searching:
            for word in command:
                if word == tag:
                    found = True
                    found_index = tags.index(tag)
                    tag_found = tag
                    searching = False
                    break
        else:
            break
    for list_index in range(data_size):
        if searching:
            for line in data['commands'][list_index][tags[list_index]]['heard']:
                if searching:
                    line_list = line.split()
                    if len(set(command) - set(line_list)) + len(set(line_list) - set(command)) == 0:
                        found = True
                        found_index = list_index
                        tag_found = tags[list_index]
                        searching = False
                        break
                if searching:
                    for word in command:
                        if word in line:
                            found = True
                            count += 1
                    similarity = (count / query_length) * 100
                    count = 0
                    if similarity > 50:
                        if percentage < similarity:
                            percentage = similarity
                            found_index = list_index
                            tag_found = tags[list_index]
        if not searching:
            break
    try:
        if found:
            say = data['commands'][found_index][tag_found]['say'][int(random() * 10) % len(data['commands'][found_index][tag_found]['say'])]
            return say, tag_found, found
    except Exception as e:
        return "I can't understand", "not found", found
