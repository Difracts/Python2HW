class Wordplay():
    def __init__(self,arr):
        self.arr = arr

    def words_with_length(self,n):
        output = []
        for i in self.arr:
            if len(i)==n:
                output.append(i)
        return output

    def starts_with(self,s):
        output = []
        for i in self.arr:
            if i[0]==s:
                output.append(i)
        return output

    def ends_with(self,s):
        output = []
        for i in self.arr:
            if i[-1]==s:
                output.append(i)
        return output

    def palindromes(self):
        output = []
        for i in self.arr:
            if i == i[::-1]:
                output.append(i)
        return output 

    def only(self,letters):
        output = []
        for i in self.arr:
            count = 0
            for j in i:
                if j in letters:
                    count+=1
            if len(i)==count:
                output.append(i)
        return output

    def avoids(self,letters):
        output = []
        for i in self.arr:
            count = 0
            for j in i:
                if j not in letters:
                    count+=1
            if len(i) == count:
                output.append(i)
        return output

g = Wordplay(["spiderman","hulk","ironman","qazaq","captain america","vanda","vision","black panzer","starlord","black widow"])

print(g.words_with_length(9))
print(g.starts_with("h"))
print(g.ends_with("m"))
print(g.palindromes())
print(g.only("lostrard"))
print(g.avoids("ca"))