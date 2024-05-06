def get_words(filename):
    f = open(filename, 'r')
    lines = f.read().split()
    f.close()
    return (lines)

print(get_words("SampleWords1.txt"))

