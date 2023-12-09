

def Check(vorodi):
    condition = {
        'space': 'blue',
        'mind':'yellow',
        'reality': 'red',
        'power': 'purple',
        'time': 'green',
        'soul': 'orange',
    }

    for i in vorodi:
        # use get method to return the value of the dictionary.
        print (condition.get(i))
        


vorodi= input().split('\n')
Check(vorodi)