for i in range(5):
    for k in range(5, i, -1):
        print(' ', end='')

    for k in range((i+1)*2-1):
         print('☆', end='')
    print()
    