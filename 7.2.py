from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
a=Counter("высокий уровень вовлечения представителей целевой аудитории является четким доказательством простого факта, что реализация намеченных плановых заданий является качественно новой ступенью позиций, занимаемых участниками в отношении поставленных задач, но постоянное информационнопропагандистское обеспечение нашей деятельности требует от нас анализа существующих финансовых и административных условий")
plt.bar(*zip(*a.most_common()), width=.5, color='g')
plt.show()