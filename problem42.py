import time


def run():
    count = 0
    with open('words.txt', 'r') as f:
        for line in f:
            curr_line = line.split(',')
            for word in curr_line:
                # print(word)
                word_sum = sum([(ord(char)-64) for char in word[1:-1]])
                word_sum = ((1 + 8*word_sum)**0.5 - 1) / 2
                if word_sum == int(word_sum):
                    count += 1
    return count


start = time.time()
print(run())
print("It took {}s".format(time.time() - start))
