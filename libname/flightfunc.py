def flightfunc():
    import pickle
    f=open('file.dat','wb')
    n=int(input('No of lines='))
    for i in range(n):
        a=int(input('Flight ID='))
        b=input('Flight name=')
        c=input('From location=')
        d=input('Destination=')
        e=float(input('Fare='))
        l=[a,b,c,d,e]
        pickle.dump(l,f)
    f.close()

    def addrec():
        f=open('file.dat','ab')
        D=input('Do you want to add?')
        while D.lower()=='y':
            a=int(input('Flight ID='))
            b=input('Flight name=')
            c=input('From location=')
            d=input('Destination=')
            e=float(input('Fare='))
            l=[a,b,c,d,e]
            pickle.dump(l,f)
            D=input('Do you want to add?')
        f.close()

    def display():
        F=open('file.dat','rb')
        print('ID','NAME','FROM','TO','FARE',sep='\t')
        try:
            while True:
                L=pickle.load(F)
                print(L[0],L[1],L[2],L[3],L[4],sep='\t')
        except EOFError:
            pass

    def search():
        X=input('Start searching?')
        while X.lower()=='y':
            print('Search with:\n1.From location\n2.Flight ID')
            S=int(input('Choice='))
            if S==1:
                F=open('file.dat','rb')
                m=0
                v=input('enter from location=')
                try:
                    print('Flights Starting:\n')
                    while True:
                        k=pickle.load(F)
                        if k[2].lower()==v.lower():
                            m+=1
                            print(k[1])
                except EOFError:
                    pass
                if m==0:
                    print('No flights are departing from',v)
            elif S==2:
                F=open('file.dat','rb')
                m=0
                v=int(input('Enter Id='))
                try:
                    print('Flights Details:\n')
                    while True:
                        k=pickle.load(F)
                        if k[0]==v:
                            m+=1
                            print(k)
                except EOFError:
                    pass
                if m==0:
                    print('No flights with that ID')
            X=input('Search again?')

    def incfare():
        f=open('file.dat','rb+')
        m=0
        try:
            while True:
                o=f.tell()
                K=pickle.load(f)
                if K[1].lower()=='air india':
                    m+=1
                    K[4]+=(10/100)*K[4]
                    f.seek(o)
                    pickle.dump(K,f)
        except EOFError:
            pass
        if m==0:
            print('No Air India flights in file')

    j=input('Start?')
    while j.lower()=='y':
        print('1.Add Record\n2.Search Record\n3.Display all records\n4.Increase fare of air india flights by 10% and display')
        c=int(input('Choice='))
        if c==1:
            addrec()
        elif c==2:
            search()
        elif c==3:
            display()
        elif c==4:
            incfare()
            display()
        else:
            print('Invalid Choice')
        j=input('Continue?')
