import time


def run(code):
    code_list = code.split("\n")
    var = {}
    for i in code_list:
        code_current = ""
        operation = 0
        arg = ""
        use_var = False
        colon = False
        for j in i:
            if j == "\"":
                if colon:
                    colon = False
                else:
                    colon = True
            elif j == " " and not colon:
                if code_current == "print":
                    operation = 1
                elif code_current == "var":
                    operation = 2
                elif code_current == "add":
                    operation = 3
                elif code_current == "sub":
                    operation = 4
                elif code_current == "mul":
                    operation = 5
                elif code_current == "div":
                    operation = 6
                elif code_current == "fdiv":
                    operation = 7
                elif code_current == "mod":
                    operation = 8
                elif code_current == "py":
                    operation = 9
                elif code_current == "date":
                    operation = 10
                else:
                    break
                code_current = ""
            elif operation == 1:
                if j == "$" and not colon:
                    use_var = True
                else:
                    code_current += j
            elif operation == 2:
                if j == "," and not colon:
                    arg = code_current
                    code_current = ""
                else:
                    code_current += j
            elif operation == 3:
                if j == ",":
                    arg = code_current
                    code_current = ""
                else:
                    code_current += j
            elif operation == 4:
                if j == ",":
                    arg = code_current
                    code_current = ""
                else:
                    code_current += j
            elif operation == 5:
                if j == ",":
                    arg = code_current
                    code_current = ""
                else:
                    code_current += j
            elif operation == 6:
                if j == ",":
                    arg = code_current
                    code_current = ""
                else:
                    code_current += j
            elif operation == 7:
                if j == ",":
                    arg = code_current
                    code_current = ""
                else:
                    code_current += j
            elif operation == 8:
                if j == ",":
                    arg = code_current
                    code_current = ""
                else:
                    code_current += j
            elif operation == 9:
                if colon:
                    code_current += j
            else:
                code_current += j
        if operation == 1:
            if use_var:
                print(var[code_current])
            else:
                print(code_current)
        elif operation == 2:
            var[arg] = code_current
        elif operation == 3:
            print(int(arg) + int(code_current))
        elif operation == 4:
            print(int(arg) - int(code_current))
        elif operation == 5:
            print(int(arg) * int(code_current))
        elif operation == 6:
            print(int(arg) // int(code_current))
        elif operation == 7:
            print(int(arg) / int(code_current))
        elif operation == 8:
            print(int(arg) % int(code_current))
        elif operation == 9:
            eval(code_current)
        elif operation == 10:
            print(time.localtime())
        else:
            print("error: invalid function")


def main():
    version = "1.1.0"
    author = "meowjiao"
    print("welcome to meowthon!")
    while 1:
        select = input("run or version or exit -> ")
        if select == "run":
            path = input("file path -> ")
            file = open(path, "r")
            code = file.read()
            run(code)
        elif select == "version":
            print("version: " + str(version))
            print("author: " + str(author))
        elif select == "exit":
            break
        else:
            print("error: invalid function")


if __name__ == '__main__':
    main()
