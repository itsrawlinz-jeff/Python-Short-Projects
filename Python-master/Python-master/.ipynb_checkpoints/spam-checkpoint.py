import webbrowser
import time
import random

#while the program is runnig 
while True:
    #create a variable called sites that holds a list of choices in which we use the random module to randomly select which site to go in the list
    sites = random.choice(["craigslist.com", "reddit.com", "betaprofiles.com", "ansible.com", 
    "bing.com", "yahoo.com"])

    #format the websites in the list so that they are in http form
    visit = "http://{}".format(sites)

    #use the webbrowser module to open the specified formatted sites in the variable visit
    webbrowser.open(visit)

    #create a variable seconds to randomly determine the range of seconds to have the program sleep 
    seconds = random.randrange(20, 60)
    time.sleep(seconds)
