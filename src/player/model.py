'''
Created on 5 Jul 2014

@author: canisater
'''

class Model(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.grid_size = (10,10)
        self.own_ships = {}
        self.own_shots = {}
        self.nme_shots = {}
        