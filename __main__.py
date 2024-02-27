# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 08:13:40 2020

@author: srappold
"""

"""
"""
import Notebooks.Sankey as sankey
import Notebooks.Network as network
import Notebooks.Cypher as cypher
import os
import sys

#from platform import python_version

__author__ = 'Scott Rappold'
__copyright__ = 'Copyright 2019-2021'
__license__ = ''
__maintainer__ = 'Scott Rappold'
__email__ = 'rappold.scott@gmail.com'


def main() -> None:
    # print command line arguments
#    for arg in sys.argv[1:]:
#        print(arg)

	#sankey.make_sankey()
    cypher.write_cypher()
    
#    network.make_network()

    print('completed')
        
if __name__ == '__main__':
    main()