profit = int(input('输入利润（I)：'))
bonus = 0
thresholds = [100000, 100000, 200000, 200000, 400000]
rates = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
for i, threshold in enumerate(thresholds):
    if profit <= threshold:
        bonus += profit * rates[i]
        profit = 0
        break
    else:
        bonus += threshold * rates[i]
        profit -= threshold
bonus += profit * rates[-1]
print('应发放奖金总数：', bonus)
