def exception_check():
    try:
        a=15/0
        return 1
    except Exception as e:
        print('abcd')
        return 999
    finally:
        print('fuck')
        # return 9


if __name__ == '__main__':
    print(exception_check())