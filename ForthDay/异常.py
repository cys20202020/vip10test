'''
try:
 可能发⽣错误的代码
except:
 如果出现异常执⾏的代码
 try:
    open('test.txt', 'r')
except:
    open('test.txt','w')

'''

'''
捕获指定异常
try:
 可能发⽣错误的代码
except 异常类型:
 如果捕获到该异常类型执⾏的代码
try:
    open(num)
except NameError:
    print('有错误') 
'''

'''
捕获多个指定异常
try:
 print(1/0)
except (NameError, ZeroDivisionError):
 print('有错误')
'''

'''
捕获异常描述信息
try:
    print(num)
except (NameError, ZeroDivisionError) as result:
    print(result)
'''

'''
异常的else
else表示的是如果没有异常要执⾏的代码
try:
    print(1)
except Exception as result:
    print(result)
else:
    print('我是else，是没有异常的时候执⾏的代码')
'''

'''
异常的finally
finally表示的是⽆论是否异常都要执⾏的代码，例如关闭⽂件.
try:
    f = open('test.txt', 'r')
except Exception as result:
    f = open('test.txt', 'w')
else:
    print('没有异常，真开⼼')
finally:
    f.close()
'''


