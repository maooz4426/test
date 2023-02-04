
#平均を計算
class Avr():#分散等で同じ動作を行うため、クラス化
    def __init__(self):
        self.size = int(input("データの数を入力して下さい "))
        self.list = []
        self.sum = float(0)
        for n in range(self.size):
            self.list.append(float(input("データの値を入力してください ")))
            self.sum += self.list[n]
    def avr(self):
        self.avr = float(self.sum / float(self.size))
        print("平均は" + str(self.avr))

#分散を計算    
class Dsp(Avr):#他の計算で同じようなことをするため
    def __inti__(self):
        super().__init__()#平均計算の際に行ったコンストラクタを使用
        self.list
    def dsp(self):
        super().avr()#平均での計算結果を試用するため、Avrクラスのavrメッソドを継承
        sum = 0
        for n in range(self.size):
            sum += (self.list[n] - self.avr)**2
        self.dsp = sum / self.size
        print("分散は" + str(self.dsp))
        
#標準偏差の計算
class Std_dev(Dsp):#標準偏差は分散を1/2するため、継承
    def __init__(self):
        super().__init__()
    def dev(self):
        super().dsp()
        self.dev = (self.dsp)**(1/2)
        print("標準偏差は" + str(self.dev))
       
  
#不変分散の計算
class Not_cng_dsp(Avr):#平均を途中で使うためAvrクラスを継承
    def __init__(self):
        super().__init__()
        self.list
    def dsp(self):
        super().avr()
        sum = 0
        for n in range(self.size):
            sum += (self.list[n] - self.avr)**2
        self.dsp = sum / (self.size - 1)
        print("不変分散" + str(self.dsp))
                
#標準誤差(分散が未知の場合)
class Std_error(Not_cng_dsp):
    def __init__(self):
        super().__init__()
        super().dsp()
    def std_er(self):
        self.std_er = (self.dsp / self.size)**(1/2)
        print("標準誤差は" + str(self.std_er))
        
print("行う操作を選択してください")#作成したクラスのどれを使うか選択出来るようにifを使用する
n = input("1平均、2分散、3標準偏差、4不変分散、5標準誤差 ")
if(n == "1"):
    while True:
        p_avr = Avr()
        p_avr.avr()
        c = input("やりなおしますか yes or no ")
        if(c == "no"):
            break
        elif(c == "yes"):
            pass #動作を間違えた際にすぐやり直せるようにwhileとifを併用して、javaのdo-whileと同じことをする       
elif(n == "2"):
    while True:
        p_dsp = Dsp()
        p_dsp.dsp()
        c = input("やりなおしますか yes or no ")
        if(c == "no"):
            break
        elif(c == "yes"):
            pass
elif(n == "3"):
    while True:
        p_std_dev = Std_dev()
        p_std_dev.dev()
        c = input("やりなおしますか yes or no ")
        if(c == "no"):
            break
        elif(c == "yes"):
            pass
elif(n == "4"):
    while True:
        p_not_cng_dsp = Not_cng_dsp()
        p_not_cng_dsp.dsp()
        c = input("やりなおしますか yes or no ")
        if(c == "no"):
            break
        elif(c == "yes"):
            pass 
elif(n == "5"):
    while True:
        p_std_error = Std_error()
        p_std_error.std_er()
        c = input("やりなおしますか yes or no ")
        if(c == "no"):
            break
        elif(c == "yes"):
            pass 