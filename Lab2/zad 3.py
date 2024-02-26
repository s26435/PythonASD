"""
Jan Wolski 2/26/24
"""


def contains(text, mask):
    mask = bin(mask)[2:]
    tab = []
    try:
        for i in range(len(text)):
            if mask[i] == '1':
                tab.append(text[i])
    except:
        pass
    return ''.join(tab)


def looping(text):
    for i in range(2 * len(text)):
        print(f"nr.{i}={contains(text, i)}")


looping("Jan")
