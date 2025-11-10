while True:
    try:
        a = input("請輸入a:")
        if a == "exit":
            break
        a = eval(a)
        b = eval(input("請輸入b:"))

        if a > b:
            print(f"a比b大{a - b}")
        elif b > a:
            print(f"b比a大{b - a}")
        else:
            print("a跟b一樣大")
    except Exception as e:
        print("輸入錯誤:", e)
