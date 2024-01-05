class SizeMismatchError(Exception):
    pass

class VectorLenZeroError(Exception):
    pass

def Getratios(vec1, vec2):
    try:
        if len(vec1) == 0 or len(vec2) == 0:
            raise VectorLenZeroError('vector cannot be empty')

        if len(vec1) != len(vec2):
            raise SizeMismatchError('vector lengths are different')

        ratios = []
        try:
            for a, b in zip(vec1, vec2):
                if b == 0:
                    ratios.append('NaN')
                    

                else:
                    r = a / b
                    ratios.append(r)
        except ZeroDivisionError as e:
            return f' error {e}'

        return ratios

    except VectorLenZeroError as e:
        return f' error {e}'
    except SizeMismatchError as e:
        return f'error {e}'


v1 = [8, 4]
v2 = [2, 0]

print(Getratios(v1, v2))


        
            

        
        
