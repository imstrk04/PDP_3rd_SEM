class IsExists:

    def is_existS(self, file, word):
        with open(file, 'r') as f:
            text = f.read()
            if word in text:
                return True
            return False