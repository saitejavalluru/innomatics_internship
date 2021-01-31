if __name__ == '__main__':
    n = int(input())
    student_dict = dict()

    for i in range(n):
        a= input().split(' ')
        name = a[0]
        student_dict[name] = (float(a[1]), float(a[2]), float(a[3]))

    name = input()
    print('%.2f' % (sum(student_dict[name]) / 3.0))


    
