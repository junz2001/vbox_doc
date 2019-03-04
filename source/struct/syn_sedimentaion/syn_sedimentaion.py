######################################
# title: 同构造沉积
# date: 2019-01-19
# authors: 李长圣
# E-mail: sheng0619@163.com
# more info, see www.geovbox.com
#######################################
#从 0000046000.sav <版本1.3> 计算节点恢复，由 一个实例学会VBOX 生成
RES 0000046000.sav
# 每次 100 步更新一次进度条
SET stepbar 100
#设置墙的挤压速度 x方向速度为2.0
WALL id 1 xv 2.0
#设置墙的挤压量x方向推进1000.0，每挤压2000.0保存一次计算结果
IMPLE wall id 1 xmove 1000.0 save 2000.0 print 1000.0 ps 1000.0

##################################### 沉积 #####################################
#停止挤压，墙的x方向速度改为0.0
WALL id 1 xv 0.0
#沉积。在挤压前端12000～40000.0上方，沉积约 1 km 颗粒。y的范围需要设置为4000-6000。
#经验：颗粒充填满2km范围，沉积之后的地层厚度约为1km
GEN NUM 100000.0 rad discrete 60.0 80.0,  x ( 12000.0, 40000.0), y ( 4000.0, 6000.0), COLOR red GROUP sed
#设置沉积颗粒 GROUP=sed 的微观参数
PROP DENSITY 2.5e3, fric 0.3, shear 2.9e9, poiss 0.2, damp 0.4, hertz range GROUP sed
#计算2000步，让颗粒沉积下来
SET print 100 #每 500 步输出一次计算结果
CYC 2000
################################################################################

#设置墙的挤压速度 x方向速度为2.0
WALL id 1 xv 2.0
#设置墙的挤压量x方向推进5000.0，每挤压2000.0保存一次计算结果
IMPLE wall id 1 xmove 5000.0 save 2000.0 print 1000.0 ps 1000.0

#计算停止
STOP
