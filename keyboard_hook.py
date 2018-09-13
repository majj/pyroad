
# keyboard hook
# work with python 3.6.5
# but keyboard lib has issue with python 3.7

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
        #print (x.name)


def main():
    
    keyboard.hook(callback, suppress=False)

    while True:
        time.sleep(5) 
        
if __name__ == "__main__":
    main()