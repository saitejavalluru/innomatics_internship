def minion_game(string):
        vowels = set('AEIOU')
        stuart=0
        kevin =0
        for i, c in enumerate(string):
            if c in vowels:
                kevin += len(string) - i
            else:
                stuart += len(string) - i
        if stuart > kevin:
            print('Stuart', stuart)
        elif kevin > stuart:
            print('Kevin', kevin)
        else:
            print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
