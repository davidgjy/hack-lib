class UserVehicle:  
    id = 0  
    mobile = '00000000000'
    licenseNo = 'FFFFFFF'
  
    def __init__(self, pId, pMobile, pLicenseNo):  
        self.id = pId  
        self.mobile = pMobile
        self.licenseNo = pLicenseNo

def display(uvList):
    for uv in uvList:
        print("Id: %s" % uv.id)
        print("Mobile: %s" % uv.mobile)
        print("License No: %s" % uv.licenseNo)
        print("---------------------------------------------------")
        
def main():
    startMobile = 13800000000
    startLicenseNo = 10000
    uvList = []
    for i in range(1, 100):
        strMobile = str(startMobile + i)
        strLicenseNo = "沪A" + str(startLicenseNo) + str(i)
        userVehicle = UserVehicle(i, strMobile, strLicenseNo)
        uvList.append(userVehicle)
        
    display(uvList)
    
if __name__=='__main__':
    main()   
    
        
        
       