data = []

def linear_search(val:int ,data:list):
    for i in range(len(data)):
        if data[i]  == val: 
            print(f'element found at index {i+1}')


for i in range(int(input('Enter number of elements: '))):
    data.append(int(input('Enter the numbers: ')))
# print(data)
x = int(input('enter element to search: '))

linear_search(x,data)