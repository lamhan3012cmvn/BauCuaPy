import random


# hàm này k cân thiết cho ds ra global lun vì mình sử dụng thường xuyên gọi hàm tôn stack
def chuyenSoThanhHinh(n):
    ds = ["cua", "bau", "tom", "ca", "ga", "nai"]
    return ds[n]


def lac():
    kq = []
    for i in range(0, 3):
        n = random.randrange(6)
        kq.append(chuyenSoThanhHinh(n))
    return kq


def tinhDiem(datCuoc, kq):
    tongDiem = 0
    hoanTien = 0
    for hinhDaLuaChon, diem in datCuoc.items():
        for hinh, soluong in kq.items():
            if (hinh == hinhDaLuaChon):
                hoanTien += diem
                tongDiem += soluong * diem
    return tongDiem + hoanTien


def dem(kq):
    kqm = {}
    for i in kq:
        kqm[i] = kq.count(i)
    return kqm


def nhapLuaChon(diemTong):
    datCuoc = {}
    dem = 3
    while(dem > 0):
        xacnhan = input("Bạn có muốn đặt cược tiếp không (y/n) ")
        if (xacnhan.lower() == "y"):
            # check input ở đây nữa nhập sai nhập lại tốt nhát cho người ta vd mẫu
            hinh = (input("Nhập con bạn muốn: ")).lower()
            # check chỗ này vì nhập số cược lơn hơn Điểm mình đang có
            diem = int(input("Số điểm bạn cược: "))
            datCuoc[hinh] = diem
            diemTong = diemTong - diem
            dem = dem - 1
        else:  # nếu k xử lý gì thì chú xóa dòng này vì nó k thiết break thẳng lun
            break
    return datCuoc, diemTong


def chayChuongTrinh():
    diemTong = 1000
    print("*Điểm ban đầu : %d *" % (diemTong))
    while(True):
        if(diemTong > 0):
            print("------Game Bầu Cua------")
            print("1. Chơi          2. Đóng")
            chon = input("=>: ")
            if (chon == "1"):
                datCuoc = {}
                ketQua = lac()
                ketQuaSauKhiDem = dem(ketQua)
                # đặt rồi mời chạy code lắc
                datCuoc, diemTong = nhapLuaChon(diemTong)
                print("dc = ", datCuoc)
                if(len(datCuoc) == 0):
                    diemAn = 0
                else:
                    diemAn = tinhDiem(datCuoc, ketQuaSauKhiDem)
                print("an = ", diemAn)
                print("kết quả lần lắc này: ", ketQua)
                diemTong = diemTong + diemAn
                print("*Điểm còn: %d *" % diemTong)
            else:
                break
        else:
            break
    print("Game Over!")


chayChuongTrinh()
