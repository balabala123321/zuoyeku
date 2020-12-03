
# coding: utf-8

# In[1]:


def move(players,step):
    # 移动step前的元素到末尾
    num = step - 1
    while num > 0:
        tmp = players.pop(0)
        players.append(tmp)
        num = num - 1
    return players # 根据step做了元素的移动
def play(players,step,alive):
    """
    模拟约瑟夫环问题的函数
    
    Input:
    players：玩家人数
    step：数到step数字的人淘汰
    alive：幸存人数，即游戏结束
    
    Output:
    返回一个列表，列表中元素为幸存者编号

    """
    list1 = [i for i in range(1,players+1)]
    
    # 进入游戏的循环，每次数到step淘汰，step之前的元素移到列表末尾
    # 游戏结束的条件：列表剩余人数小于alive
    while len(list1)>alive: 

        list1 = move(list1,step)
        
        list1.pop(0) # 此时的step的元素在列表第一个位置，使用pop(0)从列表中删除
    return list1
players_num = int(input("请输入参加游戏的人数:"))
step_num = int(input("请输入淘汰的数字："))
alive_num = int(input("请输入幸存人数："))

alive_list = play(players_num,step_num,alive_num)
print(alive_list)

