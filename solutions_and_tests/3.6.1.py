from xml.etree import ElementTree


def count(my_dict, level, root):
    color = root.attrib['color']
    my_dict[color] += level
    for child in root:
        count(my_dict, level + 1, child)

text = ElementTree.fromstring(input())
# test = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
# text = ElementTree.fromstring(test)
level = 1
my_dict = {'red': 0, 'green': 0, 'blue': 0}
count(my_dict, level, text)
print('{} {} {}'.format(my_dict['red'], my_dict['green'], my_dict['blue']))


