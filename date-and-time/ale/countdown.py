def display(seconds):
    print(f'{(seconds // 60):02}:{(seconds % 60):02}')

def countdown(seconds):
    while seconds >= 0:
        display(seconds)
        if input() != '':
            break
        seconds -= 1

countdown(300)
