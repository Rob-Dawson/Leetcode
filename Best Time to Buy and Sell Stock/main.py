prices = [7,1,5,3,6,4]
maxProfit = 0

# for i in range(len(prices)):
#     cost = prices[i]
#     for j in range(i+1, len(prices)):
#         sale = prices[j]
#         profit = sale- cost
#         if profit > maxProfit:
#             maxProfit = profit 
# print(maxProfit)

# O(n^2)

minPrice = float("inf")

for i in range(len(prices)):
    if prices[i] < minPrice:
        minPrice = prices[i]
    if prices[i] - minPrice > maxProfit:
        maxProfit = prices[i] - minPrice
    print(maxProfit)
# O(n)