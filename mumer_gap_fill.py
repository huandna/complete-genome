#!/share/apps/anaconda3/bin/python
import getopt, sys
opts, args = getopt.getopt(sys.argv[1:],'-h-a:-b:-c:-d:-e:')
if opts==[]:
   print("-a or --align==your file \n-h or --help for useage")
for o,a in opts:
    if o in ("-h","--help"):
        print("you need help")
        sys.exit()
    if o in ("-a", "--align"):
         with open(a, 'r') as f:
           lis1=f.readlines()
    if o in ("-b", "--hhh"):
         with open(a, 'r') as g:
           lis2=g.readlines()
    if o in ("-d","--seq"):
         m=open(a,"w")
    if o in ("-c","--seq"): 
         rate=float(a)
    if o in ("-e","--seq"):
         lth=int(a)
dic2={}
for l in lis1:
     l=l.strip()
     l=l.split()
     dic2[l[0]]=[]
for l in lis1:
     l=l.strip()
     l=l.split()
     ID=l[0]
     dic2[ID].append([l[1],l[2],l[3],l[5]])
dic3={}
dic4={}
for l in lis2:
    l=l.strip()
    l=l.split()
    if l[-2] in dic2.keys() and dic2[l[-2]]!=[]:
        for i in dic2[l[-2]]:
             ID=tuple([l[-1],l[-2],i[0],i[1]])
             dic3[ID]=[]
             dic4[ID]=[]
for l in lis2:
    l=l.strip()
    l=l.split()
    if l[-2] in dic2.keys() and dic2[l[-2]]!=[]:
        for i in dic2[l[-2]]:
             ID=tuple([l[-1],l[-2],i[0],i[1]])
             if int(l[1])<=int(i[0]):
                   if dic3[ID]==[]:
                      dic3[ID]=[l[2],l[3],l[0],l[1],l[8]]
                      #print("three",ID,dic3[ID])
                   else:
                      if int(l[1])>=int(dic3[ID][3]):
                         dic3[ID]=[l[2],l[3],l[0],l[1],l[8]]
                         #print("three",ID,dic3[ID])
        for i in dic2[l[-2]]:
             ID=tuple([l[-1],l[-2],i[0],i[1]])
             if int(l[0])>=int(i[1]):
                   if dic4[ID]==[]:
                      dic4[ID]=[l[2],l[3],l[0],l[1],l[8]]
                      #print("four",ID,dic4[ID])        
                   else:
                      if int(l[0])<=int(dic4[ID][2]):
                         dic4[ID]=[l[2],l[3],l[0],l[1],l[8]]
                         #print("four",ID,dic4[ID])
dic5={}
for i in dic3.keys():
    #print(i,dic3[i],dic4[i])
    if dic3[i]!=[]:
       if int(dic3[i][0])>int(dic3[i][1]):
          dic3[i][0],dic3[i][1]=dic3[i][1],dic3[i][0]
          dic3[i].append("-")
       else:
          dic3[i].append("+")
    else:
        dic3[i].append("none")
for i in dic4.keys():
    #print(4,i,dic4[i])
    if dic4[i]!=[]:
       if int(dic4[i][0])>int(dic4[i][1]):
          dic4[i][0],dic4[i][1]=dic4[i][1],dic4[i][0]
          dic4[i].append("-")
       else:
          dic4[i].append("+")
    else:
        dic4[i].append("none")
for I in dic2.keys():
    for i in dic2[I]:
        IDD=tuple([I,i[0],i[1]])
        dic5[IDD]=[i[2],i[3]]
