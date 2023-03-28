import pandas as pd
import numpy as np

#이동평균선(데이터, 기간)
def moving_average(data, window):
    ma = pd.Series(data['close'].rolling(window=window).mean(), name='MA_' + str(window))
    return ma

#RSI(데이터, 기간)
def relative_strength_index(data, n):
    delta = data['close'].diff()
    delta = delta[1:]
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up = up.rolling(window=n).mean()
    roll_down = down.abs().rolling(window=n).mean()
    rs = roll_up / roll_down
    rsi = 100.0 - (100.0 / (1.0 + rs))
    return rsi

#스토캐스틱(데이터, 기간)
def stochastic(data, n):
    high = data['high'].rolling(window=n).max()
    low = data['low'].rolling(window=n).min()
    stoch = 100 * (data['close'] - low) / (high - low)
    return stoch

#볼린저밴드(데이터, 기간)
def bollinger_bands(data, window):
    ma = data['close'].rolling(window=window).mean()
    std = data['close'].rolling(window=window).std()
    upper_band = ma + 2 * std
    lower_band = ma - 2 * std
    return upper_band, lower_band

#MACD(데이터, 작은 넓이, 큰 넓이)
def moving_average_convergence_divergence(data, smaller, bigger):
    emas = data['close'].ewm(span=smaller, adjust=False).mean()
    emab = data['close'].ewm(span=bigger, adjust=False).mean()
    macd = emas - emab
    signal = macd.ewm(span=9, adjust=False).mean()
    return macd, signal

#Parabolic SAR
# AF 초기값은 0.02, 최대값은 0.2, 감소치는 0.02로 설정
def parabolic_sar(data, af=0.02, max_af=0.2, af_inc=0.02):
    # 초기값 설정
    high = data['high']
    low = data['low']
    psar = data['close'][0:len(data)]
    psarbull = np.zeros(len(data))
    psarbear = np.zeros(len(data))
    bull = True
    af_current = af
    psar[0] = data['close'][0]
    psarbull[0] = psar[0] - 0.1
    psarbear[0] = psar[0] + 0.1
    
    # 파라볼릭 SAR 계산
    for i in range(1, len(data)):
        if bull:
            psar[i] = psar[i - 1] + af_current * (high[i - 1] - psar[i - 1])
        else:
            psar[i] = psar[i - 1] + af_current * (low[i - 1] - psar[i - 1])
        
        # 추세 변경 여부 판단
        if bull:
            if low[i] < psar[i]:
                bull = False
                psar[i] = high[i - 1]
                af_current = af
        else:
            if high[i] > psar[i]:
                bull = True
                psar[i] = low[i - 1]
                af_current = af
        
        # AF 조절
        if bull:
            if high[i] > psar[i - 1]:
                af_current = min(af_current + af_inc, max_af)
        else:
            if low[i] < psar[i - 1]:
                af_current = min(af_current + af_inc, max_af)
        
        # SAR 값이 어느 쪽에 있는지 판단
        if bull:
            psarbull[i] = psar[i]
        else:
            psarbear[i] = psar[i]
    
    return psar, psarbull, psarbear


#ADX(데이터, 기간)
def ADX(df, n=14):
    df = df.copy()
    df['TR'] = np.max([df['high'] - df['low'], abs(df['high'] - df['close'].shift()),
                       abs(df['low'] - df['close'].shift())], axis=0)
    
    df['DMplus'] = np.where((df['high'] - df['high'].shift()) > (df['low'].shift() - df['low']),
                            np.max([df['high'] - df['high'].shift(), np.zeros(len(df.index))], axis=0),
                            np.zeros(len(df.index)))
    
    df['DMminus'] = np.where((df['low'].shift() - df['low']) > (df['high'] - df['high'].shift()),
                             np.max([df['low'].shift() - df['low'], np.zeros(len(df.index))], axis=0),
                             np.zeros(len(df.index)))
    
    ATR = df['TR'].rolling(window=n, center=False).mean()
    df['DIplus'] = 100 * (df['DMplus'].rolling(window=n, center=False).mean() / ATR)
    df['DIminus'] = 100 * (df['DMminus'].rolling(window=n, center=False).mean() / ATR)
    df['ADX'] = 100 * (abs(df['DIplus'] - df['DIminus']) / (df['DIplus'] + df['DIminus'])).rolling(window=n, center=False).mean()
    
    return df['ADX']

#일목균형표(데이터, 전환선, 기준선, 선행스팬)
def ichimoku_cloud(df, tenkan_period=9, kijun_period=26, senkou_span_period=52):
    
    high_prices = df['high'].values
    low_prices = df['low'].values
    close_prices = df['close'].values
    
    conversion_line = (np.max(high_prices[-tenkan_period:]) + np.min(low_prices[-tenkan_period:])) / 2
    base_line = (np.max(high_prices[-kijun_period:]) + np.min(low_prices[-kijun_period:])) / 2
    
    leading_span_A = (conversion_line + base_line) / 2
    leading_span_B = (np.max(high_prices[-senkou_span_period:]) + np.min(low_prices[-senkou_span_period:])) / 2
    
    cloud_color = np.where(leading_span_A > leading_span_B, 'green', 'red')
    return pd.DataFrame({'ConversionLine': conversion_line,
                        'BaseLine': base_line,
                        'LeadingSpanA': leading_span_A,
                        'LeadingSpanB': leading_span_B,
                        'CloudColor': cloud_color}, index=[df.index[-1]])

#지지/저항선(데이터, 기간)
def support_resistance(df, n=30):
    df = df.copy()
    df['sup'] = df['low'].rolling(window=n, center=False).min()
    df['res'] = df['high'].rolling(window=n, center=False).max()
    return pd.DataFrame({'support': df['sup'].iloc[-1], 'resistance': df['res'].iloc[-1]}, index=[df.index[-1]])

#선형회귀(데이터, 기간)
def linreg(df, period):
    x = np.arange(period)
    y = df['close'].tail(period).values
    slope, intercept = np.polyfit(x, y, deg=1)
    return slope
