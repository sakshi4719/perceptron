import numpy as np
w1, w2, w3, w4 = 0, 0, 0, 0
b = 0
alpha = 1

x1 = [1, -1, 1, 1]
x2 = [1, 1, 1, -1]
x3 = [1, -1, 1, -1]
x4 = [1, -1, -1, 1]

t = [1, 1, -1, -1]

def signum(y_in):
    if y_in == 0:
        return 0
    elif y_in < 0:
        return -1
    else:
        return 1

converged = False
epoch = 0  

while not converged:
    epoch += 1  
    converged = True
    
    print(f"Epoch {epoch}:")
    
    for i in range(4):
        y_in = x1[i] * w1 + x2[i] * w2 + x3[i] * w3 + x4[i] * w4 + b
        y = signum(y_in)
        print(f"y_in: {y_in}, y: {y}, target: {t[i]}")

        if y != t[i]:
            w1 = w1 + alpha * t[i] * x1[i]
            w2 = w2 + alpha * t[i] * x2[i]
            w3 = w3 + alpha * t[i] * x3[i]
            w4 = w4 + alpha * t[i] * x4[i]
            b = b + alpha * t[i]
            converged = False
        
        print(f"Updated w1: {w1}, w2: {w2}, w3: {w3}, w4: {w4}, b: {b} \n")

print("Training complete after", epoch, "epochs")
