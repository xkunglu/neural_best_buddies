
import os
import numpy as np
from .models import vgg19_model
from .algorithms import neural_best_buddies as NBBs
from .util import util, MLS


def run_files(opt):

    vgg19 = vgg19_model.define_Vgg19(opt)
    if opt.results_dir is None:
        save_dir = None
    else:
        save_dir = os.path.join(opt.results_dir, opt.name)

    nbbs = NBBs.sparse_semantic_correspondence(vgg19, opt.gpu_ids, opt.tau, opt.border_size,
                                               save_dir, opt.k_per_level, opt.k_final, opt.fast)

    A = util.read_image(opt.datarootA, opt.imageSize)
    B = util.read_image(opt.datarootB, opt.imageSize)

    points = nbbs.run(A, B)

    if nbbs.save_dir:
        mls = MLS.MLS(v_class=np.int32)
        mls.run_MLS_in_folder(root_folder=save_dir)

        print('NBB: files saved to ', os.path.abspath(save_dir))

    # nbbs.intermediate_correspondences
    # nbbs.correspondences
    # nbbs.patch_size_list[L-1]
    # nbbs.self.search_box_radius_list[L-1]
    # nbbs.draw_radius[L-1]
    return nbbs
