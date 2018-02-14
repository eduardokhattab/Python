#vou executar dois codigos que fazem a mesma coisa
#um utilizando o python puro e outro o numpy
#perceba a diferença de tempo ao executa-los separadamente

import numpy as np
print(np.arange(1,100000001, dtype='int64').sum())