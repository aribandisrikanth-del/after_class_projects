class dog:
    location_from="german"
    def __init__(self,breed,family):
        self.breed=breed
        self.family=family
roar=dog("shepard","greens")
raf_raf=dog("labradour","franks")
print("roar","is a",roar.location_from,roar.breed,"form the",roar.family,"family")
print("raf_raf","is a",raf_raf.location_from,raf_raf.breed,"form the",raf_raf.family,"family")