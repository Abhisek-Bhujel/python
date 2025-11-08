# jabber = open('Jabberwocky.txt', 'r')

# for line in jabber:
#     # print(line, end = '')
#     print(line.strip())
    
# jabber.close()


with open('Jabberwocky.txt', encoding='utf-8') as jabber:
    for line in jabber:
        print(line)

print('*'*80)
        
# with open('Jabberwocky.txt') as jabber:
#     for line in jabber:
#         print(line.rstrip())
#         if 'jubjub' in line.casefold():
#             break
# print('*'*80)
