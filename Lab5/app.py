import utils

def func():
    while(True):
        x = input()
        if x == 'q':
            break
        x = int(x)
        print(utils.process_item(x))
        
if __name__ == "__main__":
    print("1")
    pass