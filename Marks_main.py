from Marks_functions import printOnScreen, average, median, variance, deviation

def main(args):
    subjects = set(['polish', 'english', 'mathematic', 'physics' ])
    printOnScreen(subjects, 'Dataset of subjects contain: ')

    print('\nTo interrupt input of subjects press Enter.')
    while True:
        subject = input('Type name of subject which you want to add to dataset: ')
        if len(subject):
            if subject in subjects:
                print('This is already in dataset.')
            subjects.add(subject)  # Add subject to dataset
        else:
            printOnScreen(subjects, '\nYour subjects: ')
            subject = input('\nTo which subject do you want to add marks? ')
            if subject not in subjects:
                print('Lack of the inputed subject. You should add it first.')
            else:
                break
    marks = []  # definition
    mark = None  #  variable steering a loop and to download the marks
    print('\nTo interrupt input of marks input ''0''.')

    while not mark:
        try:
            mark = int(input('Type the mark (1-6):'))  # in Poland we have marks from 1(worst) to 6(best)
            if (mark > 0 and mark < 7):
                marks.append(float(mark))
            elif mark == 0:
                break
            else:
                print('Wrong mark.')
            mark = None
        except ValueError:
            print('Wrong data!')
            continue
    
    printOnScreen(marks, subject.capitalize() + ' inputed marks: ')
    avg = average(marks)
    m = median(marks)
    v = variance(marks, avg)
    dev = deviation(marks, avg)
    print('\nAverage: {0:5.2f}'.format(avg))  # https://pyformat.info/
    print('Median: {0:5.2f}'.format(m))
    print('Variance: {0:5.2f}'.format(v))
    print('Deviation: {0:5.2f}'.format(dev))

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
