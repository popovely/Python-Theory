def p_plus(a, b):
    print(a + b)


def r_plus(a, b):
    return a + b
    print("return 아래에 있어서 실행되지 않는 코드")


p_result = p_plus(2, 3)
r_result = r_plus(2, 3)

print(p_result, r_result)
