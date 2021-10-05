count = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

sentence = "Learning programming is similar to learning a musical instrument. Both involve practise and making lots of mistakes. Both also require perseverance to develop fluency. Keep going!"

for char in sentence.lower():
    if char in count.keys():
        count[char] += 1

print(count)
