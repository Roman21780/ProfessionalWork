dict_ = {str(i): i * i for i in range(20)}

import pprint
# pprint.pp(dict_)

# import pprint as ppr
# ppr.pp(dict_)

# from pprint import pp, pformat as pf, PrettyPrinter
# pp(dict_)

from tools.my_tools.my_pprint import pprint
# from pprint import *

pprint(dict_)
