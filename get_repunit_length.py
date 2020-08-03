import sys


def get_repunit_length(number):
    if (number <= 0):
        return -1
    elif ((number % 2 == 0) or (number % 5 == 0)):
        return 0
    else:
        repunit = 1
        length = 0
        while(True):
            length += 1
            if (repunit % number == 0):
                return length
            else:
                repunit = repunit + 10 ** length




if __name__ == "__main__":
    args = sys.argv
    input = int(args[1])

    result = get_repunit_length(input)

    if (result == -1):
        print("自然数を入力してください。")
    elif (result == 0):
        print(f'{input} で割り切れるRepunit数は存在しません。')
    else:
        print(f'{input} で割り切れる最小のRepunit数は R_{result} です。')
