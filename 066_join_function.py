l = ['Camera', 'laptop', 'Phone', 'ipad', 'hard disk', 'nvidia graphic card' ]

sentence = ' and '.join(l)
print(sentence)
#prints: Camera and laptop and Phone and ipad and hard disk and nvidia graphic card


sentence = '~~'.join(l)
print(sentence)

sentence = '\n'.join(l)
print(sentence)

print(type(sentence))