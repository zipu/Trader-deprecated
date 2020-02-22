import sys
sys.path.append('..')

import matplotlib.pyplot as plt
import numpy as np
from pandas.plotting import register_matplotlib_converters


def bar_chart(ax, quotes, linewidth=1, colors=['k','k'], background='lightgoldenrodyellow'):
    """
    * 바차트
    * Input:
     - ax: 차트를 그릴 pyplot axis
     - quotes: pandas ohlc 데이터 column 명이 반드시 'open/high/low/close'여야함
     - linewidth: 바 굻기
     - colors: 상승바/하락바 색
     - background: 배경색
    """
    register_matplotlib_converters()
    for idx, color in enumerate(colors):
        cond = quotes['close']>= quotes['open']
        data = quotes[cond] if idx == 0 else quotes[~cond]
        ohlc = data[['open','high','low','close']].values
        o,h,l,c = np.squeeze(np.split(ohlc, 4, axis=1))
        
        #x축 세팅
        dates =data.index.values
        
        if dates.dtype == 'M8[ns]':
            offset = np.timedelta64(10, 'h')
        elif dates.dtype == 'int64':
            offset = 0.45
        
        
        ax.vlines(dates, l, h, linewidth=linewidth, color=color)
        ax.hlines(o, dates-offset, dates, linewidth=linewidth, color=color)
        ax.hlines(c, dates, dates+offset, linewidth=linewidth, color=color)

    #style
    ax.grid(linestyle='--')
    ax.set_facecolor(background)
    ax.yaxis.tick_right()
    return ax