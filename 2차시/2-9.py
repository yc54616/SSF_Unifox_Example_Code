class bmi_calculater:
    def __init__(self,weight,height):
        self.weight = weight
        self.height = height/100
    def result(self):
        bmi = self.weight/self.height**2
        if bmi <= 18.5:
            return '저체중'
        elif bmi <= 22.9:
            return '정상'
        elif bmi <= 24.9:
            return '과체중'
        else:
            return '비만'
    
bmi_1 = bmi_calculater(71,179)
bmi_2 = bmi_calculater(60,175)

print(bmi_1.weight, bmi_1.height, bmi_1.result())
print(bmi_2.weight, bmi_2.height, bmi_2.result())