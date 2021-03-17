def func(balance, annualInterestRate, monthlyPaymentRate):
    for i in range(12):
        monthlyBalance = balance * (1-monthlyPaymentRate) * (1+annualInterestRate/12)
        balance = monthlyBalance
    return round(monthlyBalance, 2)

def func2(balance, annualInterestRate):
    payment = 0
    monthlyBalance = 1
    while monthlyBalance > 0:
        payment += 10
        lastBalance = balance
        for i in range(12):
            monthlyBalance = (lastBalance-payment) * (1+annualInterestRate/12)
            lastBalance = monthlyBalance
    print(payment)
    
def func3(balance, annualInterestRate):
    high = (balance*(1+annualInterestRate/12)**12)/12
    low = balance/12
    payment = balance/12
    monthlyBalance = 1
    lastBalance = balance
    step = 0
    while abs(monthlyBalance) > 0.01:
        lastBalance = balance
        if monthlyBalance > 0:
            low = payment
            payment = (high+low)/2
        else:
            high = payment
            payment = (high+low)/2
        for i in range(12):
            monthlyBalance = (lastBalance-payment) * (1+annualInterestRate/12)
            lastBalance = monthlyBalance
            step += 1
    print(round(payment, 2))
