def splitter(li):
    count = len(li)
    if count % 2 != 0:
        print(li[0])
        del li[0]
    it = iter(li)

    for i, j in zip(it, it):
        print(i, j)


if __name__ == "__main__":
    li = [1, 2, 3, 4, 5, 6, 7]
    splitter(li)
