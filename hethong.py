import mysql.connector

# tạo đối tượng connection
myconn = mysql.connector.connect(host="localhost", user="root",
                                 password="", database="httt")

# tạo đối tượng cursor
cur = myconn.cursor()
# # bth dùng if else
# #if (nhietdo==x[0][0] && x[0][0]= khoong lajnh) >>
# elif ( )


def so_sanh(so1, so2):
    if so1 == so2:
        return 1
    return 0

# nhập dữ liệu

def ketLuan(S,id_loi):
    id=int(id_loi)
    queryRS = ("SELECT loi, giaiphap FROM loivakhacphuc"" WHERE ID=%s")
    cur.execute(queryRS, (id,))
    kq = cur.fetchall()
    loi = str(kq[0][0])
    giaiphap = str(kq[0][1])
    if S>=0.9:
        print("BOT : BOT xin được trả lời là điều hòa của bạn bị lỗi về " +
          loi + " và giải pháp để khắc phục " + loi + " là: \n" + giaiphap)
    elif S>=0.8 and S<0.9:
        print("BOT : BOT xin được trả lời là điều hòa của bạn  khả năng cao bị lỗi về " +
          loi + " và giải pháp để khắc phục " + loi + " là: \n" + giaiphap)  
    elif S>=0.5 and S<=0.8:
        print("BOT : BOT xin được trả lời là điều hòa của bạn có thể bị lỗi về " +
          loi + " và giải pháp để khắc phục " + loi + " là: \n" + giaiphap)
    elif S>0 and S<0.5:
        print("BOT : BOT xin được trả lời là điều hòa của bạn cần được theo dõi thêm để biết rõ về lỗi")
    else:
        print("BOT : BOT không thể kết luận được lỗi về điều hòa của bạn")
