# coding:utf-8 

from uie_pytorch.uie_predictor import UIEPredictor
from pprint import pprint

schema = ['时间', '选手', '赛事名称'] # Define the schema for entity extraction
ie = UIEPredictor(model='uie-base', schema=schema)
pprint(ie("2月8日上午北京冬奥会自由式滑雪女子大跳台决赛中中国选手谷爱凌以188.25分获得金牌！")) # Better print results using pprint
