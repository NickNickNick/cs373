colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green', 'green', 'green']


motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]


def calculate():

    #DO NOT USE IMPORT
    #ENTER CODE BELOW HERE
    #ANY CODE ABOVE WILL CAUSE
    #HOMEWORK TO BE GRADED
    #INCORRECT
  
    p = []
   
for i in range(len(colors)):
    p.append([1./(len(colors)*len(colors[i]))] * len(colors[i]))

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        s=[]
        for j in range(len(p[i])):
            hit = (Z == colors[i][j])
            s.append(p[i][j] * (hit * sensor_right + (1-hit) *(1-sensor_right)))
        q.append(s)
    zz=0
    for i in range(len(p)):
        for j in range(len(p[i])):
            zz =zz+q[i][j]
    #print "Z",zz,"ненормализ",q
    for i in range(len(q)):
        for j in range(len(p[i])):
            q[i][j]=q[i][j]/zz
    #print "нормализ.",q
    return q


def move(p, U):
    q = []
    qq=p
    for i in range(len(p)):
        ss=[]
        for j in range(len(p[i])):
            s = p_move * p[i][(j-U[0]) % len(p[i])]
            s = s + (1-p_move) * p[i][(j-U[0]+1) % len(p[i])]
            ss.append(s)
        q.append(ss)
    print "Q",q
    for j in range(len(p[i])):
        for i in range(len(p)):
            s = p_move * q[(i-U[1]) % len(p)][j]
            s = s + (1-p_move) * q[(i-U[0]+1) % len(p)][j]
            qq[i][j]=s
    print "QQ",qq
    return qq

for k in range(len(measurements)):
    p = sense(p, measurements[k])
    p = move(p, motions[k])




    #Your probability array must be printed 
    #with the following code.

    show(p)
    return p

