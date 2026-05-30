'''String Indexing 
String indexing is a way to access individual characters in a string using their position.'''
text   = "Ronaldo"
#index =  0123456
#value = "Ronaldo"
print(text[0]) #output: R
print(text[1]) #output: o
print(text[2]) #output: n
print(text[3]) #output: a
print(text[4]) #output: l
print(text[5]) #output: d
print(text[6]) #output: o


#Negative Indexing
'''Negative indexing allows you to access characters from the end of the string'''
print(text[-1]) #output: o
print(text[-2]) #output: d
print(text[-3]) #output: l
print(text[-4]) #output: a
print(text[-5]) #output: n
print(text[-6]) #output: o
print(text[-7]) #output: R


#String Slicing
#Extract portions of strings using [start:stop:step]
'''String slicing allows you to extract a portion of a string by specifying a range of indices.'''

text = "GOAT Ronaldo"
print(text[0:4]) #output: GOAT {indices 0 to 3}
print(text[5:12]) #output: Ronaldo {indices 5 to 11}
print(text[:4]) #output: GOAT {from the beginning to index 3}
print(text[5:]) #output: Ronaldo {from index 5 to the end}
print(text[:]) #output: GOAT Ronaldo {the entire string}

#Step in slicing
print(text[::2]) #output: GATRnl {every second character}
print(text[::2]) #output: OA oao {every second character starting from index 1}
print(text[::-1]) #output: odlanorT AOG {the entire string in reverse}