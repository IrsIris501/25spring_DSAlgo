def f(x):
    return x**3-5*x**2+10*x-80
def df(x):
    return 3*x**2-10*x+10
cur_x=0
prev_x=0
max_error=10**(-10)
while True:
    prev_x=cur_x
    cur_x=prev_x-f(prev_x)/df(prev_x)
    if abs(cur_x-prev_x)<max_error:
        break
print('%.9f' %cur_x)