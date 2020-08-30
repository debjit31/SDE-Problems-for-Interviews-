## Buy and sell stocks
rates = list(map(int, input().split()))
buy, profit = 99999, 0
for i in range(len(rates)):
	buy = min(buy, rates[i])
	profit = max(profit, abs(buy-rates[i]))
print(profit)