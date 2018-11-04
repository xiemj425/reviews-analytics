data = []
length = []
sum = 0
with open('reviews.txt','r') as f:
    for line in f:
        sum = sum + len(line)
        data.append(line)
print('留言平均長度：',sum/len(data))