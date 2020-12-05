from django.db import models

# Create your models here.

class Visitor(models.Model):
    phone = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=15)
    temperature = models.FloatField()

class Manager(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    password = models.CharField(max_length=15)

class Club(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    president = models.CharField(max_length=10)
    markImage = models.ImageField()
    members = models.IntegerField()
    info = models.TextField()

class Lab(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    members = models.IntegerField()
    info = models.TextField()

class Point(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True)
    floor = models.IntegerField()
    locationX = models.FloatField()
    locationY = models.FloatField()
    locationZ = models.FloatField()
    connectPoints = models.TextField(blank=True)
    connectMarkets = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.id) + self.name

    # 연결된 포인트들을 보여준다.
    def showConnectedPoints(self):     
        for point in self.connectPoints:
            print(point)

    # 연결된 상점들을 보여준다.
    def showConnectMarkets(self):
        for market in self.connectMarkets:
            print(market)

    # 포인트 한개를 연결한다.
    def addConnectPoint(self, point):
        self.connectPoints.append(point)

    # 포인트 리스트를 연결한다.
    def addConnectPoints(self, points):
        self.connectPoints.extend(points)

    # 상점을 연결한다.
    def addConnectMarket(self, market):
        self.connectMarkets.append(market)

    # getter    
    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getConnectedPoints(self):
        return self.connectPoints

    def getConnectedMarkets(self):
        return self.connectMarkets;
    
    
# 상점과 포인트를 연결한다.
def connectMarketAndPoint(market, *points):
    market.addConnectPoints(points)
    for point in points:
        point.addConnectMarket(market)

# 포인트들을 연결한다.
def connectPoints(point, *points):
    for i in points:
        point.addConnectPoint(i)
        i.addConnectPoint(point)


