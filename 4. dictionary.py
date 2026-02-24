d1 = {}
#print(type(d1))

d2 = { "krishna": "apple" , "mridul": "banana" , "shyam": "nuts" }
#print(d2)
#print(d2["krishna"])                                                      #we can use either line 6 or 7 ,output will be same
#print(d2.get("krishna"))

d2["krishiv"] = "strawberry"                                                    #addition of new key pair in dictionary
print(d2)

del d2["krishiv"]                                                         #removing/deleting of key pair
#print(d2)

print(d2.copy())                                                        #create shallow copy of dictionary
print(d2)


d2.update({"krishna": "blueberry"})                                           #updating the dictionary with new word
print(d2)

#print(d2.keys())                                                       #display all keys in the dictionary

#print(d2.values())                                                     #display all values from the dictionary

#print(d2.items())                                                      #display all key-value pairs



