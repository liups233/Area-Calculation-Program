def rectangle_area(a, b):
    r_area = float(a) * float(b)
    return r_area
# 矩形面积


def triangle_area(a, h):
    t_area = 1/2 * float(a) * float(h)
    return t_area
# 三角形面积


def rotundity_area(r):
    pi = 3.14
    r_area = float(r) ** 2 * pi
    return r_area
# 圆形面积


def trapezoid_area(a, b, h):
    t_area = 1/2 * (a + b) * h
    return t_area
# 梯形面积


def computing():
    while True:
        print('''
    [1]计算矩形面积
    [2]计算三角形面积
    [3]计算圆形面积
    [4]计算梯形面积
    ''')
        mode1 = input('输入选项: ')
        if mode1 == '1':
            while True:
                while True:
                    length = input('输入长: ')
                    if length.replace('.', '').isdigit():
                        length = float(length)
                        break
                    else:
                        print('''
                            
    输入一个数字!
                            
                        ''')
                if length <= 0:
                    print('''
                        
    长必须为正!
                        
                    ''')
                else:
                    break
            while True:
                while True:
                    weight = input('输入宽: ')
                    if weight.replace('.', '').isdigit():
                        weight = float(weight)
                        break
                    else:
                        print('''
                            
    输入一个数字!
                            
                        ''')
                if weight <= 0:
                    print('''
                        
    宽必须为正!
                        
                    ''')
                else:
                    break
            area = rectangle_area(length, weight)
            print('面积为:', area)
            break

        elif mode1 == '2':
            while True:
                while True:
                    bottom = input('输入底: ')
                    if bottom.replace('.', '').isdigit():
                        bottom = float(bottom)
                        break
                    else:
                        print('''
                        
    输入一个数字!
                        
                        ''')
                if bottom <= 0:
                    print('''
        
    底必须为正!
        
                    ''')
                else:
                    break
            while True:
                while True:
                    height = input('输入高: ')
                    if height.replace(',', '').isdigit():
                        height = float(height)
                        break
                    else:
                        print('''
                        
    输入一个数字!
                        
                        ''')
                if height <= 0:
                    print('''
    
    高必须为正!
    
                    ''')
                else:
                    break
            area = triangle_area(bottom, height)
            print('面积为:', area)
            break

        elif mode1 == '3':
            while True:
                while True:
                    radius = input('输入半径: ')
                    if radius.replace('.', '').isdigit():
                        radius = float(radius)
                        break
                    else:
                        print('''
                        
    输入一个数字!
                        
                        ''')
                if radius <= 0:
                    print('''
                    
    半径必须为正!
                    
                    ''')
                else:
                    break
            area = rotundity_area(radius)
            print('面积为:', area)
            break

        elif mode1 == '4':
            while True:
                while True:
                    upper = input('输入上底: ')
                    if upper.replace('.', '').isdigit():
                        upper = float(upper)
                        break
                    else:
                        print('''
                        
    输入一个数字!
                        
                        ''')
                if upper <= 0:
                    print('''
                    
    上底必须为正!
                    
                    ''')
                else:
                    break
            while True:
                while True:
                    lower = input('输入下底: ')
                    if lower.replace('.', '').isdigit():
                        lower = float(lower)
                        break
                    else:
                        print('''
                        
    输入一个数字!
                        
                        ''')
                if lower <= 0:
                    print('''
    
    下底必须为正!
    
                    ''')
                else:
                    break
            while True:
                while True:
                    height = input('输入高: ')
                    if height.replace('.', '').isdigit():
                        height = float(height)
                        break
                    else:
                        print('''
                        
    输入一个数字!
                        
                        ''')
                if height <= 0:
                    print('''
    
    高必须为正!
    
                    ''')
                else:
                    break
            area = trapezoid_area(upper, lower, height)
            print('面积为:', area)
            break
        else:
            print('''
            
    输入正确数字!
            
            ''')


program_name = '面积计算程序'
print(program_name.center(50))
print()
while True:
    computing()
    print('''
    [1]继续计算
    [2]退出
    ''')
    while True:
        mode2 = input('输入选项: ')
        if mode2 == '1':
            break
        elif mode2 == '2':
            exit()
        else:
            print('''
            
    输入正确选项!        
          
            ''')
