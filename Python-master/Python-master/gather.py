import json

#prompt user to enter an id key that they want to look up
key = input("Enter Key : ")

#create a bool variable and set it false
found = False

#define a function get_key that holds in the key variable as one argument
def get_key(key):
    #read the data.json file and set its contents to data
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        #loop through the json data
        for p in data:
            #if p encounters a key that matches the user's key
            if key == p:
                #set found to True
                global found
                found = True
                #set the key values to its own variable
                teacher = data[p][0]['teacher']
                grade = data[p][0]['student_grade']
                ssid = data[p][0]['student_ssid']
                name = data[p][0]['student_name']
                #after p has found key and set its values into varaiables, break out of loop
                break
    #if the found variable is true
    if found == True:
        #print the values of the key 
        print("Name: " + name + "\n" + 
                "Grade: " + grade + "\n" + 
                "Teacher: " + teacher + "\n" + 
                "SSID: " + ssid)
    #else print Key was not found
    else:
        print("Key %s could not be found" %key)

#call the function 
get_key(key)