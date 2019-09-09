def givePrivateKeys(locator_path=''):
    if locator_path:
        locator_path += '/locator_private'
    else:
        locator_path = 'locator_private'

    with open(locator_path, 'r', encoding='utf-8') as loc:
        keys_path = loc.read()

    with open(keys_path, 'r', encoding='utf-8') as doc:
        login = doc.readline().strip()
        password = doc.readline().strip()

    return [login, password]


def giveGroupKeys(locator_path = ''):
    if locator_path:
        locator_path += '/locator_group'
    else:
        locator_path = 'locator_group'

    with open(locator_path, 'r', encoding='utf-8') as loc:
        keys_path = loc.read()

    with open(keys_path, 'r', encoding='utf-8') as doc:
        token = doc.readline().strip()
        id = doc.readline().strip()

    return [token, id]


if __name__ == "__main__":
    print('PrivateKeys:', *givePrivateKeys(), sep='\n')
    print()
    print('GroupKeys:', *giveGroupKeys(), sep='\n')
