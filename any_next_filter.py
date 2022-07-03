t = (None, False, "", "witch", None, True)

#
lstComp = next(v for v in t if v)
print(lstComp) # witch

lstFilter = next(filter(None, t))
print(lstFilter) # witch

anyResult = any(t)
print(anyResult) # true