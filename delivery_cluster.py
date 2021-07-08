# -*- coding: utf-8 -*-
import random
  
'''
Kurgu aşağıdaki şekilde gerçekleşmektedir.
- distributionGeocode: Kuryelerin çıkış noktasını temsil etmektedir.
- generateDeliveryPoint ile istenilen miktarda teslimat noktası oluşturulur.
- ....... ile dağıtım noktasına en yakın ilk teslim noktası tespit edilir.
- tespit edilen teslim noktasının 1km çapı hesaplanarak hesaplanan alan içerisindeki diğer teslim noktalarıda kuryeye atanmak üzere ayrılır.
- Kuryeye teslim edilen teslim noktaları generateDeliveryPoint ile oluşturulan teslimat noktalarından silinir.
- Bu kurgu oluşturulan teslimat noktaları bitene kadar devam eder.
'''
  
# Sipariş
class Orders():
  # Her sipariş oluşturulduğunda rastgele bir ürün oluşur.
  dummpy_products = ["Hamburger", "Cheeseburger", "Köfte Ekmek", "Lahmacun", "Adana Kebap", "Çiğköfte", "Sucuk Ekmek", "Kokoreç", "Pide"]
  def __init__(self):
      self.product = self.dummpy_products[random.randint(0, 8)]

# Teslimat Noktası
class DeliveryPoint():
  def __init__(self,lat, lng):
      self.lat = lat
      self.lng = lng
      self.orders =  Orders()

  

class DeliveryCluster(): 
  # Params
  # distribution_geocode : Object{lat:float, lng:float}
  # deliveryPointCount : int: Default:1000
  def __init__(self, distributionGeocode, deliveryPointCount = 10):
    
      # Kuryelerin dağıtım merkezinin koordinatı.  Bu koordinat merkeze alınarak teslimat noktaları 1KM çapına göre kümelenerek dağıtılacaktır.
      self.distributionGeocode = distributionGeocode
      self.deliveryPointCount = deliveryPointCount
      self.deliveryPoints = self.generateDeliveryPoint(deliveryPointCount)
      

  # Random teslimat noktasi oluşturur.
  def generateDeliveryPoint(self, deliveryPointCount):
    deliveryPoints = []
    
    # Tekirdağ-Çorlu ilçe sınırları google.
    # Bu bilgi, sınırlar içerisinde rastgele geocode oluşturulması için kullanılmaktadır.
    max_lat = 41.211552
    min_lat = 41.125490
    max_lng = 27.818213
    min_lng = 27.752073
    
    
    for i in range(0, deliveryPointCount):
      deliveryLat = random.uniform(min_lat, max_lat)
      deliveryLng = random.uniform(min_lng, max_lng)
      deliveryPoints.append(DeliveryPoint(deliveryLat, deliveryLng))
      # if len(deliveryPoints) == 0:
      #   deliveryPoints.append(DeliveryPoint(deliveryLat, deliveryLng))
      # else:
      #   pass
      # Todo random teslimat noktaları oluşturulurken 1km çap içinde olanlar küme
        
    return deliveryPoints


distributionGeo = {'lat': 41.157733, 'lng': 27.805881}

c = DeliveryCluster(distributionGeo, 5)
for deliveryPoint in c.deliveryPoints:
  print(deliveryPoint.lat, deliveryPoint.lng)
#print(c.deliveryPoints[0]['orders'].product)




