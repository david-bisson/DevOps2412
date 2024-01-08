while True:
    try:
        a = int(input("enter first number "))
        b = int(input("enter second number "))
        result = a / b
        print(result)
        break
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ValueError")
    except BaseException as e:
        print(e.args)
        print(e.with_traceback())
