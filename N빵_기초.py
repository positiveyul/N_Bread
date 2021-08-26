a = "" #참석자 명단
b = {} #참석자별 금액 정리
final = {} #총금액 최종 정리
n차=int(input("총 회식은 몇번 진행이 되었나요? : "))

for i in range(1,n차+1):
    b = {}
    print("{}차".format(i))
   
    print("회식에 참석한 사람들의 이름을 모두 써주세요, 다 쓰면 end를 입력해주세요.") #여기서 3명이라고 썼을때 딱 3명의 input만 받게 하는 법???????
    a=""
    while a !="end":
        a = input("회식 참석자: ")
        if a in b:
            b[a]= b[a]
        else: b[a]= 0
 
    if 'end' in b:
        del b['end']
    if '끝' in b:
        del b['끝']    

    # print("회식 참석자 명단입니다~~~",b.keys())
    #print(len(b.keys()))
    print("총 {}명이 참석하였습니다~".format(len(b)))

    while True:
        try:
            print("총 얼마를 내셨나요?")
            총금액 = int(input("총 금액을 입력해주세요: "))
            break    
        except (ValueError):
            print("금액은 0을 제외한 정수만 입력하셔야 합니다.")



    총무 = input("총무는 누가 하였나요?: " )
    while 총무 not in b:
        print("총무를 다시 입력해주세요.")
        총무 = input("총무는 누가 하였나요?: ")

    b[총무]= -총금액 + b[총무]
    # print(b, "총무가격")

    for x in b.keys():
        b[x]= int(총금액/len(b) + b[x]) #입력한 사람만 하게 해야하는데,,,,\


    #print(b, "N빵 {}차 결과".format(i))
    for kb,vb in b.items():
        if kb in final:
            final[kb] = final[kb]+b[kb]
        else:
            final[kb] = b[kb]
    # print("{}차".format(i),final)
    #print("아래와 같이 나누어 주세요")

    #for x in b.keys():
    #    if b[x] > 0:
    #        print("{}는 {}에게 {}의 금액을 주세요".format(x,총무,b[x]))


##어떻게 나누어 줄까?
copy = final


for kfinal,vfinal in final.items():
    for kcopy, vcopy in copy.items():
        if int(final[kfinal]) !=0 and int(final[kfinal])+int(copy[kcopy])==0:
                print("{} --> {}에게 {}를 준다.".format(kfinal,kcopy,final[kfinal]))
                final[kfinal]=0 #줬으니 차감
                copy[kcopy]=0
                final[kcopy]=0
                copy[kfinal]=0
                print("같은 가격 있는 지 계산!!!!!",final,copy)


for kfinal,vfinal in final.items():
    for kcopy, vcopy in copy.items():
        if copy[kcopy]<0 and final[kfinal]>0:            
            if int(final[kfinal])+int(copy[kcopy])<0:
                print("{} --> {}에게 {}를 준다.".format(kfinal,kcopy,final[kfinal]))
                copy[kcopy]=int(final[kfinal])+int(copy[kcopy])
                final[kcopy]=copy[kcopy]
                final[kfinal]=0
                copy[kfinal]=0
                #print("총무가 받을 게 아직 남음!!/n",final)
            else:
                print("{} --> {}에게 {}를 준다.".format(kfinal,kcopy,-copy[kcopy])) #총무가 받아야 할 돈이 적을 때이므로 총무가 받을 만큼만 받으면 된다.
                final[kfinal]=int(final[kfinal])+int(copy[kcopy])
                copy[kcopy]=0 #특정 총무 돈 다 갚음!!
                final[kcopy]=copy[kcopy]                
                copy[kfinal]=final[kfinal]
                #print("총무 돈은 다 줌!!!/n",final)
            #print("4",final,copy)
        #print("5",final,copy)
    #print("6",final,copy)    



