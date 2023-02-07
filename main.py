def run(code):
    code_list = code.split("\n")
    var = {}
    for i in code_list:
        code_current = ""
        operation = 0
        name = ""
        print_var = False
        colon = False
        for j in i:
            if j == " " and operation == 0:
                if code_current == "print":
                    operation = 1
                elif code_current == "var":
                    operation = 2
                code_current = ""
            elif operation == 1:
                if j == "$" and not colon:
                    print_var = True
                elif j == "\"" and colon:
                    colon = False
                elif j == "\"":
                    colon = True
                else:
                    code_current += j
            elif operation == 2:
                if j == "," and not colon:
                    name = code_current
                    code_current = ""
                elif j == "\"" and colon:
                    colon = False
                elif j != "\"":
                    code_current += j
                    colon = True
            else:
                code_current += j
        if operation == 1:
            if print_var:
                print(var[code_current])
            else:
                print(code_current)
        elif operation == 2:
            var[name] = code_current
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
