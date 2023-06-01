# a="i love you do you love me?"
# a=a.split()
# print(a, type(a));
# print ("hello")
# #print(sorted(a, key=len))
# b=[1,2,3,1,5,4,10,6]
# b=sorted(b)

# listed=[i if i%2!=0   else 'even' for i in range(0,10) ]; print (listed)

# a=[1,2,3,1,4,5,6,9,18,21]
# b=filter(lambda x:x%3==0, a)
# print(list(b))
# b=map(lambda x:x**2, filter(lambda x:x%3==0, a))
# print(list(b))
# # or we can use 
# #list comprehension 
# b=[i**2 for i in a if i %3==0]

# print(list(b))
# b={1:'hello', 2:'hey', 3:'hi'}
# b=list(b.values())
# print(b)
dream = """I have a dream that one day this nation will rise up and live out the true
meaning of its creed We hold these truths to be self-evident that all men are created equal
I have a dream that one day on the red hills of Georgia the sons of former slaves and the sons of
former slave owners will be able to sit down together at the table of brotherhood
I have a dream that one day even the state of Mississippi a state sweltering with the heat
of injustice sweltering with the heat of oppression, will be transformed into an oasis of freedom 
and justice
I have a dream that my four little children will one day live in a nation where they will not be
judged by the color of their skin but by the content of their character 
I have a dream today
I have a dream that one day, down in Alabama, with its vicious racists with its governor having
his lips dripping with the words of interposition and nullification one day right there 
in Alabama little black boys and black girls will be able to join hands with little white boys 
and white girls as sisters and brothers"""
wordlist={}
dream=dream.split()
for word in dream:
    if word in wordlist:
        wordlist[word]+=1
    else:
        wordlist[word]=1
print(len(wordlist))
#print(wordlist)
a={k:v for k,v in sorted(wordlist.items(), key=lambda a:a[1], reverse=True)}
print(f'{"WORD":<16}COUNT')
for k,v in a.items():
    if v>=6:
        print(f'{k:<16}{v}')
