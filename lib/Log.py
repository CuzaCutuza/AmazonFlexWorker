import json, time

class Log:
    
    @staticmethod 
    def info(message: str):
        print(f'\nINFO: {message}', flush=True)

    @staticmethod
    def error(message: str):
        print(f'ERROR: {message}', flush=True)

    @staticmethod
    def offer(jsonObj: str, wareHouses ):
        offers = jsonObj.json().get('offerList')
        for offer in offers:
            # extract info
            rateInfo = offer.get('rateInfo')
            priceAmount = rateInfo.get('priceAmount')
            projectedTips = rateInfo.get('projectedTips')
            offerDate = time.strftime('%a %b %#d', time.localtime(offer.get('startTime')))
            offerStartTime = time.strftime('%#I:%M %p', time.localtime(offer.get('startTime')))
            offerEndTime = time.strftime('%#I:%M %p', time.localtime(offer.get('endTime')))
            offerTotalHour = ((offer.get('endTime') - offer.get('startTime')) / 3600)
            totalOfferCost = priceAmount + projectedTips
            serviceAreaName = "N/A"
            try:
                serviceAreaId = offer.get('serviceAreaId')
                serviceAreaName = wareHouses[serviceAreaId]
            except KeyError:
                print("serviceAreaId not in wareHouses dict")

            msg = "\n--------------------\n"+str(offerDate)+"\n"+str(serviceAreaName)+"\n"+str(offerStartTime)+ " - "+ str(offerEndTime)+ " "+ str(offerTotalHour)+"hrs\n"+str(priceAmount)+" + " +str(projectedTips)+" = "+str(totalOfferCost)
            return msg
