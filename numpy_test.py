import numpy as np
#將這幾個長跑距離（公里）轉換為英里
print("將這幾個長跑距離公里轉換為英里")
distances = [1, 1.6, 3, 5, 10, 21.097, 42.195]
distances = np.array(distances)  #向量化vectorization執行，不用再用迭代(for loop)
dist_in_mile = distances * 0.62137
print(dist_in_mile)

#計算 A 與 B 的內積 C
print('計算 A 與 B 的內積 C')
A = [
    [1, 2],
    [4, 5]
]
B = [
    [4, 3],
    [2, 1]
]
A = np.array(A)
B = np.array(B)
C = A.dot(B)
print(C)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_arr = np.array(my_list)
print(my_list[1::2])
print(my_arr[my_arr % 2 == 0])
print(my_arr[my_arr < 7]) #booling indexing
print(my_arr[[0,1, 2, -3, -1]]) #fancy indexing

#函數介紹
print('函數介紹')
print(np.zeros(5, dtype=int))  #給5個0
print(np.ones((2, 2), dtype=float)) #2*2陣列的1
print(np.full((2, 2), 5566, dtype=int)) #2*2陣列的賦予值


#np.arange(start, stop, step) 創建從 start （包含）間隔 step 至 stop （不包含）的等差數列，使用方式同內建函數 range()
#np.linspace(start, stop, num) 創建從 start （包含）至 stop （包含）的均勻切割為 num 個資料點的數值陣列
print(np.arange(1, 10, 2))
print(np.linspace(1, 9, 5, dtype=int))

# np.random.random(size)
# np.random.normal(loc, scale, size) = (avg, std, size)
# np.random.randint(low, high, size) 隨機取值

arr = np.random.random(10000)

# ndarray 的屬性
# arr.ndim ：檢視 arr 有幾個維度
# arr.shape ：檢視 arr 的外型
# arr.size ：檢視 arr 的資料筆數，對一維陣列的意涵就像內建函數 len() 作用在 list 上一般
# arr.dtype ：檢視 arr 中同質資料的型態
print('ndarray 的屬性')

zero_d = np.array(5566)            # 零維陣列，純量
one_d = np.array([55, 66, 5566])   # 一維陣列
two_d = np.ones((3, 3), dtype=int) # 二維陣列
print("ndim:")
print(zero_d.ndim)
print(one_d.ndim)
print(two_d.ndim)
print("shape:")
print(zero_d.shape)
print(one_d.shape)
print(two_d.shape)
print("size:")
print(zero_d.size)
print(one_d.size)
print(two_d.size)
print("dtype:")
print(zero_d.dtype)
print(one_d.dtype)
print(two_d.dtype)

#從 ndarray 中取出單個資料值的方式與 list 相同，使用 arr[INDEX] 取值
print('從 ndarray 中取出單個資料值的方式與 list 相同，使用 arr[INDEX] 取值')
arr = np.array([55, 66, 56, 5566])
print("From start to stop:")
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[arr.size - 1])
print("From stop to start:")
print(arr[-1])
print(arr[-2])
print(arr[-3])
print(arr[-arr.size])


#面對二維以上的陣列，ndarray 支援使用 [i, j, …] 的方式取出位於第 i 列（row）、第 j 欄（column）… 的資料
print('面對二維以上的陣列，ndarray 支援使用 [i, j, …] 的方式取出位於第 i 列（row）、第 j 欄（column）… 的資料')
np.random.seed(42)
arr = np.random.randint(1, 10, size=(3, 4))
print(arr)
print(arr[1, 1]) # 3 located at (1, 1)
print(arr[2, -3]) # 4 located at (2, -3)


#使用 arr[start:stop:step] 取出陣列的片段
print('使用 arr[start:stop:step] 取出陣列的片段')
arr = np.arange(10, 20)
print(arr[::]) # all defaults
print(arr[::2]) # step=2
print(arr[:5]) # stop=5, exclusive
print(arr[5:]) # start=5, inclusive
print(arr[::-1]) # step=-1, reverse

#布林索引（Boolean indexing）指的是以外觀相同的陣列傳入布林值，將位置為 True 的資料篩選出來
print('布林索引（Boolean indexing）指的是以外觀相同的陣列傳入布林值，將位置為 True 的資料篩選出來')
np.random.seed(0)
arr = np.random.randint(1, 100, size=(10))
is_odd = arr % 2 == 1
print(arr)
print(is_odd)
print(arr[is_odd])


#arr.reshape(m, n, ...) 將數值陣列重塑成運算所需要的外觀
#arr.ravel() 將外觀為 (m, n, …) 的數值陣列調整回一維
print('重塑外觀')
arr = np.arange(1, 10)
print(arr)
print(arr.shape)
print(arr.reshape(3, 3))
print(arr.reshape(3, 3).shape)

# [1 2 3 4 5 6 7 8 9]
# (9,)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# (3, 3)

#ndarray 有一個重要的預設特性稱為「不複製」，因此不論在切割或重新宣告的情境中都是創建陣列的 View，而非複製另一個陣列，這代表著對以 View 型式存在的子陣列（Sub-array）更新會改動到原始陣列
print('實踐陣列的複製，可以運用其 .copy() 方法')
arr = np.arange(1, 10)
mat = arr.copy()
mat = mat.reshape(3, 3)
mat[1, 1] = 5566
print(mat)
print(arr)

