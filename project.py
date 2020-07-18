let = ['.',',','!','?','-','+']
sent = input()
listsent = str.split(sent, ' ')
alist = []
for i in range(len(listsent)):
    blist = []
    w=len(listsent[i])
    punct = 0
    for o in range(w):
        if listsent[i][o] in let:
            punct = 1

    for j in range(w):
        if punct == 1:
            if listsent[i][j] not in let:
                blist.append(listsent[i][w-2-j])
            else:
                blist.append(listsent[i][w-1])
        else:
            blist.append(listsent[i][w-1-j])
    alist.append(blist)
clist = []
for i in range(len(alist)):
    clist.append(''.join(alist[i]))
done = ' '.join(clist)
print (done)
dlist = []
for i in range(len(listsent)):
    word = listsent[i]
    if word not in dlist:
        dlist.append(word)
    else:
        continue
    wcount = 0
    for j in range(len(listsent)):
        if listsent[j] == word:
            wcount+=1
    print(word+' '+str(wcount))
 