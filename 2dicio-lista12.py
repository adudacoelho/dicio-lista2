def printDic(d):
 for k in d:
    print("%30s, %4d" % (k,d[k]))

def limpa(s):
   ns = ""
   for c in s:
      if c.isallnum():
         ns = ns + c
   return ns

def main():

    arq = open("documento1.txt" , "rt", encoding = "UTF-8")
    D = {}

    linha = arq.readline()
    while linha != "":
        lst = linha.strip().split()

        for palavra in lst:
            if palavra in D:
                D[palavra] = D[palavra] + 1
            else:
                D[palavra] = 1

        linha = arq.readline()

    printDic(D)

main()