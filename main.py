''' main '''
# 使用自建的套件 myMath 來計算使用者輸入的五個數的平均值
import myMath.myStatistics
number=[]
for i in range(5):
  
number.append(int(input("輸入數字:")))

print(number)
print(myMath.myStatistics.myMean(number))
