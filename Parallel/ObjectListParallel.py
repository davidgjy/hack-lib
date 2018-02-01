import threading
from time import ctime,sleep

class UserVehicle:  
    id = 0  
    mobile = '00000000000'
    licenseNo = 'FFFFFFF'
  
    def __init__(self, pId, pMobile, pLicenseNo):  
        self.id = pId  
        self.mobile = pMobile
        self.licenseNo = pLicenseNo

class VehicleThread (threading.Thread):
    def __init__(self, uvList):
        threading.Thread.__init__(self)
        self.partList = uvList
    
    def run(self):
        displayItem(self.partList)

def displayItem(uvList):
    for uv in uvList:
        sleep(0.25)
        print("Id: %s" % uv.id)
        print("Mobile: %s" % uv.mobile)
        print("License No: %s" % uv.licenseNo)
        print("---------------------------------------------------")    

def displayParallel(uvList, threadNum):
    if len(uvList) % threadNum == 0:
        avgNum = len(uvList) // threadNum
    else:
        avgNum = len(uvList) // threadNum + 1
    lowerNum = 0
    upperNum = avgNum
    for i in range(1, threadNum + 1):
        partList = []
        for j in range(lowerNum, upperNum):
            partList.append(uvList[j])
        
        lowerNum = lowerNum + avgNum
        upperNum = upperNum + avgNum
        if upperNum > len(uvList):
            upperNum = len(uvList)
         
        thread = VehicleThread(partList) 
        thread.start()
    
        
def main():
    startMobile = 13800000000
    startLicenseNo = 10000
    uvList = []
    for i in range(1, 100):
        strMobile = str(startMobile + i)
        strLicenseNo = "沪A" + str(startLicenseNo) + str(i)
        userVehicle = UserVehicle(i, strMobile, strLicenseNo)
        uvList.append(userVehicle)
        
    displayParallel(uvList, 10)
    
if __name__=='__main__':
    main()   
    
        
        
       