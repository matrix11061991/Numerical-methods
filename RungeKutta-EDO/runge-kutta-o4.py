def rangeKutta_order_4(x0,y0,xn,n):
    h = (xn-x0)/n
    for i in range(n):
        k1,k2,k3,k4 = h * (f(x0, y0)), h * (f((x0+h/2), (y0+k1/2))), h * (f((x0+h/2), (y0+k2/2))), h * (f((x0+h), (y0+k3)))
        k = (k1+2*k2+2*k3+k4)/6
        yn = y0 + k
        y0 = yn
        x0 = x0+h
        return xn,yn