def khongCo(nhietdo,quatgio,dongho,maynenam,mui,maynen,luoiloc,tuyet,dongdien,
                       trangthai,maychay,dieukhien,nuoc,den,dieuhoanguondien):
    query = ("SELECT nhietdomaylanh ,quatgioocucnong ,donghododien ,cotiengphatratumaynen ,comuimaylanh ,trangthaimaynen ,bieuhienluoiloc ,coxuathientuyet ,hoatdongdongdien ,trangthaimaylanhkhibat ,maychayvangunglientuc ,manhinhdieukhien ,nuoctrongongdan ,denbaoloi ,trangthaidieuhoakhiconguondien, IDloi  FROM caseloi")
    cur.execute(query)
    myrs = cur.fetchall()
    query2 = ("SELECT COUNT(*) FROM caseloi")
    cur.execute(query2)
    rows = cur.fetchall()
    leng_rows = int(rows[0][0])
    print(type(leng_rows))
    # mangIDloi=myrs[15]
    a = []
    #  sau khi tisnh xong S
    Max=0;
    IDloi=0;
    for i in range(leng_rows):
            
            if myrs[i][15]==1:
                sum=0;
                cnt=[]
                bangtinh = [7, 1, 1, 3, 6, 6, 7, 1, 1, 3, 2, 1, 1, 1, 1]
                sum_array=0
                for k in range(15):
                    sum_array+=bangtinh[k]
                x1=so_sanh(nhietdo,myrs[i][0])
                if x1==1:
                    x1=1
                else: x1=0.1
                x2=so_sanh(quatgio,myrs[i][1])
                if x2==1:
                    x2=1
                else : x2=0
                x3=so_sanh(dongho,myrs[i][2])
                if x3==1:
                    x3=1
                else : x3=0
                x4=so_sanh(maynenam,myrs[i][3])
                if x4==1:
                    x4=1
                else : x4=0.2
                x5=so_sanh(mui,myrs[i][4])
                if x5==1:
                    x5=1
                else : x5=0.3
                x6=so_sanh(maynen,myrs[i][5])
                if x6==1:
                    x6=1
                else : x6=0
                x7=so_sanh(luoiloc,myrs[i][6])
                if x7==1:
                    x7=1
                else : x7=0.5
                x8=so_sanh(tuyet,myrs[i][7])
                if x8==1:
                    x8=1
                else : x8=0.4
                x9=so_sanh(dongdien,myrs[i][8])
                if x9==1:
                    x9=1
                else : x9=0.6
                x10=so_sanh(trangthai,myrs[i][9])
                if x10==1:
                    x10=1
                else : x10=0.2
                x11=so_sanh(maychay,myrs[i][10])
                if x11==1:
                    x11=1
                else : x11=0.1
                x12=so_sanh(dieukhien,myrs[i][11])
                if x12==1:
                    x12=1
                else : x12=0
                x13=so_sanh(nuoc,myrs[i][12])
                if x13==1:
                    x13=1
                else : x13=0.1
                x14=so_sanh(den,myrs[i][13])
                if x14==1:
                    x14=1
                else : x14=0
                x15=so_sanh(dieuhoanguondien,myrs[i][14])
                if x15==1:
                    x15=1
                else : x15=0
                sum=(x1*bangtinh[0]+x2*bangtinh[1]+x3*bangtinh[2]+x4*bangtinh[3]+x5*bangtinh[4]+x6*bangtinh[5]+x7*bangtinh[6]+x8*bangtinh[7]+x9*bangtinh[8]+x10*bangtinh[9]+x11*bangtinh[10]+x12*bangtinh[11]+x13*bangtinh[12]+x14*bangtinh[13]+x15*bangtinh[14])/sum_array
                if sum>Max:
                    Max=sum
                    IDloi=myrs[i][15]
                    cnt=[Max,IDloi]
                    a.append(cnt)
            elif myrs[i][15]==2:
                sum=0;
                cnt=[]
                bangtinh2 = [7, 8, 6, 2, 1, 1, 2, 1, 2, 3, 1, 1, 1, 2, 1]
                sum_array=0
                for k in range(15):
                    sum_array+=bangtinh2[k]
                x1=so_sanh(nhietdo,myrs[i][0])
                if x1==1:
                    x1=1
                else: x1=0.1
                x2=so_sanh(quatgio,myrs[i][1])
                if x2==1:
                    x2=1
                else : x2=0
                x3=so_sanh(dongho,myrs[i][2])
                if x3==1:
                    x3=1
                else : x3=0
                x4=so_sanh(maynenam,myrs[i][3])
                if x4==1:
                    x4=1
                else : x4=0.2
                x5=so_sanh(mui,myrs[i][4])
                if x5==1:
                    x5=1
                else : x5=0.3
                x6=so_sanh(maynen,myrs[i][5])
                if x6==1:
                    x6=1
                else : x6=0
                x7=so_sanh(luoiloc,myrs[i][6])
                if x7==1:
                    x7=1
                else : x7=0.5
                x8=so_sanh(tuyet,myrs[i][7])
                if x8==1:
                    x8=1
                else : x8=0.4
                x9=so_sanh(dongdien,myrs[i][8])
                if x9==1:
                    x9=1
                else : x9=0.6
                x10=so_sanh(trangthai,myrs[i][9])
                if x10==1:
                    x10=1
                else : x10=0.2
                x11=so_sanh(maychay,myrs[i][10])
                if x11==1:
                    x11=1
                else : x11=0.1
                x12=so_sanh(dieukhien,myrs[i][11])
                if x12==1:
                    x12=1
                else : x12=0
                x13=so_sanh(nuoc,myrs[i][12])
                if x13==1:
                    x13=1
                else : x13=0.1
                x14=so_sanh(den,myrs[i][13])
                if x14==1:
                    x14=1
                else : x14=0
                x15=so_sanh(dieuhoanguondien,myrs[i][14])
                if x15==1:
                    x15=1
                else : x15=0
            
                sum=(x1*bangtinh2[0]+x2*bangtinh2[1]+x3*bangtinh2[2]+x4*bangtinh2[3]+x5*bangtinh2[4]+x6*bangtinh2[5]+x7*bangtinh2[6]+x8*bangtinh2[7]+x9*bangtinh2[8]+x10*bangtinh2[9]+x11*bangtinh2[10]+x12*bangtinh2[11]+x13*bangtinh2[12]+x14*bangtinh2[13]+x15*bangtinh2[14])/sum_array
                if sum>Max:
                    Max=sum
                    IDloi=myrs[i][15]
                    cnt=[Max,IDloi]
                    a.append(cnt)
                        
                
            elif myrs[i][15]==3:
                sum=0;
                cnt=[]
                bangtinh3 = [8, 1, 1, 8, 2, 4, 2, 2, 5, 1, 1, 1, 1, 1, 3]
                sum_array=0
                for k in range(15):
                    sum_array+=bangtinh3[k]
                x1=so_sanh(nhietdo,myrs[i][0])
                if x1==1:
                    x1=1
                else: x1=0.1
                x2=so_sanh(quatgio,myrs[i][1])
                if x2==1:
                    x2=1
                else : x2=0
                x3=so_sanh(dongho,myrs[i][2])
                if x3==1:
                    x3=1
                else : x3=0
                x4=so_sanh(maynenam,myrs[i][3])
                if x4==1:
                    x4=1
                else : x4=0.2
                x5=so_sanh(mui,myrs[i][4])
                if x5==1:
                    x5=1
                else : x5=0.3
                x6=so_sanh(maynen,myrs[i][5])
                if x6==1:
                    x6=1
                else : x6=0
                x7=so_sanh(luoiloc,myrs[i][6])
                if x7==1:
                    x7=1
                else : x7=0.5
                x8=so_sanh(tuyet,myrs[i][7])
                if x8==1:
                    x8=1
                else : x8=0.4
                x9=so_sanh(dongdien,myrs[i][8])
                if x9==1:
                    x9=1
                else : x9=0.6
                x10=so_sanh(trangthai,myrs[i][9])
                if x10==1:
                    x10=1
                else : x10=0.2
                x11=so_sanh(maychay,myrs[i][10])
                if x11==1:
                    x11=1
                else : x11=0.1
                x12=so_sanh(dieukhien,myrs[i][11])
                if x12==1:
                    x12=1
                else : x12=0
                x13=so_sanh(nuoc,myrs[i][12])
                if x13==1:
                    x13=1
                else : x13=0.1
                x14=so_sanh(den,myrs[i][13])
                if x14==1:
                    x14=1
                else : x14=0
                x15=so_sanh(dieuhoanguondien,myrs[i][14])
                if x15==1:
                    x15=1
                else : x15=0
            
                sum=(x1*bangtinh3[0]+x2*bangtinh3[1]+x3*bangtinh3[2]+x4*bangtinh3[3]+x5*bangtinh3[4]+x6*bangtinh3[5]+x7*bangtinh3[6]+x8*bangtinh3[7]+x9*bangtinh3[8]+x10*bangtinh3[9]+x11*bangtinh3[10]+x12*bangtinh3[11]+x13*bangtinh3[12]+x14*bangtinh3[13]+x15*bangtinh3[14])/sum_array
                if sum>Max:
                    Max=sum
                    IDloi=myrs[i][15]
                    cnt=[Max,IDloi]
                    a.append(cnt)
                
            elif myrs[i][15]==4:
                sum=0;
                cnt=[]
                bangtinh4 = [6, 2, 1, 3, 2, 1, 3, 3, 4, 2, 2, 1, 2, 2, 1]
                sum_array=0
                for k in range(15):
                    sum_array+=bangtinh4[k]
                x1=so_sanh(nhietdo,myrs[i][0])
                if x1==1:
                    x1=1
                else: x1=0.1
                x2=so_sanh(quatgio,myrs[i][1])
                if x2==1:
                    x2=1
                else : x2=0
                x3=so_sanh(dongho,myrs[i][2])
                if x3==1:
                    x3=1
                else : x3=0
                x4=so_sanh(maynenam,myrs[i][3])
                if x4==1:
                    x4=1
                else : x4=0.2
                x5=so_sanh(mui,myrs[i][4])
                if x5==1:
                    x5=1
                else : x5=0.3
                x6=so_sanh(maynen,myrs[i][5])
                if x6==1:
                    x6=1
                else : x6=0
                x7=so_sanh(luoiloc,myrs[i][6])
                if x7==1:
                    x7=1
                else : x7=0.5
                x8=so_sanh(tuyet,myrs[i][7])
                if x8==1:
                    x8=1
                else : x8=0.4
                x9=so_sanh(dongdien,myrs[i][8])
                if x9==1:
                    x9=1
                else : x9=0.6
                x10=so_sanh(trangthai,myrs[i][9])
                if x10==1:
                    x10=1
                else : x10=0.2
                x11=so_sanh(maychay,myrs[i][10])
                if x11==1:
                    x11=1
                else : x11=0.1
                x12=so_sanh(dieukhien,myrs[i][11])
                if x12==1:
                    x12=1
                else : x12=0
                x13=so_sanh(nuoc,myrs[i][12])
                if x13==1:
                    x13=1
                else : x13=0.1
                x14=so_sanh(den,myrs[i][13])
                if x14==1:
                    x14=1
                else : x14=0
                x15=so_sanh(dieuhoanguondien,myrs[i][14])
                if x15==1:
                    x15=1
                else : x15=0
            
                sum=(x1*bangtinh4[0]+x2*bangtinh4[1]+x3*bangtinh4[2]+x4*bangtinh4[3]+x5*bangtinh4[4]+x6*bangtinh4[5]+x7*bangtinh4[6]+x8*bangtinh4[7]+x9*bangtinh4[8]+x10*bangtinh4[9]+x11*bangtinh4[10]+x12*bangtinh4[11]+x13*bangtinh4[12]+x14*bangtinh4[13]+x15*bangtinh4[14])/sum_array
                if sum>Max:
                    Max=sum
                    IDloi=myrs[i][15]
                    cnt=[Max,IDloi]
                    a.append(cnt)
                
            elif myrs[i][15]==5:
                sum=0;
                cnt=[]
                bangtinh5 = [5, 8, 2, 4, 2, 7, 1, 2, 4, 4, 2, 2, 3, 2, 1]
                sum_array=0
                for k in range(15):
                    sum_array+=bangtinh5[k]
                x1=so_sanh(nhietdo,myrs[i][0])
                if x1==1:
                    x1=1
                else: x1=0.1
                x2=so_sanh(quatgio,myrs[i][1])
                if x2==1:
                    x2=1
                else : x2=0
                x3=so_sanh(dongho,myrs[i][2])
                if x3==1:
                    x3=1
                else : x3=0
                x4=so_sanh(maynenam,myrs[i][3])
                if x4==1:
                    x4=1
                else : x4=0.2
                x5=so_sanh(mui,myrs[i][4])
                if x5==1:
                    x5=1
                else : x5=0.3
                x6=so_sanh(maynen,myrs[i][5])
                if x6==1:
                    x6=1
                else : x6=0
                x7=so_sanh(luoiloc,myrs[i][6])
                if x7==1:
                    x7=1
                else : x7=0.5
                x8=so_sanh(tuyet,myrs[i][7])
                if x8==1:
                    x8=1
                else : x8=0.4
                x9=so_sanh(dongdien,myrs[i][8])
                if x9==1:
                    x9=1
                else : x9=0.6
                x10=so_sanh(trangthai,myrs[i][9])
                if x10==1:
                    x10=1
                else : x10=0.2
                x11=so_sanh(maychay,myrs[i][10])
                if x11==1:
                    x11=1
                else : x11=0.1
                x12=so_sanh(dieukhien,myrs[i][11])
                if x12==1:
                    x12=1
                else : x12=0
                x13=so_sanh(nuoc,myrs[i][12])
                if x13==1:
                    x13=1
                else : x13=0.1
                x14=so_sanh(den,myrs[i][13])
                if x14==1:
                    x14=1
                else : x14=0
                x15=so_sanh(dieuhoanguondien,myrs[i][14])
                if x15==1:
                    x15=1
                else : x15=0
                
                sum=(x1*bangtinh5[0]+x2*bangtinh5[1]+x3*bangtinh5[2]+x4*bangtinh5[3]+x5*bangtinh5[4]+x6*bangtinh5[5]+x7*bangtinh5[6]+x8*bangtinh5[7]+x9*bangtinh5[8]+x10*bangtinh5[9]+x11*bangtinh5[10]+x12*bangtinh5[11]+x13*bangtinh5[12]+x14*bangtinh5[13]+x15*bangtinh5[14])/sum_array
                if sum>Max:
                    Max=sum
                    IDloi=myrs[i][15]
                    cnt=[Max,IDloi]
                    a.append(cnt)
                
            elif myrs[i][15]==6:
                sum=0;
                cnt=[]
                bangtinh6 = [2, 1, 1, 1, 1, 2, 1, 7, 1, 1, 8, 1, 9, 1, 1]
                sum_array=0
                for k in range(15):
                    sum_array+=bangtinh6[k]
                x1=so_sanh(nhietdo,myrs[i][0])
                if x1==1:
                    x1=1
                else: x1=0.1
                x2=so_sanh(quatgio,myrs[i][1])
                if x2==1:
                    x2=1
                else : x2=0
                x3=so_sanh(dongho,myrs[i][2])
                if x3==1:
                    x3=1
                else : x3=0
                x4=so_sanh(maynenam,myrs[i][3])
                if x4==1:
                    x4=1
                else : x4=0.2
                x5=so_sanh(mui,myrs[i][4])
                if x5==1:
                    x5=1
                else : x5=0.3
                x6=so_sanh(maynen,myrs[i][5])
                if x6==1:
                    x6=1
                else : x6=0
                x7=so_sanh(luoiloc,myrs[i][6])
                if x7==1:
                    x7=1
                else : x7=0.5
                x8=so_sanh(tuyet,myrs[i][7])
                if x8==1:
                    x8=1
                else : x8=0.4
                x9=so_sanh(dongdien,myrs[i][8])
                if x9==1:
                    x9=1
                else : x9=0.6
                x10=so_sanh(trangthai,myrs[i][9])
                if x10==1:
                    x10=1
                else : x10=0.2
                x11=so_sanh(maychay,myrs[i][10])
                if x11==1:
                    x11=1
                else : x11=0.1
                x12=so_sanh(dieukhien,myrs[i][11])
                if x12==1:
                    x12=1
                else : x12=0
                x13=so_sanh(nuoc,myrs[i][12])
                if x13==1:
                    x13=1
                else : x13=0.1
                x14=so_sanh(den,myrs[i][13])
                if x14==1:
                    x14=1
                else : x14=0
                x15=so_sanh(dieuhoanguondien,myrs[i][14])
                if x15==1:
                    x15=1
                else : x15=0
                
                sum=(x1*bangtinh6[0]+x2*bangtinh6[1]+x3*bangtinh6[2]+x4*bangtinh6[3]+x5*bangtinh6[4]+x6*bangtinh6[5]+x7*bangtinh6[6]+x8*bangtinh6[7]+x9*bangtinh6[8]+x10*bangtinh6[9]+x11*bangtinh6[10]+x12*bangtinh6[11]+x13*bangtinh6[12]+x14*bangtinh6[13]+x15*bangtinh6[14])/sum_array
                if sum>Max:
                    Max=sum
                    IDloi=myrs[i][15]
                    cnt=[Max,IDloi]
                    a.append(cnt)
                
            elif myrs[i][15]==7:
                sum=0;
                cnt=[]
                bangtinh7 = [5, 1, 1, 1, 4, 1, 2, 7, 8, 2, 3, 1, 2, 9, 1]
                sum_array=0
                for k in range(15):
                    sum_array+=bangtinh7[k]
                x1=so_sanh(nhietdo,myrs[i][0])
                if x1==1:
                    x1=1
                else: x1=0.1
                x2=so_sanh(quatgio,myrs[i][1])
                if x2==1:
                    x2=1
                else : x2=0
                x3=so_sanh(dongho,myrs[i][2])
                if x3==1:
                    x3=1
                else : x3=0
                x4=so_sanh(maynenam,myrs[i][3])
                if x4==1:
                    x4=1
                else : x4=0.2
                x5=so_sanh(mui,myrs[i][4])
                if x5==1:
                    x5=1
                else : x5=0.3
                x6=so_sanh(maynen,myrs[i][5])
                if x6==1:
                    x6=1
                else : x6=0
                x7=so_sanh(luoiloc,myrs[i][6])
                if x7==1:
                    x7=1
                else : x7=0.5
                x8=so_sanh(tuyet,myrs[i][7])
                if x8==1:
                    x8=1
                else : x8=0.4
                x9=so_sanh(dongdien,myrs[i][8])
                if x9==1:
                    x9=1
                else : x9=0.6
                x10=so_sanh(trangthai,myrs[i][9])
                if x10==1:
                    x10=1
                else : x10=0.2
                x11=so_sanh(maychay,myrs[i][10])
                if x11==1:
                    x11=1
                else : x11=0.1
                x12=so_sanh(dieukhien,myrs[i][11])
                if x12==1:
                    x12=1
                else : x12=0
                x13=so_sanh(nuoc,myrs[i][12])
                if x13==1:
                    x13=1
                else : x13=0.1
                x14=so_sanh(den,myrs[i][13])
                if x14==1:
                    x14=1
                else : x14=0
                x15=so_sanh(dieuhoanguondien,myrs[i][14])
                if x15==1:
                    x15=1
                else : x15=0
                
                sum=(x1*bangtinh7[0]+x2*bangtinh7[1]+x3*bangtinh7[2]+x4*bangtinh7[3]+x5*bangtinh7[4]+x6*bangtinh7[5]+x7*bangtinh7[6]+x8*bangtinh7[7]+x9*bangtinh7[8]+x10*bangtinh7[9]+x11*bangtinh7[10]+x12*bangtinh7[11]+x13*bangtinh7[12]+x14*bangtinh7[13]+x15*bangtinh7[14])/sum_array
                if sum>Max:
                    Max=sum
                    IDloi=myrs[i][15]
                    cnt=[Max,IDloi]
                    a.append(cnt)
                
            elif myrs[i][15]==8:
                sum=0;
                cnt=[]
                bangtinh8 = [3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 1, 1, 1]
                sum_array=0
                for k in range(15):
                    sum_array+=bangtinh8[k]
                x1=so_sanh(nhietdo,myrs[i][0])
                if x1==1:
                    x1=1
                else: x1=0.1
                x2=so_sanh(quatgio,myrs[i][1])
                if x2==1:
                    x2=1
                else : x2=0
                x3=so_sanh(dongho,myrs[i][2])
                if x3==1:
                    x3=1
                else : x3=0
                x4=so_sanh(maynenam,myrs[i][3])
                if x4==1:
                    x4=1
                else : x4=0.2
                x5=so_sanh(mui,myrs[i][4])
                if x5==1:
                    x5=1
                else : x5=0.3
                x6=so_sanh(maynen,myrs[i][5])
                if x6==1:
                    x6=1
                else : x6=0
                x7=so_sanh(luoiloc,myrs[i][6])
                if x7==1:
                    x7=1
                else : x7=0.5
                x8=so_sanh(tuyet,myrs[i][7])
                if x8==1:
                    x8=1
                else : x8=0.4
                x9=so_sanh(dongdien,myrs[i][8])
                if x9==1:
                    x9=1
                else : x9=0.6
                x10=so_sanh(trangthai,myrs[i][9])
                if x10==1:
                    x10=1
                else : x10=0.2
                x11=so_sanh(maychay,myrs[i][10])
                if x11==1:
                    x11=1
                else : x11=0.1
                x12=so_sanh(dieukhien,myrs[i][11])
                if x12==1:
                    x12=1
                else : x12=0
                x13=so_sanh(nuoc,myrs[i][12])
                if x13==1:
                    x13=1
                else : x13=0.1
                x14=so_sanh(den,myrs[i][13])
                if x14==1:
                    x14=1
                else : x14=0
                x15=so_sanh(dieuhoanguondien,myrs[i][14])
                if x15==1:
                    x15=1
                else : x15=0
                
                sum=(x1*bangtinh8[0]+x2*bangtinh8[1]+x3*bangtinh8[2]+x4*bangtinh8[3]+x5*bangtinh8[4]+x6*bangtinh8[5]+x7*bangtinh8[6]+x8*bangtinh8[7]+x9*bangtinh8[8]+x10*bangtinh8[9]+x11*bangtinh8[10]+x12*bangtinh8[11]+x13*bangtinh8[12]+x14*bangtinh8[13]+x15*bangtinh8[14])/sum_array
                if sum>Max:
                    Max=sum
                    IDloi=myrs[i][15]
                    cnt=[Max,IDloi]
                    a.append(cnt)
            
            
            elif myrs[i][15]==9:
                sum=0;
                cnt=[]
                bangtinh9 = [9, 6, 6, 7, 5, 6, 4, 6, 4, 5, 2, 1, 6, 4, 10]
                sum_array=0
                for k in range(15):
                    sum_array+=bangtinh9[k]
                x1=so_sanh(nhietdo,myrs[i][0])
                if x1==1:
                    x1=1
                else: x1=0.1
                x2=so_sanh(quatgio,myrs[i][1])
                if x2==1:
                    x2=1
                else : x2=0
                x3=so_sanh(dongho,myrs[i][2])
                if x3==1:
                    x3=1
                else : x3=0
                x4=so_sanh(maynenam,myrs[i][3])
                if x4==1:
                    x4=1
                else : x4=0.2
                x5=so_sanh(mui,myrs[i][4])
                if x5==1:
                    x5=1
                else : x5=0.3
                x6=so_sanh(maynen,myrs[i][5])
                if x6==1:
                    x6=1
                else : x6=0
                x7=so_sanh(luoiloc,myrs[i][6])
                if x7==1:
                    x7=1
                else : x7=0.5
                x8=so_sanh(tuyet,myrs[i][7])
                if x8==1:
                    x8=1
                else : x8=0.4
                x9=so_sanh(dongdien,myrs[i][8])
                if x9==1:
                    x9=1
                else : x9=0.6
                x10=so_sanh(trangthai,myrs[i][9])
                if x10==1:
                    x10=1
                else : x10=0.2
                x11=so_sanh(maychay,myrs[i][10])
                if x11==1:
                    x11=1
                else : x11=0.1
                x12=so_sanh(dieukhien,myrs[i][11])
                if x12==1:
                    x12=1
                else : x12=0
                x13=so_sanh(nuoc,myrs[i][12])
                if x13==1:
                    x13=1
                else : x13=0.1
                x14=so_sanh(den,myrs[i][13])
                if x14==1:
                    x14=1
                else : x14=0
                x15=so_sanh(dieuhoanguondien,myrs[i][14])
                if x15==1:
                    x15=1
                else : x15=0
                
                sum=(x1*bangtinh9[0]+x2*bangtinh9[1]+x3*bangtinh9[2]+x4*bangtinh9[3]+x5*bangtinh9[4]+x6*bangtinh9[5]+x7*bangtinh9[6]+x8*bangtinh9[7]+x9*bangtinh9[8]+x10*bangtinh9[9]+x11*bangtinh9[10]+x12*bangtinh9[11]+x13*bangtinh9[12]+x14*bangtinh9[13]+x15*bangtinh9[14])/sum_array
                if sum>Max:
                    Max=sum
                    IDloi=myrs[i][15]
                    cnt=[Max,IDloi]
                    a.append(cnt)
                
            else:       
                sum=0;
                cnt=[]
                bangtinh10 = [4, 1, 2, 1, 3, 2, 4, 2, 4, 7, 8, 3, 1, 1, 1]
                sum_array=0
                for k in range(15):
                    sum_array+=bangtinh10[k]
                x1=so_sanh(nhietdo,myrs[i][0])
                if x1==1:
                    x1=1
                else: x1=0.1
                x2=so_sanh(quatgio,myrs[i][1])
                if x2==1:
                    x2=1
                else : x2=0
                x3=so_sanh(dongho,myrs[i][2])
                if x3==1:
                    x3=1
                else : x3=0
                x4=so_sanh(maynenam,myrs[i][3])
                if x4==1:
                    x4=1
                else : x4=0.2
                x5=so_sanh(mui,myrs[i][4])
                if x5==1:
                    x5=1
                else : x5=0.3
                x6=so_sanh(maynen,myrs[i][5])
                if x6==1:
                    x6=1
                else : x6=0
                x7=so_sanh(luoiloc,myrs[i][6])
                if x7==1:
                    x7=1
                else : x7=0.5
                x8=so_sanh(tuyet,myrs[i][7])
                if x8==1:
                    x8=1
                else : x8=0.4
                x9=so_sanh(dongdien,myrs[i][8])
                if x9==1:
                    x9=1
                else : x9=0.6
                x10=so_sanh(trangthai,myrs[i][9])
                if x10==1:
                    x10=1
                else : x10=0.2
                x11=so_sanh(maychay,myrs[i][10])
                if x11==1:
                    x11=1
                else : x11=0.1
                x12=so_sanh(dieukhien,myrs[i][11])
                if x12==1:
                    x12=1
                else : x12=0
                x13=so_sanh(nuoc,myrs[i][12])
                if x13==1:
                    x13=1
                else : x13=0.1
                x14=so_sanh(den,myrs[i][13])
                if x14==1:
                    x14=1
                else : x14=0
                x15=so_sanh(dieuhoanguondien,myrs[i][14])
                if x15==1:
                    x15=1
                else : x15=0
                
                sum=(x1*bangtinh10[0]+x2*bangtinh10[1]+x3*bangtinh10[2]+x4*bangtinh10[3]+x5*bangtinh10[4]+x6*bangtinh10[5]+x7*bangtinh10[6]+x8*bangtinh10[7]+x9*bangtinh10[8]+x10*bangtinh10[9]+x11*bangtinh10[10]+x12*bangtinh10[11]+x13*bangtinh10[12]+x14*bangtinh10[13]+x15*bangtinh10[14])/sum_array
                if sum>Max:
                    Max=sum
                    IDloi=myrs[i][15]
                    cnt=[Max,IDloi]
                    a.append(cnt)
    # S=float (a[0][0]) ; id_loi=int(a[0][1])   
    # print(a)
    # print(a[len(a)-1][1])
    S=float(a[len(a)-1][0]) ; id_loi=int (a[len(a)-1][1])
    if S<0.5:
        query2=("INSERT INTO loivakhacphuc ( `loi`, `giaiphap`) VALUES ('lỗi mới','cần nhờ thợ sửa điều hòa để xem xét')")
        cur.execute(query2)
        query3=("SELECT ID FROM loivakhacphuc")
        cur.execute(query3)
        my_ID=cur.fetchall()
        id_loi=int(my_ID[0][0])
        query = ("INSERT INTO caseloi ( nhietdomaylanh, quatgioocucnong, donghododien, cotiengphatratumaynen, comuimaylanh, trangthaimaynen, bieuhienluoiloc, coxuathientuyet, hoatdongdongdien, trangthaimaylanhkhibat, maychayvangunglientuc, manhinhdieukhien, nuoctrongongdan, denbaoloi, trangthaidieuhoakhiconguondien, IDloi) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        cur.execute(query, (
        nhietdo, quatgio, dongho, maynenam, mui, maynen, luoiloc, tuyet, dongdien,
        trangthai, maychay, dieukhien, nuoc, den, dieuhoanguondien,id_loi))
        myconn.commit()
        # print(cur.rowcount)
    ketLuan(S,id_loi)
    
       
    


