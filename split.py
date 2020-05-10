#!/share/apps/anaconda3/bin/python
import getopt, sys
opts, args = getopt.getopt(sys.argv[1:],'-h-c:-s:',['help','contig=','scaffold='])
if opts==[]:
   print("-a or --align==your file \n-h or --help for useage")
for o,a in opts:
    if o in ("-h","--help"):
        print("you need help")
        sys.exit()
    if o in ("-c", "--contig"):
        g=open(a,"w")
    if o in ("-s","--scaffold"):
        f=open(a,"r")
dic={}
for l in f.readlines():
    l=l[:-1]
    if l[0]==">":
       ID=l
       dic[ID]=""
    else:
       s=l.replace("N"," ")
       dic[ID]=str(dic[ID])+str(s)
for i in dic.keys():
    dic[i]=dic[i].split() 
for i in dic.keys():
    n=0
    for v in range(len(dic[i])):
         print(i,"_",v,sep="",file=g)
         print(dic[i][v],file=g)    
         n=n+len(dic[i][v])   
    print(n)
