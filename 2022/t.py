# while online
# [[[ACTION for __ in [0 if CONDITION else b.clear()] if b] for INDEX in LISTE if b] for b in [[0]]]

#recursion inline
# [t(args,t) for t in [lambda args, t: ACTION]]

#set valeur (tableau -> sum)
# set = lambda t,x : [t.append[x] for _ in [t.clear()]]

# def flat(t):
#     flatten = []
#     for el in t:
#         if type(el) == list:
#             flatten += flat(el)
#         else: flatten.append(el)
#     return flatten