
"""
##########################################################
### @Author Joe Krall      ###############################
### @copyright see below   ###############################

    This file is part of JMOO,
    Copyright Joe Krall, 2014.

    JMOO is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    JMOO is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with JMOO.  If not, see <http://www.gnu.org/licenses/>.

###                        ###############################
##########################################################
"""

"Brief notes"
"Property File.  Defines default settings."

from jmoo_algorithms import jmoo_NSGAII, jmoo_SWAY5, jmoo_SPEA2
from jmoo_problems import *

from Problems.NRP.nrp import *
# from Problems.MONRP.monrp import *
from Problems.POM3.POM3B import *
from Problems.POM3.POM3B_1_2 import *
from Problems.POM3.POM3B_2_3 import *

from Problems.POM3.POM3A import *
from Problems.POM3.POM3A_1_2 import *
from Problems.POM3.POM3A_2_3 import *

from Problems.POM3.POM3C import *
from Problems.POM3.POM3C_1_2 import *
from Problems.POM3.POM3C_2_3 import *

from Problems.POM3.POM3D import *
from Problems.POM3.POM3D_1_2 import *
from Problems.POM3.POM3D_2_3 import *

from Problems.XOMO.XOMO_flight import *
from Problems.XOMO.XOMO_flight_1_2 import *
from Problems.XOMO.XOMO_flight_2_3 import *
from Problems.XOMO.XOMO_flight_3_4 import *

from Problems.XOMO.XOMO_all import *
from Problems.XOMO.XOMO_all_1_2 import *
from Problems.XOMO.XOMO_all_2_3 import *
from Problems.XOMO.XOMO_all_3_4 import *

from Problems.XOMO.XOMO_ground import *
from Problems.XOMO.XOMO_ground_1_2 import *
from Problems.XOMO.XOMO_ground_2_3 import *
from Problems.XOMO.XOMO_ground_3_4 import *

from Problems.XOMO.XOMO_osp import *
from Problems.XOMO.XOMO_osp_1_2 import *
from Problems.XOMO.XOMO_osp_2_3 import *
from Problems.XOMO.XOMO_osp_3_4 import *

from Problems.XOMO.XOMO_osp2_1_2 import *
from Problems.XOMO.XOMO_osp2_2_3 import *
from Problems.XOMO.XOMO_osp2_3_4 import *
from Problems.XOMO.XOMO_osp2 import *

from Problems.NRP.nrp import NRP
from Problems.MONRP.monrp import MONRP



# JMOO Experimental Definitions
algorithms = [
            # jmoo_NSGAII(),
            # jmoo_SPEA2(),
            # jmoo_GALE(),
            # jmoo_SWAY2(),
            jmoo_SWAY5()
              ]

problems =[
    POM3A_1_2(), POM3A_2_3(),
    # POM3A(),
    # POM3B(),
    POM3B_1_2(), POM3B_2_3(),
    # # POM3C(),
    POM3C_1_2(), POM3C_2_3(),
    # # POM3D(),
    POM3D_1_2(), POM3D_2_3(),
    # # XOMO_flight(),
    XOMO_flight_1_2(), XOMO_flight_2_3(), XOMO_flight_3_4(),
    # # # XOMO_all(),
    XOMO_all_1_2(), XOMO_all_2_3(), XOMO_all_3_4(),
    # # # XOMO_ground(),
    XOMO_ground_1_2(), XOMO_ground_2_3(), XOMO_flight_3_4(),
    # # # XOMO_osp(),
    XOMO_osp_1_2(), XOMO_osp_2_3(), XOMO_osp_3_4(),
    # # # XOMO_osp2(),
    XOMO_osp2_1_2(), XOMO_osp2_2_3(), XOMO_osp2_3_4()
    # MONRP(50, 4, 5, 0, 90), MONRP(50, 4, 5, 0, 110), MONRP(50, 4, 5, 4, 90), MONRP(50, 4, 5, 4, 110),
    # NRP(50, 4, 5, 0, 90), NRP(50, 4, 5, 0, 110), NRP(50, 4, 5, 4, 90), NRP(50, 4, 5, 4, 110),
    ]



build_new_pop = False                                       # Whether or not to rebuild the initial population

Configurations = {
    "Universal": {
        "Repeats" : 20,
        "Population_Size" : 10000,
        "No_of_Generations" : 1
    },
    "NSGAIII": {
        "SBX_Probability": 1,
        "ETA_C_DEFAULT_" : 30,
        "ETA_M_DEFAULT_" : 20
    },
    "GALE": {
        "GAMMA" : 0.15,  # Constrained Mutation Parameter
        "EPSILON" : 1.00,  # Continuous Domination Parameter
        "LAMBDA" :  3,     # Number of lives for bstop
        "DELTA"  : 3       # Accelerator that increases mutation size
    },
    "DE": {
        "F" : 0.75, # extrapolate amount
        "CF" : 0.3, # prob of cross over
    },
    "MOEAD" : {
        "niche" : 20,  # Neighbourhood size
        "SBX_Probability": 1,
        "ETA_C_DEFAULT_" : 20,
        "ETA_M_DEFAULT_" : 20,
        "Theta" : 5
    },
    "STORM": {
        "STORM_EXPLOSION" : 5,
        "STORM_POLES" : 20,  # number of actual poles is 2 * ANYWHERE_POLES
        "F" : 0.75, # extrapolate amount
        "CF" : 0.3, # prob of cross over
        "STORM_SPLIT": 6,  # Break and split into pieces
        "GAMMA" : 0.15,
    }
}


# File Names
DATA_PREFIX        = "Data/"
DEFECT_PREDICT_PREFIX = "defect_prediction/"
VERSION_SPACE_PREFIX = "version_space/"

"decision bin tables are a list of decisions and objective scores for a certain model"
DECISION_BIN_TABLE = "decision_bin_table"

"result scores are the per-generation list of IBD, IBS, numeval,scores and change percents for each objective - for a certain model"
RESULT_SCORES      = "result_"

SUMMARY_RESULTS    = "summary_"

RRS_TABLE = "RRS_TABLE_"
DATA_SUFFIX        = ".datatable"


