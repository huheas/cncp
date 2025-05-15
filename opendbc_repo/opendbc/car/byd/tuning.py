#!/usr/bin/env python3

class Tuning:

  STEER_ANGLE_OFFSET_DEG = -2.01

  LAT_ANGLE_MODE = False # 横向控制模式，True为角度模式，False力矩模式

  # 仅角度模式有效
  # 这是重要的横向控制参数。例如下面的就是指速度8.3m/s的时候，P为0.13，I为0.025，随着速度提高到27.8，P会增加到0.20，I会增加到0.05
  # 可以按需求增加插值点, 想要舒服就I多一点点P少一点点，想要响应速度就反之。参考PI整定办法。
  LATERAL_BP = [8.3  ,  27.8] #8.3m/s=30kph, 27.8m/s=100kph 插值点的速度输入，单位是米每秒
  LATERAL_KP = [0.6  ,  0.6] # PID的P
  LATERAL_KI = [0.0  ,  0.0] # PID的I
  LATERAL_KF = 0.000072 # 控制环的前馈，如果进入过早（晚）和/或行驶过远内侧（外侧），则 kf 过高（低）

  #仅力矩模式有效
  LAT_TORQUE_USE_SIGLIN = False # 力矩模式下有效，True为使用siglin，False为使用linear
  LAT_SIGLIN_TABLE = [6.824, 1.0, 0.321, 1.0] #siglin模式有效
  LAT_TORQ_KP = 1.0
  LAT_TORQ_KI = 0.1
  LAT_ACCEL_FACTOR = 1.3717421124828 #仅Linear有效
  LAT_FRICTION = 0.15

  #横向速度限制参数
  LAT_STEER_RATE_LIMIT_ENABLE = False
  LAT_STEER_RATE_DEG_LIMIT_BP = [8.3,  27.8] #m/s
  LAT_STEER_RATE_DEG_LIMIT    = [132  , 64]   #deg/s, 注意是4的倍数
  LAT_STEER_RATE_LIMIT_DEACTIVE = 0.002
  LAT_STEER_RATE_LIMIT_ACTIVE   = 0.005

  STEER_ACTUATOR_DELAY = 0.02 # 如果转弯过早则减少,如果转弯太晚则增加
  STEER_LIMIT_TIMER = 0.4

  #自动参数整定，在调试时可以设为False
  AUTO_TUNING = True


  # OP自己的纵向控制参数
  LONG_BP = [0.]
  LONG_KP = [0.8]
  LONG_KI = [0.3]

  #速度修正参数
  DASHSPEED_BP = [30,   60,   90,  120] #BP是车速
  DASHSPEED_FP = [0.94, 1.0,  1.0, 1.0] #修正百分比

  # modified stock long control 原车long控制的速度平滑百分比设定, 例如下面40米以内，则加速率是原来的70%，减速率是原来的100%
  K_ACCEL_BP  = [40,  50,  60,  70,  80]  # meters BP是离前车距离

  K_ACCEL_POS_4BAR = [0.7, 0.7, 0.7, 0.6, 0.6] # acceleration 加速的百分比
  K_ACCEL_NEG_4BAR = [1.0, 0.8, 0.7, 0.7, 0.6] # deceleration 减速的百分比

  K_ACCEL_POS_3BAR = [0.7, 0.7, 0.7, 0.7, 0.6] # acceleration 加速的百分比
  K_ACCEL_NEG_3BAR = [1.0, 0.9, 0.8, 0.7, 0.6] # deceleration 减速的百分比

  K_ACCEL_POS_2BAR = [0.9, 0.8, 0.7, 0.7, 0.6] # acceleration 加速的百分比
  K_ACCEL_NEG_2BAR = [1.0, 0.9, 0.9, 0.7, 0.6] # deceleration 减速的百分比

  K_ACCEL_POS_1BAR = [1.0, 0.9, 0.8, 0.8, 0.7] # acceleration 加速的百分比
  K_ACCEL_NEG_1BAR = [1.0, 1.0, 0.9, 0.7, 0.7] # deceleration 减速的百分比

  # 人为扭动方向盘的阈值，大于这个值才认为方向盘被故意扭动了，变道辅助涉及它
  STEER_PRESSED_THRESHOLD = 60

  # 禁用EPS故障检查, 某些车有EPS固件比较奇怪报错的话，则可以设为True
  DISABLE_HAN_EPS_FAULTCHECK = False
