def accumulate_text(text):
    global accumulated_text
    accumulated_text += text


def make_header():
    print("Level: ", end="")
    while True:
        level = int(input())
        if level in range(1, 7):
            break
        else:
            print("The level should be within the range of 1 to 6")
    print("Text: ", end="")
    input_text = input()
    final_text = f"{'#' * level} {input_text}"
    accumulate_text(final_text + "\n")


def make_plain():
    print("Text: ", end="")
    input_text = input()
    accumulate_text(input_text)


def make_bold():
    print("Text: ", end="")
    input_text = input()
    input_text = f"**{input_text}**"
    accumulate_text(input_text)


def make_italic():
    print("Text: ", end="")
    input_text = input()
    input_text = f"*{input_text}*"
    accumulate_text(input_text)


def make_inline_code():
    print("Text: ", end="")
    input_text = input()
    input_text = f"`{input_text}`"
    accumulate_text(input_text)


def make_new_line():
    accumulate_text('\n')


def make_link():
    print("Label: ", end="")
    label = input()
    print("URL: ", end="")
    url = input()
    final_link = f"[{label}]({url})"
    accumulate_text(final_link)


def make_list():
    final_list = ''
    while True:
        print("Number of rows: ", end="")
        num_rows = int(input())
        if num_rows > 0:
            break
        print("The number of rows should be greater than zero")

    for i in range(num_rows):
        print("Row #{}".format(i + 1), end=": ")
        if user_choice == 'unordered-list':
            current_row = '* {}\n'.format(input())
            final_list += current_row
        elif user_choice == 'ordered-list':
            current_row = '{}. {}\n'.format(i + 1, input())
            final_list += current_row

    accumulate_text(final_list)


def done():
    with open('output.md', 'w', encoding='utf-8') as file:
        file.write(accumulated_text)


def switcher(action):
    actions = {
        'plain': make_plain,
        'bold': make_bold,
        'italic': make_italic,
        'header': make_header,
        'link': make_link,
        'inline-code': make_inline_code,
        'new-line': make_new_line,
        'unordered-list': make_list,
        'ordered-list': make_list
    }
    actions[action]()


available_formatters = "unordered-list ordered-list plain bold italic header link inline-code new-line".split()

special_commands = "!help !done".split()

help_message = "Available formatters: " + " ".join(available_formatters) + "\n" + "Special commands: !help !done"

accumulated_text = ""

while True:
    print("Choose a formatter: ", end="")
    user_choice = input()

    if user_choice == "!done":
        done()
        break
    elif user_choice == "!help":
        print(help_message)
    elif user_choice not in available_formatters:
        print("Unknown formatting type or command")
        continue
    switcher(user_choice)
    print(accumulated_text)




