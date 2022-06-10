
print('Welcome to Krusty Krab!')
print('What would you like to do?')
print('1: Dine-in')
print('2. Takeaway')
print('3. Catering for events')
print('0. Change of mind')
while True:
    cmd = input('')
    if cmd == '1':
        print('Dine-in')
        num = input('How many guests are there in your party?\n')
        try:
            num = int(num)
            if num < 0:
                print('Number of guess must be a whole number more than 0.')
            else:
                cnt = (num - 1) // 6 + 1
                if num > 15 * 6:
                    print('You will need to select "3. Catering"')
                elif cnt > 2:
                    print('You will need to wait. Can I get your name?')
                    name = input()
                    print(f'Wating list: {cnt} tables for {name}.')

                else:
                    print(f"{cnt} table for {num} peoples!")
        except:
            print('Number of guess must be a whole number more than 0.')
        break
    elif cmd == '2':
        print('Takeaway')
        print('Proceed to counter to order')
        break
    elif cmd == '3':
        print('Comming soons! Call us for event caterings:')
        break
    elif cmd == '0':
        print('join us another time')
        break
    else:
        print('Try again.')



