def choose_router(clients):
    router = int(input('Please select what Client number your router is: \n')) - 1
    router = clients[router]
    print('You chose {} as your router, is this correct? y/n'.format(router))
    repeat = input()
    if 'y' in repeat.lower():
        return router
    else:
        choose_router(clients)
def choose_console(clients):
    device = int(input('Please select what Client number your console is: \n')) - 1
    device = clients[device]
    print('You chose {} as your console, is this correct? y/n'.format(device))
    repeat = input()
    if 'y' in repeat.lower():
        return device
    else:
        choose_console(clients)