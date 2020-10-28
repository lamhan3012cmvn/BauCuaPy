import random
ds = ["cua","bau","tom","ca","ga","nai"]
lichSu = {}

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

def luuLichSu(n, ketQua, datCuoc):
    lichSu[str(n)] = ketQua, datCuoc

def xuatLichSu():
    for lan, [ketQua, datCuoc] in lichSu.items():
        print("Lần %s = %s | Bạn đặt = %s"%(lan, ketQua, datCuoc))

def chayChuongTrinh():
    diemTong= 1000
    print("*Điểm ban đầu : %d *" %(diemTong))
    lanLac = 1
    while(True):
        if(diemTong > 1):
            print("------Game Bầu Cua------")
            print("1.Chơi\n2.Lịch Sử\n0. Đóng ")
            chon = input("=>: ")
            if (chon == "1"):
                datCuoc = {}
                ketQua = lac()
                ketQuaSauKhiDem = dem(ketQua)
                datCuoc, diemHienTai = nhapLuaChon(diemTong)
                if(len(datCuoc) == 0):
                    diem = 0
                else:
                    diem = tinhDiem(datCuoc, ketQuaSauKhiDem)
                #
                print("Số điểm trả lại: ", diem)
                print("Kết quả lần lắc này: ",ketQua)
                diemTong = diemHienTai + diem
                print("*Điểm còn: %d *" %diemTong)
                #
                luuLichSu(lanLac, ketQua, datCuoc)
                lanLac += 1
            if(chon == "0"):
                break
            if(chon == "2"):
                xuatLichSu()
        else:
            break
    print("Game Over!")

chayChuongTrinh()


                
                



