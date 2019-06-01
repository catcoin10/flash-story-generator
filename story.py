import sys, secrets

def randomnumber(n):    return secrets.randbits(96) % n
def get_words(mode):
        def file(fname):
                fd = open(fname, "r")
                data = fd.read()
                fd.close()
                list_of_data = []
                bigstr = ','.join(data)
                small_list = [line.split(',') for line in bigstr.split('\n')]
                condensed_list = []
                for i in small_list:
                        str = ""
                        for I in i:     str += I
                        condensed_list.append(str)
                return condensed_list
        if mode == 0:   return file("words.txt")

def word():
        words = get_words(0)
        length = len(words)
        random = randomnumber(length)
        word = words[random]
        return word

list = []
for i in range(2):      print(word(),)
