from django.db import models

# Create your models here.
class FuturesInstrument(models.Model):
    CURRENCIES = [
        ('USD', 'Dollar'),
        ('EUR', 'EURO'),
        ('HKD', 'Hongkong Dollar'),
    ]

    EXCHANGES = [
        ('CME', 'CME'),
        ('NYMEX', 'NYMEX'),
        ('CBOT', 'CBOT'),
        ('EUREX', 'EUREX'),
        ('HKEX', 'HKEX'),
        ('SGX', 'SGX'),
        ('ICE_US', 'ICE_US'),
        ('LIFFE', 'LIFFE'),
        ('SHFE', 'SHFE'),
        ('MGEX', 'MGEX'),
        ('MX','MX'),
        ('CBOE','CBOE')
    ]

    MARKETS = [
        ('CUR', '통화'),
        ('IDX', '지수'),
        ('INT', '금리'),
        ('ENG', '에너지'),
        ('MTL', '금속'),
        ('Grain', '곡물'),
        ('Tropical', '열대과일'),
        ('Meat', '육류')
    ]

    name = models.CharField("상품명", max_length=64) #상품명
    symbol = models.CharField("상품코드", max_length=16) #상품코드
    currency = models.CharField("거래 통화", max_length=16, choices=CURRENCIES, default='USD') #통화
    exchange = models.CharField("거래소", max_length=16, choices=EXCHANGES) #거래소
    market = models.CharField("시장 구분", max_length=16, choices=MARKETS) #시장구분
    tickunit = models.DecimalField("호가 단위", max_digits=14, decimal_places=8) #틱 단위
    tickprice = models.DecimalField("호가당 가격", max_digits=7, decimal_places=4) #틱당 가격
    margin = models.DecimalField("증거금", max_digits=5, decimal_places=0) #증거금
    depth = models.IntegerField("주거래월물", default=1)
    decimal_places = models.SmallIntegerField("소수점 자리수") #소수점 자리수
    opentime = models.TimeField("거래 시작시간") #장 시작시간(한국)
    closetime = models.TimeField("거래 종료시간") #장 종료시간(한국)
    has_history = models.BooleanField("과거데이터 유무")
    is_tradable = models.BooleanField("거래가능여부")
    description = models.TextField("비고", null=True, blank=True)
    

    def __str__(self):
        return f"{self.name} ({self.symbol})"