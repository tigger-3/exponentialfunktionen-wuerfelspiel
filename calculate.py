import random
# for visualization:
import graphcreator


class Wuerfel:
    def __init__(self, minimum=1, maximum=6):
        #   initialize minimum and maximum
        self.minimum = minimum
        self.maximum = maximum

    def wuerfeln(self) -> int:
        out = random.randrange(self.minimum, self.maximum + 1)
        return out


class Wurflist:
    def __init__(self, minimum=1, maximum=6):
        #   initialize w as wuerfel and wuerfe as list
        self.w = Wuerfel(minimum, maximum)
        self.wuerfe = []

    def werfen(self):
        wurf = self.w.wuerfeln()
        self.wuerfe.append(wurf)
        return wurf

    def get_wuerfe(self):
        return self.wuerfe


mlist = []
plist = []
olist = []
inpt = int(input("Number of Dices: "))
i = 0
while i < inpt:
    mlist.append(Wurflist())
    plist.append(Wurflist())
    i += 1
# n=0
m = 0
data = []
datasorted = []
dataraw = []
while mlist.__len__() > 0:
    numlist = []
    rawlist = []
    d = []
    m += 1
    i = 0
    while i < mlist.__len__():
        zahl = str(mlist[i].werfen())
        numlist.append(zahl)
        rawlist.append(zahl)
        if int(zahl) == 6:
            olist.append(mlist[i])
            mlist.pop(i)
            d.append(True)
        else:
            d.append(False)
            i += 1
    d.sort(reverse=True)
    data.append(d)
    dataraw.append(rawlist)
    numlist.sort(reverse=True)
    datasorted.append(numlist)

# done visualize data
f = graphcreator.setup_folder(inpt)
graphcreator.convertmatrix(data, f, "black-white", data.__len__(), inpt)
graphcreator.convertmatrix(dataraw, f, "unsorted", dataraw.__len__(), inpt)
graphcreator.convertmatrix(datasorted, f, "sorted_by_numbers", datasorted.__len__(), inpt)
print("done")
