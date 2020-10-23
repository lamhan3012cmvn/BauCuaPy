import random
ds = ["cua","bau","tom","ca","ga","nai"]

def lac():
    kq = []
    for i in range(0,3):
        n = random.randrange(6)
        kq.append(ds[n])
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

def kiemTraHinh(hinh):
    while(True):
        if hinh not in ds:
            hinh = (input("Nhập lại con bạn muốn(vd: cua, tom, ca,..): ")).lower()
        else:
            break
    return hinh

def nhapLuaChon(diemTong):
    diemHienTai = diemTong
    datCuoc ={}
    dem = 3
    while(dem>0):
        xacnhan = input("Bạn có muốn đặt cược tiếp không (y/n) ")
        if (xacnhan.lower() == "y"):         
            hinh = (input("Nhập con bạn muốn(vd: cua, tom, ca,..): ")).lower()
            hinh = kiemTraHinh(hinh)
            diem = int(input("Số điểm bạn cược(vd: 100,200,..): "))
            diemConLai = diemHienTai - diem
            if(diemConLai > 0):
                datCuoc[hinh] = diem
                diemHienTai = diemConLai
                dem = dem - 1
            else:
                print("Bạn không đủ điểm để chơi tiếp! \nChúng tôi đã lưu kết quả cược của bạn!")
                break
        else:
            break
    return datCuoc, diemHienTai

def chayChuongTrinh():
    diemTong= 1000
    print("*Điểm ban đầu : %d *" %(diemTong))
    while(True):
        if(diemTong > 1):
            print("------Game Bầu Cua------")
            print("1. Chơi          2. Đóng")
            chon = input("=>: ")
            if (chon == "1"):
                datCuoc = {}
                ketQua = lac()
                ketQuaSauKhiDem = dem(ketQua)
                datCuoc, diemHienTai = nhapLuaChon(diemTong)
                #print("dc = ",datCuoc)
                if(len(datCuoc) == 0):
                    diem = 0
                else:
                    diem = tinhDiem(datCuoc, ketQuaSauKhiDem)
                print("Số điểm trả lại: ", diem)
                print("kết quả lần lắc này: ",ketQua)
                diemTong = diemHienTai + diem
                print("*Điểm còn: %d *" %diemTong)
            else:
                break
        else:
            break
    print("Game Over!")

chayChuongTrinh()


                
                



