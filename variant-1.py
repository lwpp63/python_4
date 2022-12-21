import  datetime, time
#
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
nachalo = time.time()
start = datetime.datetime.now()


if __name__ == '__main__':
    print_hi(f'Variant-1 started in {start.strftime("%c")}')