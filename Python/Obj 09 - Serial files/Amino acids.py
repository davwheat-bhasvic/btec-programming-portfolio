text = ""

with open('dna', 'r') as file:
    text = file.read()

sequence = input("Enter sequence to count: ")

print(text.count(sequence))
