'''
    Module Marks_functions contain functions used in Marks_main
'''

import math

def printOnScreen(to_print, comment='Sequens contain: '):
    print(comment)
    for data in to_print:
        print(data, end=' ')
    print() # '\n' for better console view

def average(marks):
    sumOfMarks = sum(marks)
    return sumOfMarks / float(len(marks))

def median(marks):
    '''
        If quantity of marks is even, median is like average of two middle marks.
        If quantity of marks is odd, median is middle mark of sorted ascending list of marks.
    '''
    
    marks.sort()
    # Even 
    if len(marks) % 2 == 0:  # modulo '%' checks if quantity of marks is even
        half = int(len(marks) / 2)
        # 1st solution:
        # return float(marks[half-1]+marks[half] / 2.0
        # 2nd solution:
        return float(sum(marks[half - 1: half + 1])) / 2.0
    # Odd 
    else:
        return marks[int(len(marks) / 2)]

def variance(marks, average):
    '''
        Variance is a sum of difference of squares each of mark with average.
        
        sigma = (o1-avg)^2 + (o2-avg)^2 +...+ (on-avg)^2 /n
        
        o1,o2,...,on - marks
        avg - average of marks
        n - quantity of marks
    '''
    sigma = 0.0
    for mark in marks:
        sigma += (mark - average)**2
    return sigma / len(marks)

def deviation(marks, average):
    '''
        Deviation is the square root of the variance.
    '''

    v = variance(marks, average)
    return math.sqrt(v)

def singleMarkDeviation(mark, average):
    '''
        Deviation is the square root of the variance.
        In this case counted for 1 element of set.
    '''
    
     return math.sqrt(((mark - average)**2))
