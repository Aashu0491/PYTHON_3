dict= {
    'student_name' : 'Aakanksha',
    'Section' :'A',
    'Contact' : 1234567891,
    'E-mail': 'ak@gmail.com',

}

print (dict)

#clear()-Removes all the elements from the dictionary 
dict.clear()
print(f'after clear',dict)

#copy() - Returns a copy of the dictionary
stud_info= {
    'student_name' : 'Aakanksha',
    'Section' :'A',
    'Contact' : 1234567891,
    'E-mail': 'ak@gmail.com',

}
stud_copy=stud_info.copy()
print(f'after copy',stud_copy)

#fromkeys() - Returns a dictionary with the specified keys and value 
new_dict = stud_info.fromkeys(['name', 'age', 'gender'],'None') 
print("New dictionary using fromkeys():", new_dict) 

# get() - Returns the value of the specified key contact 
contact=stud_info.get('Contact')
print(f'get data:',contact)

#items() - Returns a list containing a tuple for each key-value pair 
stud_items=stud_info.items()
print(f'stud items',stud_items)

#keys() - Returns a list containing the dictionary's keys
stud_keys= stud_info.keys()
print(f'stud_keys',stud_keys)

#pop() - Removes the element with the specified key 
removed_contact = stud_info.pop('Contact','Not found')
print("Removed Contact:", removed_contact) 
print("After pop():", stud_info)

#popitem() - Removes the last inserted key-value pair
lastitem=stud_info.popitem()
print('removed last item',lastitem)
print('After item',stud_info)

#setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value 
default=stud_info.setdefault('Stream','Science')
print(' defaultStream',default)
print('After default',stud_info)

#update() - Updates the dictionary with the specified key-value pairs 
stud_update=stud_info.update({'College':'ST.Paul','Address': 'wadi'})
print(f'After update',stud_info)

#values() - Returns a list of all the values in the dictionary
values_list = stud_info.values() 
print("Values in the dictionary:", values_list)


