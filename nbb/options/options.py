import argparse
import os
from ..util import util
import torch


class Opt:
    """class to pass dictionary to mother class"""
    def __init__(self, **entries):
        self.__dict__.update(entries)

class Options():
    def __init__(self):

        self.parser = argparse.ArgumentParser()
        self.initialized = False
        self.opt = None

        self.args = {
            'imageSize': [224, 'rescale the image to this size'],
            'gpu_ids': [[0], 'gpu ids: e.g. 0  0,1,2, 0,2. use -1 for CPU'],
            'tau': [0.05, 'response threshold'],
            'border_size': [7, 'removing this brder_size correspondences in the final mapping'],
            'input_nc': [3, 'number of input channels'],
            'batchSize': [1, 'batch size'],
            'k_per_level': [1000, 'maximal number of best buddies per local search.'],
            'k_final': [10, 'The number of chosen best buddies based on their accumulative response.'],
            'fast': [False, 'if specified, stop the algorithm in layer 2, to accelerate runtime.'],
            'name': ['experiment_name', 'name of the experiment'],
            'results_dir': ['../results', 'models are saved here'],
            'save_path': [None, 'path to save outputs (use in features family)'],
            'niter_decay':[100, '# of iter to linearly decay learning rate to zero'],
            'beta1': [0.5, 'momentum term of adam'],
            'lr': [0.05, 'initial learning rate for adam'],
            'gamma': [1, 'weight for equallibrium in BEGAN or ratio between I0 and Iref features for optimize_based_features'],
            'convergence_threshold': [0.001, 'threshold for convergence for watefall mode (for optimize_based_features_model']
        }


    def initialize(self):
        """
        Pass arguments from dictionary to parser syntax
        so it can be handled from script as originally.
        Required arguments and empty arguments are passed independently
        Boolean and array arguments are turned to string.

        """
        self.parser.add_argument('--datarootA', required=True, help='path to image A')
        self.parser.add_argument('--datarootB', required=True, help='path to image B')
        self.parser.add_argument('--fast', action='store_true', help='if specified, stop the algorithm in layer 2, to accelerate runtime.')

        for arg in self.args:
            # fast already specified
            if arg == 'fast':
                continue

            argname = '--'+arg
            argdefault = self.args[arg][0]
            arghelp = self.args[arg][1]

            # None and list types need to be string for parser
            if arg == 'save_path':
                argdefault = str(argdefault)
            if arg == 'gpu_ids':
                argdefault = ','.join(str(argd) for argd in argdefault)
            argtype = type(argdefault)

            self.parser.add_argument(argname, type=argtype, default=argdefault, help=arghelp)

        self.initialized = True


    def setoptions(self, datarootA, datarootB, **kwargs):
        """
            bypass to main.py
            Examples:
            >>>
            >>>

        """
        odic = {}
        #required arguments
        odic['datarootA'] = datarootA
        odic['datarootB'] = datarootB
        for arg in self.args:
            if arg in kwargs:
                odic[arg] = kwargs[arg]
            else:
                odic[arg] = self.args[arg][0]
            print(arg, self.args[arg][0])
            
        #todo find a less assbackwards way of updating class with dict
        self.opt = Opt(**odic)
        self.initialized = True

    def parse(self):
        """
            parser to handle arguments from main.py
            Example
            #!/bin/bash
            $ python3 main.py --datarootA ./images/original_A.png --datarootB ./images/original_B.png --name lion_cat --k_final 10

        """
        if not self.initialized:
            self.initialize()
        self.opt = self.parser.parse_args()

        str_ids = self.opt.gpu_ids.split(',')
        self.opt.gpu_ids = []
        for str_id in str_ids:
            _id = int(str_id)
            if _id >= 0:
                self.opt.gpu_ids.append(_id)

        # set gpu ids
        if self.opt.gpu_ids:
            torch.cuda.set_device(self.opt.gpu_ids[0])

        args = vars(self.opt)

        print('------------ Options -------------')
        for k, v in sorted(args.items()):
            print('%s: %s' % (str(k), str(v)))
        print('-------------- End ----------------')

        # save to the disk
        expr_dir = os.path.join(self.opt.results_dir, self.opt.name)
        util.mkdirs(expr_dir)
        file_name = os.path.join(expr_dir, 'opt.txt')
        with open(file_name, 'wt') as opt_file:
            opt_file.write('------------ Options -------------\n')
            for k, v in sorted(args.items()):
                opt_file.write('%s: %s\n' % (str(k), str(v)))
            opt_file.write('-------------- End ----------------\n')
        return self.opt