for D in dic3.keys():
    IDD=tuple([D[1],D[2],D[3]])
    pos1=D[2]
    pos2=D[3]
    gaplenth=int(pos2)-int(pos1)
    if "none" not in dic3[D]:
       cha3=int(pos1)-int(dic3[D][3])
    if "none" not in dic4[D]:
       cha4=int(dic4[D][2])-int(pos2)
    if dic3[D][-1]=="+" and dic4[D][-1]=="+" and len(dic5[IDD])==2: 
       rel_lenth=int(dic4[D][0])-int(dic3[D][1])-int(cha3)-int(cha4)
       if int(rel_lenth)>=int(gaplenth)*rate:
           dic5[IDD].extend(["+","brifix",D[0],int(dic3[D][1])+int(cha3), int(dic4[D][0])-int(cha4)])
       elif int(dic3[D][4])-int(dic3[D][1])-int(cha3)>=gaplenth*rate:
              if int(dic3[D][4])-int(dic3[D][1])-int(cha3)>=gaplenth:
                  dic5[IDD].extend(["+","singlefix",D[0],int(dic3[D][1])+int(cha3),int(dic3[D][1])+int(cha3)+int(gaplenth)])
              else:
                  dic5[IDD].extend(["+","singlefix",D[0],int(dic3[D][1])+int(cha3),dic3[D][4]])
       elif int(dic4[D][0])-int(cha4)>=gaplenth*rate:
              if int(dic4[D][0])-int(cha4)>=gaplenth:
                 dic5[IDD].extend(["+","singlefix",D[0],int(dic4[D][0])-int(cha4)-int(gaplenth),int(dic4[D][0])-int(cha4)])
              else:
                 dic5[IDD].extend(["+","singlefix",D[0],1,int(dic4[D][0])-int(cha4)])
       elif int(rel_lenth)<=0 and int(gaplenth)<=lth:
              if int(dic3[D][0])<=int(dic4[D][1]):
                   dic5[IDD].extend(["+","infix",D[0],0,0])
       else:
              continue
    elif dic3[D][-1]=="-" and dic4[D][-1]=="-" and len(dic5[IDD])==2: 
       rel_lenth=int(dic3[D][0])-int(dic4[D][1])-int(cha3)-int(cha4)
       if int(rel_lenth)>=int(gaplenth)*rate:
           dic5[IDD].extend(["-","brifix",D[0],int(dic4[D][1])+int(cha3), int(dic3[D][0])-int(cha4)])
       elif int(dic4[D][4])-int(dic4[D][1])-int(cha4)>= gaplenth* rate:
              if int(dic4[D][4])-int(dic4[D][1])-int(cha4)>= gaplenth:
                 dic5[IDD].extend(["-","singlefix",D[0],int(dic4[D][1])+int(cha4),int(dic4[D][1])+int(cha4)+int(gaplenth)])
              else:
                 dic5[IDD].extend(["-","singlefix",D[0],int(dic4[D][1])+int(cha4),int(dic4[D][4])])
       elif int(dic3[D][0])-int(cha3) >= gaplenth* rate:
              if int(dic3[D][0])-int(cha3) >= gaplenth:
                 dic5[IDD].extend(["-","singlefix",D[0],int(dic3[D][0])-int(cha3)-int(gaplenth),int(dic3[D][0])-int(cha3)])
              else:
                 dic5[IDD].extend(["-","singlefix",D[0],1,int(dic3[D][0])-int(cha3)])
       elif int(rel_lenth)<=0 and int(gaplenth)<=lth:
              if int(dic3[D][1])<=int(dic4[D][0]): 
                   dic5[IDD].extend(["-","infix",D[0],0,0])
       else:
              continue 
    elif dic3[D][-1]!="none" or dic4[D][-1]!="none":
       if dic3[D][-1]=="+" and len(dic5[IDD])==2:
           if int(dic3[D][4])-int(dic3[D][1])-int(cha3)>=gaplenth*rate:
              if int(dic3[D][4])-int(dic3[D][1])-int(cha3)>=gaplenth:
                  dic5[IDD].extend(["+","singlefix",D[0],int(dic3[D][1])+int(cha3),int(dic3[D][1])+int(cha3)+int(gaplenth)])
              else:
                  dic5[IDD].extend(["+","singlefix",D[0],int(dic3[D][1])+int(cha3),dic3[D][4]])
              #print("x")
       elif dic3[D][-1]=="-" and len(dic5[IDD])==2:
           if int(dic3[D][0])-int(cha3) >= gaplenth*rate:
              if int(dic3[D][0])-int(cha3) >= gaplenth:
                 dic5[IDD].extend(["-","singlefix",D[0],int(dic3[D][0])-int(cha3)-int(gaplenth),int(dic3[D][0])-int(cha3)])
              else:
                 dic5[IDD].extend(["-","singlefix",D[0],1,int(dic3[D][0])-int(cha3)])
              #print("x")
       elif dic4[D][-1]=="+" and len(dic5[IDD])==2:
           if int(dic4[D][0])-int(cha4)>=gaplenth*rate:
              if int(dic4[D][0])-int(cha4)>=gaplenth:
                 dic5[IDD].extend(["+","singlefix",D[0],int(dic4[D][0])-int(cha4)-int(gaplenth),int(dic4[D][0])-int(cha4)])
              else:
                 dic5[IDD].extend(["+","singlefix",D[0],1,int(dic4[D][0])-int(cha4)])
              #print("x")
       elif dic4[D][-1]=="-" and len(dic5[IDD])==2:
           if  int(dic4[D][4])-int(dic4[D][1])-int(cha4)>= gaplenth*rate:
              if int(dic4[D][4])-int(dic4[D][1])-int(cha4)>= gaplenth: 
                 dic5[IDD].extend(["-","singlefix",D[0],int(dic4[D][1])+int(cha4),int(dic4[D][1])+int(cha4)+int(gaplenth)])
              else:
                 dic5[IDD].extend(["-","singlefix",D[0],int(dic4[D][1])+int(cha4),int(dic4[D][4])])
              #print("x")
       else:
           continue
    else:
         continue
for i in dic5.keys():
    print(i[0],"\t",i[1],"\t",i[2],end="\t",file=m)
    for v in dic5[i]:
       print(v,end="\t",file=m)
    print(end="\n",file=m)
