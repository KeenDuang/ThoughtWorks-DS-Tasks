# 停车场
class ParkingLot:

    def __init__(self, seq, total, used):
        self.seq = seq  # 停车场序列号
        self.total = total  # 停车场总车位数
        self.used = used  # 停车场已使用车位数

    def park_car(self, user):
        if self.used < self.total:
            ticket = str(self.seq) + '_' + user  # 生成停车票编码
            self.used += 1  # 停车场已使用车位数递增
            print('停车成功，生成车票,车票编码为：'+ticket)
            return ticket
        else:
            print('车位已满，停车失败，请前往其他停车场')

    def take_car(self, user, ticket):
        if ticket == str(self.seq) + '_' + user:  # 验证停车票是否有效
            self.used -= 1
            print('取车成功')
        else:
            print('车票无效，停车失败，请校验车票')


# 停车小弟
class ParkingBoy:

    def __init__(self, num):
        self.num = num  # 停车小弟编号

    def park_car(self, user):
        names = globals()
        for i in range(0, n):  # 假定有n个停车场，其编号从0到n-1依次递增
            if i == n - 1 and names['ParkingLot' + str(i)].used == names['ParkingLot' + str(i)].total:
                print('所有停车场车位均满，停车失败')
            if names['ParkingLot' + str(i)].used < names['ParkingLot' + str(i)].total:
                ticket = names['ParkingLot' + str(i)].park_car(user)
                return ticket
                break


# 聪明的停车小弟
class SmartParkingBoy:

    def __init__(self, num):
        self.num = num  # 聪明的停车小弟编号

    def park_car(self, user):
        names = globals()
        idx = -1
        count = 0
        for i in range(0, n):  # 假定有n个停车场，其编号从0到n-1依次递增
            if names['ParkingLot' + str(i)].total - names['ParkingLot' + str(i)].used > count:
                count = names['ParkingLot' + str(i)].total - names['ParkingLot' + str(i)].used
                idx = i
        if idx == -1:
            print('所有停车场车位均满，停车失败')
        else:
            ticket = names['ParkingLot' + str(idx)].park_car(user)
            return ticket


# 超级停车小弟
class SuperParkingBoy:

    def __init__(self, num):
        self.num = num  # 超级停车小弟编号

    def park_car(self, user):
        names = globals()
        idx = -1
        count = 0
        for i in range(0, n):  # 假定有n个停车场，其编号从0到n-1依次递增
            rate = (names['ParkingLot' + str(i)].total - names['ParkingLot' + str(i)].used) / names[
                'ParkingLot' + str(i)].total
            if rate > count:
                count = rate
                idx = i
        if idx == -1:
            print('所有停车场车位均满，停车失败')
        else:
            ticket = names['ParkingLot' + str(idx)].park_car(user)
            return ticket


# 停车场经理
class ParkingManager:

    def __init__(self, num='PM1'):  # 停车场经理编号
        self.num = num

    def park_car(self, user):  # 停车场经理的停车策略按照超级停车小弟策略执行
        names = globals()
        idx = -1
        count = 0
        for i in range(0, n):  # 假定有n个停车场，其编号从0到n-1依次递增
            rate = (names['ParkingLot' + str(i)].total - names['ParkingLot' + str(i)].used) / names[
                'ParkingLot' + str(i)].total
            if rate > count:
                count = rate
                idx = i
        if idx == -1:
            print('所有停车场车位均满，停车失败')
        else:
            ticket = names['ParkingLot' + str(idx)].park_car(user)
            return ticket

    def assign_park_car(self, num, user):  # 停车场经理将客户的车分配给停车小弟去停放
        if num in ParkingBoyList:
            ticket = ParkingBoy(num).park_car(user)
        elif num in SmartParkingBoyList:
            ticket = SmartParkingBoy(num).park_car(user)
        elif num in SuperParkingBoyList:
            ticket = SuperParkingBoy(num).park_car(user)
        else:
            print('停车小弟编号无效，请重新分配')
        return ticket


# 测试
if __name__ == '__main__':
    n = 10                     # 共10个停车场，其编号从0-9递增
    ParkingBoyList = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8']
    SmartParkingBoyList = ['SP1', 'SP2', 'SP3', 'SP4']
    SuperParkingBoyList = ['SSP1', 'SSP2']
    ParkingLot0 = ParkingLot(0, 100, 100)
    ParkingLot1 = ParkingLot(1, 100, 85)
    ParkingLot2 = ParkingLot(2, 100, 73)
    ParkingLot3 = ParkingLot(3, 100, 92)
    ParkingLot4 = ParkingLot(4, 100, 55)
    ParkingLot5 = ParkingLot(5, 80, 48)
    ParkingLot6 = ParkingLot(6, 80, 72)
    ParkingLot7 = ParkingLot(7, 80, 38)
    ParkingLot8 = ParkingLot(8, 60, 25)
    ParkingLot9 = ParkingLot(9, 60, 41)
    PM = ParkingManager()

    PM.assign_park_car('SP1', 'Marry')
    PM.assign_park_car('SSP2', 'Li')
    PM.assign_park_car('P7', 'Ken')
    PM.park_car('Trump')
