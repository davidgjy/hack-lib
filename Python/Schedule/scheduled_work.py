import time
from datetime import datetime, timedelta


def scanCoupons():
    print('scan coupons...')

def main():
    count = 0
    while (True):
        time.sleep(20)
        now = datetime.now()
        if now.hour == 22 and now.minute == 35 and count == 0:
            scanCoupons()
            count = count + 1

main()