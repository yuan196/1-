#朔望月
#游戏规则：随机生成三个二十四节气（可重复）分别作为玩家牌，人机牌与公共牌。玩家与人机均可选择使用公共牌。
# 牌面大小为牌面节气对应的2024年新历日期逐位相加。eg.霜降为10月23日，即1+0+2+3=6
#最终牌面最接近16的一方为获胜方
import random
player_score=0
computer_score=0
player_name=input('请输入玩家姓名：\n')
print('电脑角色：1.子鼠  2.丑牛  3.寅虎  4.卯兔  5.辰龙  6.巳蛇  7.午马  8.未羊  9.申猴  10.酉鸡  11.戌狗  12.亥猪\n')
computer_name_num=eval(input('请选择一位电脑角色：\n'))
names=['匿名','子鼠','丑牛','寅虎','卯兔','辰龙','巳蛇','午马','未羊','申猴','酉鸡','戌狗','亥猪']
if computer_name_num>=0 and computer_name_num<=12:
    computer_name=names[computer_name_num]
else:
    computer_name = names[0]
print(player_name,'VS',computer_name)
while True:
    play_public_num=random.randint(1,24)
    player_fist_num=random.randint(1,24)
    computer_fist_num=random.randint(1,24)
    days=['2024','立春','雨水','惊蛰','春分','清明','谷雨','立夏','小满','芒种','夏至','小暑','大暑','立秋','处暑','白露','秋分','寒露','霜降','立冬','小雪','大雪','冬至','小寒','大寒']
    play_public= days[play_public_num]
    player_fist = days[player_fist_num]
    computer_fist=days[computer_fist_num]
    day_dict={'年份':2024,'立春':6,'雨水':12,'惊蛰':8,'春分':5,'清明':8,'谷雨':14,'立夏':10,'小满':7,'芒种':11,'夏至':9,'小暑':13,'大暑':11,'立秋':15,'处暑':12,'白露':16,'秋分':13,'寒露':9,'霜降':6,'立冬':9,'小雪':6,'大雪':9,'冬至':6,'小寒':6,'大寒':3}
    print('公共牌是',play_public,'牌面大小为',day_dict.get(play_public))
    print(player_name,'的牌是',player_fist,'牌面大小为',day_dict.get(player_fist))
    reply=input('请选择是否使用公共牌：y/n\n')
    if reply=='y':
        player_answer=day_dict[play_public]+day_dict[player_fist]
    else:
        player_answer = day_dict[player_fist]
    print('最终',player_name,'的牌面大小为',player_answer)
    if abs(day_dict[computer_fist]-16)>=abs(day_dict[play_public]+day_dict[computer_fist]-16):
        computer_answer=day_dict[play_public]+day_dict[computer_fist]
        print(computer_name,'的牌是',computer_fist,'并使用公共牌','最终大小为',computer_answer)
    else:
        computer_answer = day_dict[computer_fist]
        print(computer_name, '的牌是', computer_fist, '未使用公共牌','最终大小为',computer_answer)
    if abs(player_answer-16)<abs(computer_answer-16):
        player_score+=1
        print(player_name,'胜利')
    elif abs(player_answer-16)>abs(computer_answer-16):
        computer_score+=1
        print(player_name, '失败')
    else:
        print(player_name,'与',computer_name,'平局')
    answer=input('是否继续游戏：y/n')
    if answer!='y':
        break
if player_score==computer_score:
    print('最终平局')
elif player_score > computer_score:
    print('最终胜利')
else :
    print('最终失败')