# def tinhToan(
#     nhietdo, quatgio, dongho, maynenam, mui, maynen, luoiloc, tuyet, dongdien,
#     trangthai, maychay, dieukhien, nuoc, den, dieuhoanguondien
# ):

#     query = ("SELECT IDloi FROM danlanhmaylanhhong"" WHERE nhietdomaylanh=%s ,quatgioocucnong=%s AND donghododien=%s AND cotiengphatratumaynen=%s AND comuimaylanh=%s AND trangthaimaynen=%s AND bieuhienluoiloc=%s AND coxuathientuyet=%s AND hoatdongdongdien=%s AND trangthaimaylanhkhibat=%s AND maychayvangunglientuc=%s AND manhinhdieukhien=%s AND nuoctrongongdan=%s AND denbaoloi=%s AND trangthaidieuhoakhiconguondien=%s  ")
#     cur.execute(query, (
#         nhietdo, quatgio, dongho, maynenam, mui, maynen, luoiloc, tuyet, dongdien,
#         trangthai, maychay, dieukhien, nuoc, den, dieuhoanguondien
#     ))
#     myresult = cur.fetchall()
#     # myresult=[(1,)]
#     dem = int(myresult[0][0])
#     if dem=="":
#         khongCo(nhietdo, quatgio, dongho, maynenam, mui, maynen, luoiloc, tuyet, dongdien,
#     trangthai, maychay, dieukhien, nuoc, den, dieuhoanguondien)
#     else: 
#         queryRS = ("SELECT loi, giaiphap FROM loivakhacphuc"" WHERE ID=%s")

