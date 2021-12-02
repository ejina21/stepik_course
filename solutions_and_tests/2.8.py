with open('../files_from_course/dataset_24465_4.txt') as f, open('../files_from_course/file_test.txt', 'w') as w:
    lst = []
    for line in f:
        lst.append(line)
    while len(lst):
        w.write(lst.pop())