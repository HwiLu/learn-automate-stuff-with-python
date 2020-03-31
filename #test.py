def list2str(alist):
    print(alist)
    a = alist.pop()
    a = 'and  ' + a
    alist.append(a)
    b = ', '.join(alist)
    print(b)
    return(b)    # print改成return就可以返回结果

a = ['cat', 'dog', 'cow']
list2str(a)

'''
思路
先把列表最后一个
元素pop出来，并与and进行相加，再使用join方法将其拼接
'''