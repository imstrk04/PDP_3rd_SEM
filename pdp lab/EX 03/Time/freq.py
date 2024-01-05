class Frequency:

    def frequency(self, file, word):
        cnt = 0
        with open(file, 'r') as f:
            words = f.read().split()
            for w in words:
                if w==word:
                    cnt+=1
        return cnt 