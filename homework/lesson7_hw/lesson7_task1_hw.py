while True:
    result = 3

    user_number = int(input('Enter number - '))

    if result == user_number:
        print('Congratulations, you guessed it right')
        break
    elif result != user_number:
        print('Try again, please')
