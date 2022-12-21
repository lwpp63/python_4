import  datetime, time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
nachalo = time.time()
start = datetime.datetime.now()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(f'Python_4 started in {start.strftime("%c")}')
    print(f"Это файл: var.py")
    print("Это файл: var.py с добавлением строки")
