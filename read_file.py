fw = open('sample2.txt', 'a')

fw.write('Hello world! \nHey hey hey!!!')

fw.close()

fr = open('sample2.txt', 'r')
text = fr.read()
print(text)
fr.close()
