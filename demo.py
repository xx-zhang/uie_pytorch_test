# coding:utf-8 

from uie_pytorch.uie_predictor import UIEPredictor
from pprint import pprint

def test1():
    schema = ['时间', '选手', '赛事名称'] # Define the schema for entity extraction
    ie = UIEPredictor(model='uie-base', schema=schema, use_fp16=False, )
    pprint(ie("2月8日上午北京冬奥会自由式滑雪女子大跳台决赛中中国选手谷爱凌以188.25分获得金牌！")) # Better print results using pprint


def test3():
    schema = ['时间', '攻击者', '被攻击者', '攻击次数', '攻击者地域'] # Define the schema for entity extraction
    ie = UIEPredictor(model="uie-base", task_path='/data/workdir/models/uie_base_pytorch/', schema=schema, use_fp16=False, )
    pprint(ie("2023年11月11日12点13分 目标192.168.33.1 遭受到归属到新疆的IP:52.22.11.69 攻击20次。")) # Better print results using pprint

test3() 
