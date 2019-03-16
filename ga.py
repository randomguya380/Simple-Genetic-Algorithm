import random

def dec2bin(n):
    return(format(n,'05b'))

def bin2dec(n):
   
    return(int(n,2))
    
def avg(li):
    return(sum(li)/len(li))
    
pop_size=10
pop=[]
for i in range(pop_size):
    chrom=random.randint(0,31)
    pop.append(chrom)

bin_pop=[dec2bin(f) for f in pop]
print(pop)
sq_avg=10

maxicount=1
while maxicount<8:
    print(pop)
    new=[]
    sq_pop=[f**2 for f in pop]
    
    sq_avg=avg(sq_pop)
    sum_sq_pop=sum(sq_pop)
    ps=[(f/sum(sq_pop)) for f in sq_pop]
    ps_avg=avg(ps)
    ps_sum=sum(ps)
    
    pm=[f/ps_avg for f in ps]
    pm_avg=avg(pm)
    pm_sum=sum(pm)
   
    ps_per=[f*1000 for f in ps]
    sumi=0
    cumi_ps=[]
    for l in ps_per:
        sumi+=l
        cumi_ps.append(sumi)
    for l in range(len(pop)):
        rand=random.randint(0,1000)
        c=0
        while c<10:
            if rand<=cumi_ps[c]:
                new.append(pop[c])
                break
            c=c+1
           
       
     
        
    
    bin_pop=[dec2bin(f) for f in new]
        
    for i in range(0,len(new),2):
        
        popi=list(bin_pop[i])
            
        popis=list(bin_pop[i+1])
        cross_site=random.randint(0,4)
        
    #print('before cross over')
    #print(popi,popis)
    #print(cross_site)
        
        
    for j in range(cross_site+1,5):
        
        if popi[j]=='1' and popis[j]=='0':
            popi[j]='0'
            popis[j]='1'
        elif popi[j]=='0' and popis[j]=='1':
            popi[j]='1'
            popis[j]='0'
        else:
            pass
            
    #print('After cross over')
    #print(popi,popis)
        
    popi=''.join(popi)
    popis=''.join(popis)
    bin_pop[i]=popi
    bin_pop[i+1]=popis
    pop=[bin2dec(f) for f in bin_pop]
      
    maxi=max(pop)
    maxicount=pop.count(maxi)
    
     
    
    
        
