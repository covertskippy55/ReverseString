__author__ = 'Dilan'
from sys import argv


def main():
    # argv=['','hello']
    if len(argv) < 2:
        print "Invalid use of program. Usage is : reverseString.py string"
        exit(1)
    else:
        ffhalf = ""
        fshalf = ""
        strlen = len(argv[1])
        halfpoint = strlen / 2
        print strlen
        print halfpoint
        if strlen % 2 == 0:
            fhalf = argv[1][0:halfpoint]
            shalf = argv[1][halfpoint:]
            print fhalf
            print shalf
            for i in range(halfpoint):
                k = (len(argv[1])/2) - (i+1)
                ffhalf += fhalf[k]
            for i in range(halfpoint):
                k = (len(argv[1])/2) - (i+1)
                fshalf += shalf[k]

            print "{0}{1}".format(fshalf, ffhalf)
        if strlen % 2 != 0:
            halfpoint = (strlen / 2)
            print strlen
            print halfpoint
            fhalf = argv[1][0:halfpoint]
            shalf = argv[1][halfpoint:]
            print fhalf
            print shalf
            for i in range(halfpoint):
                k = (len(argv[1])/2) - (i+1)
                ffhalf += fhalf[k]
            for i in range(halfpoint+1):
                k = (len(argv[1])/2) - i
                fshalf += shalf[k]

            print "{0}{1}".format(fshalf, ffhalf)


if __name__ == '__main__':
    main()
