if __name__ == '__main__':
    # 1. int -> float
    a = 7
    a_float = float(a)
    print("int to float:", a_float, type(a_float))

    # 2. float -> int (drops the decimal part, no rounding)
    b = 9.8
    b_int = int(b)
    print("float to int:", b_int, type(b_int))

    # 3. int -> string
    c = 42
    c_str = str(c)
    print("int to string:", c_str, type(c_str))

    # 4. string containing a number -> int
    d = "123"
    d_int = int(d)
    print("string to int:", d_int, type(d_int))

    # 5. int -> boolean (0 is False, anything else is True)
    e = 5
    e_bool = bool(e)
    print("int to bool:", e_bool, type(e_bool))
