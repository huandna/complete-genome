#!/share/apps/anaconda3/bin/python
import getopt, sys
opts, args = getopt.getopt(sys.argv[1:],'-h-a:-b:-c:-d:')
if opts==[]:
   print("-a or --align==your file \n-h or --help for useage")
for o,a in opts:
    if o in ("-h","--help"):
        print("you need help")
        sys.exit()
    if o in ("-a", "--seq1"):
         with open(a, 'r') as f:
           lis1=f.readlines()
    if o in ("-b", "--seq2"):
         with open(a, 'r') as g:
           lis2=g.readlines()
    if o in ("-c", "--index"):
         with open(a, 'r') as s:
           lis3=s.readlines()
    if o in ("-d", "--output"):
         p=open(a,"w")
dic_list={}
seq1={}
seq2={} 
dic1={}                # dic1=starand 
dic2={}
dic22={}                # dic2=material 
dicm={}
def DNA_complement_and_reverse(sequence):
    sequence=sequence.upper()
    transline=sequence[::-1].replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()
    return transline
for line in lis1:
    if line.startswith('>'):
           name=line.replace('>','').split()[0]
           seq1[name]=''
    else:
           seq1[name]+=line.replace('\n','').strip()
for line in lis2:
    if line.startswith('>'): 
           name=line.replace('>','').split()[0] 
           seq2[name]='' 
    else: 
           seq2[name]+=line.replace('\n','').strip() 
for l in lis3:
    l=l.strip()
    l=l.split()
    dic_list[l[0]]=[1]
for l in lis3:
    l=l.strip()
    l=l.split()
    pos1=int(l[8])-1
    pos2=int(l[9])
    dic2[tuple([l[0],int(l[1]),int(l[2]),l[5]])]=seq2[l[7]][pos1:pos2]
    dic_list[l[0]].extend([int(l[1]),int(l[2])])
for i in dic2.keys():                                       #reverse
    if i[3]=="-":
        dic2[i]=DNA_complement_and_reverse(dic2[i])
    dic22[tuple([i[0],i[1],i[2]])]=dic2[i]
    #print(">",i)
    #print(dic2[i])
del seq2
for i in dic_list.keys():
    dic_list[i].sort()
    dic_list[i].append("end")
    for n in range(0,len(dic_list[i])-1,2):
        if int(dic_list[i][n])==1:
           pos1=int(dic_list[i][n])-1
        else:
           pos1=int(dic_list[i][n])
        if dic_list[i][n+1]=="end":
          #dic1[tuple([i,dic_list[i][n],dic_list[i][n+1]])]=seq1[i][pos1:]
          dic1[tuple([i,dic_list[i][n],dic_list[i][n+1]])]=seq1[i][pos1:].replace('N','')                         #except N (single)
          #print(">",tuple([i,dic_list[i][n],dic_list[i][n+1]]),file=p)
          #print(dic1[tuple([i,dic_list[i][n],dic_list[i][n+1]])],file=p)
        else:
          #dic1[tuple([i,dic_list[i][n],dic_list[i][n+1]])]=seq1[i][pos1:int(dic_list[i][n+1])-1]
          dic1[tuple([i,dic_list[i][n],dic_list[i][n+1]])]=seq1[i][pos1:int(dic_list[i][n+1])-1].replace('N','')
          #print(">",tuple([i,dic_list[i][n],dic_list[i][n+1]]),file=p)
          #print(dic1[tuple([i,dic_list[i][n],dic_list[i][n+1]])],file=p)
for i in dic_list.keys():
    dicm[i]=[]
for i in dic_list.keys():
    for n in range(len(dic_list[i])):
        if n%2==0:
           dicm[i]+=dic1[tuple([i,dic_list[i][n],dic_list[i][n+1]])]
        elif n!=len(dic_list[i])-1:
           dicm[i]+=dic22[tuple([i,dic_list[i][n],dic_list[i][n+1]])]
        else:
           continue
for i in seq1.keys():
    if i in dicm.keys():
         seq1[i]=''.join(dicm[i])
    ID=">"+i
    print(ID,file=p)
    print(seq1[i],file=p)
    

















