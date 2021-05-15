import math
from hoshino import Service


sv = Service("击剑路径计算", enable_on_default=False)

@sv.on_rex(r'击剑(路径|路线)( )?(.{0,5})$')
async def arena_route(bot,ev):
    num=int(ev['match'].group(3))
    r={}
    rank = 0
    while num>1:
        rank += 1
        if (num<=11):
            num = 1
        elif (num<69):
            num -= 10
        else:
            num = math.floor(num*0.85)
        r[rank] = num
    await bot.send(ev,"最优击剑路径(大概)："+','.join(map(str,list(r.values())[:5])),at_sender=True)
