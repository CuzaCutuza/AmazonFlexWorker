import json, time

class Log:
    
    @staticmethod 
    def info(message: str):
        print(f'\nINFO: {message}', flush=True)

    @staticmethod
    def error(message: str):
        print(f'ERROR: {message}', flush=True)
    
    @staticmethod
    def offer(jsonObj: str):
        offers = jsonObj.json().get('offerList')
        for offer in offers:
            # extract info
            rateInfo = offer.get('rateInfo')
            priceAmount = rateInfo.get('priceAmount')
            projectedTips = rateInfo.get('projectedTips')
            offerDate = time.strftime('%a %b %-d', time.localtime(offer.get('startTime')))
            offerStartTime = time.strftime('%-I:%M %p', time.localtime(offer.get('startTime')))
            offerEndTime = time.strftime('%-I:%M %p', time.localtime(offer.get('endTime')))
            offerTotalHour = ((offer.get('endTime') - offer.get('startTime')) / 3600)
            totalOfferCost = priceAmount + projectedTips
            print(f'\n--------------------\n{offerDate}\n{offerStartTime} - {offerEndTime} ({offerTotalHour}hrs) \n${priceAmount} + {projectedTips} = ${totalOfferCost}', flush=True)