#         cur.execute(queryRS, (dem,))
#         kq = cur.fetchall()

#         loi = str(kq[0][0])
#         giaiphap = str(kq[0][1])
#         print("BOT : BOT xin được trả lời là điều hòa của bạn rất có thể bị lỗi về " +
#           loi + " và giải pháp để khắc phục " + loi + " là " + giaiphap)
#     myconn.close()

    

for i in range(1):
    print("BOT: Xin chào bạn, Tôi là bot tư vấn sửa chữa điện lạnh, để tiếp tục được tư vấn mời bạn nhập tiếp tục, để hủy bạn nhập hủy\n")
    chao = input()
    nhietdo = ""
    quatgio = ""
    dongho = ""
    maynenam = ""
    mui = ""
    maynen = ""
    luoiloc = ""
    tuyet = ""
    dongdien = ""
    trangthai = ""
    maychay = ""
    dieukhien = ""
    nuoc = ""
    den = ""
    dieuhoanguondien = ""
    print("Bạn nhập:", chao)
    if chao == "tiếp tục":
        print("\n BOT :Nhiệt độ của máy lạnh như thế nào, nếu mát bạn nhập mát còn không bạn nhập không mát")
        nhietdo = input()
        while(1):
            if nhietdo=="không mát" or nhietdo=="mát":
                print("\nBạn nhập:", nhietdo)
                break
            else: 
                print("\n xin mời bạn nhập lại dữ liệu cho chính xác")
                nhietdo = input()
        print("\n BOT :Quạt gió ở cục nóng có hoạt động không? Nếu hoạt động bạn nhập chạy, không hoạt động bạn nhập không chạy")
        quatgio=input()
        while(1):
                if quatgio=="chạy" or quatgio=="không chạy":
                    print("\nBạn nhập:", quatgio)
                    break
                else: 
                    print("\n xin mời bạn nhập lại dữ liệu cho chính xác")
                    quatgio = input()
        print("\n BOT :Đồng hồ đo điện có chạy không ? Nếu chạy bạn nhập chạy , không chạy bạn nhập không chạy")
        dongho=input()
        while(1):
                if dongho=="chạy" or dongho=="không chạy":
                    print("\nBạn nhập:", dongho)
                    break
                else: 
                    print("\n xin mời bạn nhập lại dữ liệu cho chính xác")
                    dongho = input()
        print("\n BOT :Máy nén có phát ra âm thanh ồn không ? Nếu bình thường bạn nhập nhẹ , ồn bạn nhập ồn")
        maynenam=input()
        while(1):
                if maynenam=="nhẹ" or maynenam=="ồn":
                    print("\nBạn nhập:", maynenam)
                    break
                else: 
                    print("\n xin mời bạn nhập lại dữ liệu cho chính xác")
                    maynenam = input()
        print("\n BOT :Máy lạnh có mùi lạ không  ? Nếu có bạn  nhập không mùi , không bạn nhập mùi lạ ")
        mui=input()
        while(1):
                if mui=="không mùi" or mui=="mùi lạ":
                    print("\nBạn nhập:", mui)
                    break
                else: 
                    print("\n xin mời bạn nhập lại dữ liệu cho chính xác")
                    mui = input()
        print("\n BOT :Máy nén có hoạt động không ? Nếu chạy bạn ghi chạy , không chạy bạn nhập không chạy")
        maynen=input()
        while(1):
                if maynen=="chạy" or maynen=="không chạy":
                    print("\nBạn nhập:", maynen)
                    break
                else: 
                    print("\n xin mời bạn nhập lại dữ liệu cho chính xác")
                    maynen = input()
        print("\n BOT :Lưới lọc có sạch không? Nếu không bẩn bạn nhập bình thường  , bẩn thì bạn nhập bẩn")
        luoiloc=input()
        while(1):
                if luoiloc=="bình thường" or luoiloc=="bẩn":
                    print("\nBạn nhập:", luoiloc)
                    break
                else: 
                    print("\n xin mời bạn nhập lại dữ liệu cho chính xác")
                    luoiloc = input()

        print("\n BOT :Có xuất hiện tuyết không ? Nếu bình thường bạn nhập ít, nhiều bạn nhập nhiều")
        tuyet=input()
        while(1):
                if tuyet=="ít" or tuyet=="nhiều":
                    print("\nBạn nhập:", tuyet)
                    break
                else: 
                    print("\n xin mời bạn nhập lại dữ liệu cho chính xác")
                    tuyet = input()

        print("\n BOT :Hoạt động của dòng điện như nào? Nếu bình thường bạn nhập bình thường , không thì bạn nhập thấp hơn")
        dongdien=input()
        while(1):
                if dongdien=="bình thường" or dongdien=="thấp hơn":
                    print("\nBạn nhập:", dongdien)
                    break
                else: 
                    print("\n xin mời bạn nhập lại dữ liệu cho chính xác")
                    dongdien = input()
        print("\n BOT :Trạng thái của máy lạnh khi bật ra sao? Nếu bình thường bạn nhập bình thường , nếu không bạn nhập tự động ngắt")
        trangthai=input()
        while(1):
                if trangthai=="bình thường" or trangthai=="tự động ngắt":
                    print("\nBạn nhập:", trangthai)
                    break
                else: 
                    print("\n xin mời bạn nhập lại dữ liệu cho chính xác")
                    trangthai = input()
        print("\n BOT :Có tình trạng Máy chạy và ngưng liên tục không  ? Nếu bình thường bạn nhập bình thường  , ngược lại bạn nhập ngưng liên tục")
        maychay=input()
        while(1):
                if maychay=="bình thường" or maychay=="ngưng liên tục":
                    print("\nBạn nhập:", maychay)
                    break
                else: 
                    print("\n xin mời bạn nhập lại dữ liệu cho chính xác")
                    maychay = input()
        
        print("\n BOT :Màn hình điều khiển có hiển thị không ? Nếu bình thường bạn nhập lên hình, không lên hình bạn nhập không lên hình")
        dieukhien=input()
        while(1):
                if dieukhien=="lên hình" or dieukhien=="không lên hình":
                    print("\nBạn nhập:", dieukhien)
                    break
                else: 
                    print("\n xin mời bạn nhập lại dữ liệu cho chính xác")
                    dieukhien = input()
        
        print("\n BOT :Nước có tồn động trong ống dẫn không ? Nếu có bạn nhập có  , không có bạn nhập không có")
        nuoc=input()
        while(1):
                if nuoc=="có" or nuoc=="không có":
                    print("\nBạn nhập:", nuoc)
                    break
                else: 
                    print("\n xin mời bạn nhập lại dữ liệu cho chính xác")
                    nuoc = input()
        print("\n BOT :Đèn báo lỗi có hiện tượng gì ? Nếu bình thường bạn nhập không có, nếu đèn nhấp nhấp bạn nhập có nhấp nháy")
        den=input()
        while(1):
                if den=="không có" or den=="có nhấp nháy":
                    print("\nBạn nhập:", den)
                    break
                else: 
                    print("\n xin mời bạn nhập lại dữ liệu cho chính xác")
                    den = input()
        print("\n BOT :Trạng thai diều hòa khi có nguồn điện như nào ? Nếu bình thường bạn nhập bình thường, nếu không chạy bạn nhập không chạy")
        dieuhoanguondien=input()
        while(1):
                if dieuhoanguondien=="bình thường" or dieuhoanguondien=="không chạy":
                    print("\nBạn nhập:", dieuhoanguondien)
                    break
                else: 
                    print("\n xin mời bạn nhập lại dữ liệu cho chính xác")
                    dieuhoanguondien = input()
        khongCo(nhietdo,quatgio,dongho,maynenam,mui,maynen,luoiloc,tuyet,dongdien,
                        trangthai,maychay,dieukhien,nuoc,den,dieuhoanguondien)
    else:
        print("\n Cảm ơn bạn đã chào hỏi BOT")
        break

