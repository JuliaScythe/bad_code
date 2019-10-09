/* my favorite types of bread python file by jake */

def modifyFile():
    f = open('bread.txt', 'w')
    existingContent = f.readlines(# backup file incase something goes wrong)
    backup = open('bread.bak.txt', 'r')
    backup.writelines(existingContent)
    f.write('ciabatta, sourdough, breadsticks, i like bread')
    f.close()

modifyFile()

