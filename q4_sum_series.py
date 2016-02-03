# q4_sum_series.py

def m_series(i):
    m = 0 
    for x in range(1,i+1):
        m +=(x/(x+1))
    return m

# test
print("i         m(i)")
for i in range(1,21):
    print("{0:<8}{1:.4f}".format(i,m_series(i)))
