#!/share/apps/anaconda3/bin/python
import getopt, sys
opts, args = getopt.getopt(sys.argv[1:],'-h-a:')
if opts==[]:
   print("-a or --align==your file \n-h or --help for useage")
for o,a in opts:
    if o in ("-h","--help"):
        print("you need help")
        sys.exit()
    if o in ("-a", "--align"):
        f=open(a,"r")
dic,dic2={},{}
lis_1kb,lis_5kb=[],[]
sum1,sum2,sum_g1,sum_g2,count_A,count_T,count_C,count_G,count_N,sum_5kb,sum_1kb=0,0,0,0,0,0,0,0,0,0,0
for l in f.readlines():
    l=l[:-1]
    if l[0]==">":
        ID=l
        dic[ID] =0
    else:
        dic[ID] = len(l)+dic[ID]
        sum1=sum1+len(l)
        for i in l:
            if i == "A" or i== "a":
                count_A=count_A+1
            if i == "T" or i== "t":
                count_T=count_T+1 
            if i == "C" or i== "c":
                count_C=count_C+1
            if i == "G" or i== "g":
                count_G=count_G+1
            if i == "N" or i== "n":
                count_N=count_N+1
list_1=sorted(dic.items(), key=lambda e:e[1], reverse=True)                          
del dic
fg=1
for i in list_1:    
    sum2=sum2+i[1]
    if sum2>=sum1*0.5 and fg:
        N50=i[1]
        fg=0
    if i[1]>=1000:
       lis_1kb.append(i[1])
    if i[1]>=5000:
       lis_5kb.append(i[1]) 	      
for i in lis_1kb:
    sum_1kb=sum_1kb+i
for i in lis_5kb:
    sum_5kb=sum_5kb+i
f.close()
print("A:\t",count_A,"\nT:\t",count_T,"\nC:\t",count_C,"\nG:\t",count_G,"\nN:\t",count_N)
print("total lenth:\t",sum1)
print("number of sequences:\t",len(list_1))
print("Average length:\t",int(sum1/len(list_1)))
print("max lenth:\t",list_1[0][1])
print("min lenth:\t",list_1[-1][1])
print("GC content:\t%.1f%%"%((count_C+count_G)/(count_C+count_G+count_T+count_A)*100))
print("N50:\t",N50)
#print(">=1kb\tNumber of sequences:\t",len(lis_1kb))
#print(">=1kb\ttotal lenth:\t",sum_1kb)
#print(">=1kb\taverage  lenth:\t",int(sum_1kb/len(lis_1kb)))
#print(">=5kb\tNumber of sequences:\t",len(lis_5kb))
#print(">=5kb\ttotal lenth:\t",sum_5kb)
#print(">=5kb\taverage  lenth:\t",int(sum_5kb/len(lis_5kb)))



