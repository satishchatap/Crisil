import numpy as np
import pandas as pd
from pylab import mpl, plt
from itertools import combinations
import pytest
import json
from py_linq import Enumerable

"""[summary]

Raises:
    ValueError: [description]

Returns:
    [type]: [description]
    """


class crisil_test:
    @staticmethod
    def movavg(f: list, w: int):
        # 1 lets make dataframe using pandas
        f_series = pd.Series(f)
        # 2 do rolling sum of 3 values.
        windows = f_series.rolling(w)
        # 3 get mean of windows to idetify average.
        ma = windows.mean()
        # 4 result or moving average list.
        ma_list = ma.tolist()
        # 5 first 2 set will have wrong calc as there is no 3 element to calc. Ignore it.
        #  But as requested for graph we have to keep it so that coordinates of plot matches.
        #ma_no_nans = ma_list[w - 1:]
        return ma_list

    @staticmethod
    def least_int(input: list):
        # 1 have to make collection of all possible some of given array along with all array items.
        sum_val = []
        # 2 cummulitive sum wouldn't be enough.
        #cum_sum =list( np.array(input).cumsum())

        # 3 find all combination of sum
        #  for each item we have to combine with remaining array item and get sum of subset.
        for item in range(0, len(input)+1):
            for sub_set in combinations(input, item):
                sum_val.append(sum(sub_set))

        # print(sum_val)
        # 4 missing element should be found element.
        found = 0
        # 5 sequential value counter
        i = 1
        # 6 sum value might have some dups, so remove it and get as list for easy count operation.
        sum_val = list(np.unique(sum_val))
        # 7 till we found missing element check sequence exists in cobination sum.
        while(found == 0):
            # 7.1 if found increment counter and continue.
            if(sum_val.count(i) > 0):
                i += 1
                continue
            # 7.2 this is our missing element.
            found = i

        return found

    # Utility to find position of value in given two dimensional array.
    # data = list[][]
    # search= search value.
    @staticmethod
    def index_2d(data, search):
        for i, e in enumerate(data):
            try:
                return i, e.index(search)
            except ValueError:
                pass
        raise ValueError("{} is not in list".format(repr(search)))

    # Test 3: Kill pawn using Rook. Rook can go Vertical & Horizontal,
    # easy would be getting H & V array and traverse to find pawn withouth any occupied block in root.
    @staticmethod
    def kill_pawn(input: list):
        # 1 define result count
        kill_count: int = 0
        # 2 get numpy array from list. we need to traverse through indexes.
        m = np.array(input)
        # print(m)
        # 3 get position of Rook
        position = crisil_test.index_2d(input, "R")
        # print(position)
        # 4 horizontal array
        hr_list = m[position[0]]
        # 5 HR+ traverse in +ve direction
        for item in range(position[1]+1, len(hr_list)):
            # 5.1 found pawn
            if(hr_list[item] == "p"):
                kill_count += 1
                break
            else:
                # 5.2 if not pawn it should be empty
                if(hr_list[item] == "."):
                    continue
            # 5.3 if not empty or pawn shouldn't continue.
            break
        # 6 HR- same as 5 in -ve direction
        for item in range(position[1]-1, -1, -1):
            # print(hr_list[item])
            if(hr_list[item] == "p"):
                kill_count += 1
                break
            else:
                if(hr_list[item] == "."):
                    continue
            break

        # 7 vertical array
        vr_list = m[:, position[1]]
        #print (vr_list)
        # 8 VR+ traverse in +ve direction
        for item in range(position[0]+1, len(hr_list)):
            # print(vr_list[item])
            if(vr_list[item] == "p"):
                kill_count += 1
                break
            else:
                if(vr_list[item] == "."):
                    continue
            break
        # 9 VR- same as 8 in -ve direction
        for item in range(position[0]-1, -1, -1):
            # print(vr_list[item])
            if(vr_list[item] == "p"):
                kill_count += 1
                break
            else:
                if(vr_list[item] == "."):
                    continue
            break

        return kill_count





class SearchByTag:

    def __init__(self, data_file, query_tag):
        with open(data_file) as data_file:
            self._data = json.load(data_file)
        self.query = query_tag

    def search(self):
        pass

    def first(self):
        pass

def searchTag():
    t=''

    t_dict = json.loads(t)
    if(not t_dict):
         raise ValueError("No items found")

    t_items = t_dict["items"];
    i=0
    while i<len(t_items):
        yield t_items[i]
        i+=1


class Pump:
     def __init__(self, fuelInLtr,timeSpent,isVaccant,order):
        self.FuelInLtr=fuelInLtr
        self.TimeSpent=timeSpent
        self.IsVaccant=isVaccant
        self.Order=order



def solution1(A, X, Y, Z):
    # write your code in Python 3.6
     if (A[0] > X and A[0] > Y and A[0] > Z):
                return -1;
     pump1 = Pump(X,0,true, 1)
     pump2 = Pump(Y,0,true, 1)
     pump3 = Pump(Z,0,true, 1)

     pumps =[pump1,pump2,pump3]
     
     waitingTime = 0;

     for c in A:
         isFree = [r for r in pumps if r.FuelInLtr >= c and x.IsVaccant].sort(key=lambda t: t.Order)
         if( isFree):
             p= isFree[0]
             p.FuelInLtr-=c
             p.TimeSpent = c
             p.IsVaccant = false
         else:
             next =  [r for r in pumps if r.FuelInLtr > c]
             next =sorted( sorted(next,key=lambda t: t.TimeSpent, reversed=true),key=lambda t: t.Order)
             if(not next):
                 return -1;
             else:
                 next[0].IsVaccant = false;
                 waitingTime += next[0].TimeSpent;
                 next[0].TimeSpent = c;
                 for item in range[1,len(pumps)]:
                    if(item.Order == next[0].Order):
                        pumps[item].IsVaccant = false
                        pumps[0].TimeSpent = c;

     return waitingTime;


query = "crime"
for val in searchTag():
    print(val)
    if("tags" in val):
        if(query in val["tags"]):
            print(val)
            break
  #  for i in range(1,len(t_items)):
   #     print(t_items[i])

# Test 1
f = [1, 2, 3, 7, 9]
w = 3
mv = crisil_test.movavg(f, w)
print("Test 1 Result: " + str(mv))

plt.plot(f, mv)
plt.title('Test 1 Result Plot')

# Test 2
x = [1, 2, 2, 5, 7]
print("Test 2 Result: " + str(crisil_test.least_int(x)))
input = [[".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", "R", ".", ".", ".", "p"],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."]]
print("Test 3 Result: " + str(crisil_test.kill_pawn(input)))


