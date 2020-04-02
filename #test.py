tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def printTable(aList):
    for i in range(0,len(aList[0])):
        #print(i)
        for j in range(0,len(aList)):
            #max=len(aList[i][j])
            print(aList[j][i].rjust(10),end=' ')
        print() # 换行


printTable(tableData)