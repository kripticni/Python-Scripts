def check1st(tuple, str):
    if tuple[0] == str:
        print("True")
    else:
        print("False")

def check2nd(tuple: tuple[str, int, float], x: int):
    if tuple[1] == x:
        print("True")
    else:
        print("False")


def check3rd(tuple: tuple[str, int, float], x: float) -> bool:
    if tuple[2] == x:
        return True
    else:
        return False

string = str(input())
integer = int(input())
float = float(input())

list = [(string,integer,float)]
for i in range(1,5):
    string = list[i-1][0]
    integer = list[i-1][1]
    float = list[i-1][2]

    string = str(int(string)+1)
    integer = integer + 1
    float = float + 0.1

    list.append((string, integer, float))

for i in range(0,5):
    check1st(list[i],"123")
    check2nd(list[i],123)
    if check3rd(list[i],123.0):
        print("True")
    else:
        print("False")
