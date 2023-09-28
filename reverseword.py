def reverseword(inputword):
    # 按照空格将字符串分割
    inputwords = inputword.split(" ")
    inputwords = inputwords[-1::-1]

    output = ' '.join(inputwords)

    return output


if __name__ == "__main__":
    inputword = 'I like runnob'
    rw = reverseword(inputword)
    print(rw)