print('合併陣列, np.concatenate([arr0, arr1, ...], axis)')

upper_arr = np.arange(1, 5).reshape(2, 2)
lower_arr = np.arange(5, 9).reshape(2, 2)
print("Merge with np.concatenate():")
print(np.concatenate([upper_arr, lower_arr])) # default axis=0 垂直2*2變2*4列
print("Merge with np.vstack():")
print(np.vstack([upper_arr, lower_arr]))

left_arr = np.zeros(4, dtype=int).reshape(-1, 1)
right_arr = np.ones(4, dtype=int).reshape(-1, 1)
print("Merge with np.concatenate():")
print(np.concatenate([left_arr, right_arr], axis=1))
print("Merge with np.hstack():")
print(np.hstack([left_arr, right_arr]))

print('拆分陣列')
arr = np.arange(11, 21)
arr0, arr1, arr2 = np.split(arr, [2, 5])
print(arr0, arr1, arr2)
#[11 12] [13 14 15] [16 17 18 19 20]

arr = np.arange(24).reshape(6, 4)
print(arr)
print("======")
arr0, arr1, arr2 = np.vsplit(arr, [1, 3])
print(arr0)
print("======")
print(arr1)
print("======")
print(arr2)

arr = np.arange(24).reshape(4, 6)
print(arr)
print("======")
arr0, arr1, arr2 = np.hsplit(arr, [1, 3])
print(arr0)
print("======")
print(arr1)
print("======")
print(arr2)


# long_arr = np.random.randint(1, 101, size=1000000)
# %timeit [1/i for i in long_arr]

# long_arr = np.random.randint(1, 101, size=1000000)
# %timeit 1 / long_arr

print('陣列運算')
# np.add() ：同 + 運算符
# np.subtract() ：同 - 運算符
# np.multiply() ：同 * 運算符
# np.divide() ：同 / 運算符
# np.power() ：同 ** 運算符
# np.floor_divide() ：同 // 運算符
# np.mod() ：同 % 運算符
arr = np.array([2, 2, 2, 2, 2])
powers = np.arange(1, 6)
print(arr)
print(powers)
print(arr**powers) #=print(np.power(arr, powers))
print("Broadcasting:")
print(2 ** powers) #2的五次方

#上述如用原生list[1,2,3,4,5] * 2會等於複製一個一樣list[1,2,3,4,5,1,2,3,4,5]進去，如用munpy可得list內純量*2

# [2 2 2 2 2]
# [1 2 3 4 5]
# [ 2  4  8 16 32]
# Broadcasting:
# [ 2  4  8 16 32]

arr = np.arange(9)
print(arr % 2 == 0)
print(arr[arr % 2 == 0])

# [ True False  True False  True False  True False  True]
# [0 2 4 6 8]

print('隨堂練習：從隨機(100抽20個)陣列中挑出偶數')
arr = np.floor(100* np.random.random(20))  #floor= 向下取整數；np.ceil 向上取整；np.around 四舍五入
is_even = (arr % 2) == 0
print(arr[is_even])


print('隨堂練習：從隨機陣列中挑出質數')
arr = np.floor(100* np.random.random(50))
arr = arr.astype(int)

def is_prime(x):
    div_cnt = 0
    for i in range(1, x+1):
        if x % i == 0:
            div_cnt += 1
        if div_cnt > 2:
            break
    return div_cnt == 2
is_prime_list = [is_prime(i) for i in arr] #將隨機產生數投入is_prime的(x), 如果該數....
print(arr[is_prime_list])

print('假如希望對數值陣列使用的通用函數是為自己需求量身訂製的，這時可以將函數定義後以 np.vectorize() 轉換為一個通用函數')
is_prime_ufunc = np.vectorize(is_prime)
print(arr[is_prime_ufunc(arr)])

print('np.where 条件选取，numpy.where(condition[, x, y])，根据条件 condition 从 x 和 y 中选择元素，当 condition 为 True 时，选 x，否则选 y。')
data = np.random.random([2, 3])
print(data)
result = np.where(data > 0.5, data, 0)
print(result)


print('聚合函數,即在陣列中取一')
arr = np.arange(10) #0~9
print(np.power(arr, 2))
print(np.sum(arr))

# 多數具有可運算遺漏值的相對應函數
# np.sum 與 np.nansum
# np.prod 與 np.nanprod
# np.mean 與 np.nanmean
# np.median 與 np.nanmedian
# np.std 與 np.nanstd
# np.var 與 np.nanvar
# np.min 與 np.nanmin
# np.max 與 np.nanmax
# np.argmin 與 np.nanargmin
# np.argmax 與 np.nanargmax

mat = np.arange(1, 16).reshape(3, 5).astype(float)  #reshape(列, 欄)
print(mat)
print(np.sum(mat)) # 1 個輸出
print(np.sum(mat, axis=0)) # 5 個輸出
print(np.sum(mat, axis=1)) # 3 個輸出

mat[2, 4] = np.nan
print(mat)
print(np.sum(mat))
print(np.nansum(mat))