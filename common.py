#!/share/apps/anaconda3/bin/python
import getopt, sys
opts, args = getopt.getopt(sys.argv[1:],'-h-a:-b:')
if opts==[]:
   print("-a or --align==your file \n-h or --help for useage")
dic={}
for o,a in opts:
    if o in ("-h","--help"):
        print("you need help")
        sys.exit()
    if o in ("-a", "--align"):
        with open(a, 'r') as f:
           list1 = f.readlines()
    if o in ("-b","--seq"):
        g=open(a,"w")
for l in list1:
    l=l.strip() 
    l=l.split()
    ID=l[-1]
    dic[ID]=[]
for l in list1:
    l=l.strip()
    l=l.split()
    ID=l[-1]
    #l[-2]=l[-2].split("_")
    #if l[-2][0] in dic[ID]:
    if l[-2]in dic[ID]:
       continue
    else:
       dic[ID].append(l[-2]) 
       #dic[ID].append(l[-2][0])
for k in dic.keys():
    print(k,end="\t",file=g) 
    for v in dic[k]:
        print(v,end="\t",file=g)
        print(v)
    print(end="\n",file=g)           
