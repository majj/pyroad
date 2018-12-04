
# keyboard hook
# work with python 3.6, 3.7
#> pip uninstall keyboard
#> git clone https://github.com/boppreh/keyboard.git
#> python setup.py install

import keyboard, time

input = ""

def callback(event):
    global input
    
    if event.event_type == 'up':
        
        #keyboard.send(event.name)
        
        if event.name == 'enter':
            print(input)
            input = ""
        else:
            input = input + event.name
        print (event.name)


def main():
    
    keyboard.hook(callback, suppress=False)

    while True:
        time.sleep(5) 
        
if __name__ == "__main__":
    main()