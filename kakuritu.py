
#平均を計算
class Avr():#分散等で同じ動作を行うため、クラス化
    def __init__(self):
        self.size = int(input("データの数を入力して下さい"))
        self.list = []
        self.sum = float(0)
        for n in range(self.size):
            self.list.append(float(input("データの値を入力してください")))
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
        print("標準偏差は" + self.dev) 
       
  
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
        
#母平均区間推定
class Section():
    def __init__(self):
        self.size = float(input("数は？"))
        self.avr2 = float(input("標本平均は？"))
        self.dsp2 = float(input("分散は？"))
        self.dsb2 = float(input("正規分布z(α)？"))
    def section(self):
        self.section1 = self.avr2 + self.dsb2 * (self.dsp2**(1/2) / self.size**(1/2))
        self.section2 = self.avr2 - self.dsb2 * (self.dsp2**(1/2) / self.size**(1/2))
        print("[" + str(self.section2) + " " + str(self.section1) + "]")

#仮説推定
class Estimate():
    def __init__(self):
        self.avr = float(input("母平均は？"))
        self.size = float(input("数は？"))
        self.avr2 = float(input("標本平均は？"))
        self.dsp = float(input("分散は？"))
    def Z(self):
        self.z = (self.avr - self.avr2) / (self.dsp**(1/2) / self.size**(1/2))
        if(self.z < 0):
            self.z = -1 * self.z
        print("Z = " + str(self.z))
        set = input("1,H_1:m≠m_0 2,H_1:m>m_0 3,H_1:m<m_0の中で選択")
        if(set == "1"):
            self.z_alf = float(input("z(α)は？"))
            if(self.z > self.z_alf):
                print("仮説H_0を棄却する")
            else:
                print("H_0採択する")
        if(set == "2"):
            self.z_alf = float(input("z(2α)は？"))
            if(self.z > self.z_alf):
                print("仮説H_0を棄却する")
            else:
                print("H_0採択する")
        if(set == "3"):
            self.z_alf = float(input("z(2α)は？"))
            if(self.z < -1 * self.z_alf):
                print("仮説H_0を棄却する")
            else:
                print("H_0採択する")

print("行う操作を選択してください")#作成したクラスのどれを使うか選択出来るようにifを使用する
n = input("1平均、2分散、3標準偏差、4不変分散、5標準偏差、6母平均区間推定、7仮説推定")
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
        c = input("やりなおしますか yes or no")
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
elif(n == "6"):
    while True:
        p_section = Section()
        p_section.section()
        c = input("やりなおしますか yes or no ")
        if(c == "no"):
            break
        elif(c == "yes"):
            pass 
elif(n == "7"):
    while True:
        p_estimate = Estimate()
        p_estimate.Z()
        c = input("やりなおしますか yes or no ")
        if(c == "no"):
            break
        elif(c == "yes"):
            pass 
        

        
    
    