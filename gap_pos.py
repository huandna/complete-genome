#!/share/apps/anaconda3/bin/python
import getopt, sys
opts, args = getopt.getopt(sys.argv[1:],'-h-a:-b:',['help','fasta=','pos='])
if opts==[]:
   print("-a or --fasta==your file \n-h or --help for useage")
for o,a in opts:
    if o in ("-h","--help"):
        print("you need help")
        sys.exit()
    if o in ("-a", "--fasta"):
        g=open(a,"r")
    if o in ("-b","--pos"):
        z=open(a,"w")
dic1={}
dic2={}
for l in g.readlines():
    l=l.strip()
    if l[0]==">":
        ID=l.split()[0][1:]
        dic1[ID]=0
        dic2[ID]=[]
        pos1=1
        pos2=1
        fg=0
        n=0
    else:
        dic1[ID]=dic1[ID]+len(l) 
        for i in l:
            n=n+1
            if i=="N":
               if fg==0:
                  pos1=n
                  fg=1
               else:
                  pos2=n
                  fg=1
            else:
               if fg==1: 
                  gap_lenth=int(pos2)-int(pos1)
                  if gap_lenth >= 1:
                     dic2[ID].append([pos1,pos2,gap_lenth])
               fg=0 
for ID in dic2.keys():
    mid=int(dic1[ID])/2
    for i in dic2[ID]:
        if int(i[0]) >=mid:
           i.append("right")
        elif int(i[1]) <=mid:
           i.append("left")
        else:
           i.append("middle")
        print(ID,"\t",i[0],"\t",i[1],"\t",i[2],"\t",dic1[ID],"\t",i[3],file=z)





















          
       
