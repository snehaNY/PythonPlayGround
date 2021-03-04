
def fizzBuzzSample():
    lst = [3,5,10,15,17,20,23,25,27,'str',15.0]
    for i, val in enumerate(lst):
        if not isinstance(val,str):
            if val%3 == 0 and val%5 ==0:
                lst[i] = 'fizzbuzz'
            elif val%3 == 0:
                lst[i] = 'fizz'
            elif val%5 == 0:
                lst[i] = 'buzz'

    print(f'Modified list is {lst}')

def lstCompSample():
    num = [2,5,8,4,3,1]
    print(f'square of numbers are {[(i*i) for i in num]}')
    print(f'odd numbers are {[i for i in num if not i%2==0]}')

def complexSort():
    animals = [
        {'type':'elephant','age':10},
        {'type':'lion', 'age':3},
        {'type':'giraffe','age':5}
    ]
    print(sorted(animals, key= lambda animals: animals['age'], reverse = True))   
    
def uniqueWords():
    import random
    all_words = 'all the words in the world'.split()
    s = set()
    for _ in range(1000):
        s.add(random.choice(all_words))
    print(s)

def main():
    fizzBuzzSample()
    lstCompSample()
    complexSort()
    uniqueWords()        


if __name__ == '__main__': 
    main()
