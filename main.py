def run(code):
    code_list = code.split("\n")
    for i in code_list:
        code_current = ""
        operation = 0
        for j in i:
            if j == " " and operation == 0:
                if code_current == "print":
                    operation = 1
                    code_current = ""
            elif operation == 1:
                if j != "\"":
                    code_current += j
            else:
                code_current += j
        if operation == 1:
            print(code_current)
        else:
            print("error: invalid function")


def main():
    while 1:
        select = input("run or exit -> ")
        if select == "run":
            path = input("file path -> ")
            file = open(path, "r")
            code = file.read()
            run(code)
        elif select == "exit":
            break
        else:
            print("error: wrong input")


if __name__ == '__main__':
    main()
