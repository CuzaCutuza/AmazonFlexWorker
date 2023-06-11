from datetime import datetime

from lib.Log import Log


class Offer:

    def __init__(self, offerResponseObject: object) -> None:
        self.id = offerResponseObject.get("offerId")
        self.expirationDate = datetime.fromtimestamp(offerResponseObject.get("expirationDate"))
        self.location = offerResponseObject.get('serviceAreaId')
        self.blockRate = float(offerResponseObject.get('rateInfo').get('priceAmount'))
        self.tipRate = float(offerResponseObject.get('rateInfo').get('projectedTips'))
        self.endTime = datetime.fromtimestamp(offerResponseObject.get('endTime'))
        self.hidden = offerResponseObject.get("hidden")
        self.ratePerHour = self.blockRate / ((self.endTime - self.expirationDate).seconds / 3600)
        self.weekday = self.expirationDate.weekday()


    def toString(self) -> str:
        blockDuration = (self.endTime - self.expirationDate).seconds / 3600

        # translate Service ID to Service Area Name

        body = 'Location: ' + self.location + '\n'
        body += 'Date: ' + str(datetime.fromtimestamp(self.expirationDate).strftime("%m-%d %I:%M:%S %p")) +'\n'
        body += 'Pay: ' + str(self.blockRate) + '\n'
        body += 'Pay rate per hour: ' + str(self.ratePerHour) + '\n'
        body += 'Block Duration: ' + str(blockDuration) + f'{"hour" if blockDuration == 1 else "hours"}\n'

        return body
