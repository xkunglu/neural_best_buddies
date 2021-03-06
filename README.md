# Neural Best-Buddies in PyTorch

This is a fork of Kfir Aberman and Mingyi Shi's Neural Best Buddies repo. 
Contains only minor changes. Original can be found in 
https://github.com/kfiraberman/neural_best_buddies.

changes from original repo
--------------------------
* force convert images to size 224x224; larger images fail in original depot. possibly a pytorch issue with torchvision.transforms.Scale and .Resizw( ?) need to investigate why

* added pip installer:
  ```bash
  cd neural_best_buddies
  pip install .

  ```
* added access from python.
  TODO file loading and saving as options; enable numpy array io
  ```python
  import nbb
  from nbb.options import Options
  datarootA = 'images/original_A.png'
  datarootA = 'images/original_B.png'
  name='Lion_Cat'
  k_final=20
  results_dir = '../results'
  o = Options()
  o.setoptions(datarootA, datarootA, name=name, k_final=k_final, results_dir=results_dir)
  nbb.run(o.opt)
  ```
* added option to not save images; output images as numpy array
* added a jupyter notebook to visualize changes

-xk


Below the line is information included in original repo. 
-----------------
The code was written by [Kfir Aberman](https://kfiraberman.github.io/) and supported by [Mingyi Shi](https://rubbly.cn/).

**Neural Best-Buddies: [Project](http://fve.bfa.edu.cn/recap/nbbs/) |  [Paper](https://arxiv.org/pdf/1805.04140.pdf)**
<img src="./images/teaser.jpg" width="800" />

If you use this code for your research, please cite:

Neural Best-Buddies: Sparse Cross-Domain Correspondence
[Kfir Aberman](https://kfiraberman.github.io/), [Jing Liao](https://liaojing.github.io/html/), [Mingyi Shi](https://rubbly.cn/), [Dani Lischinski](http://danix3d.droppages.com/), [Baoquan Chen](http://www.cs.sdu.edu.cn/~baoquan/), [Daniel Cohen-Or](https://www.cs.tau.ac.il/~dcor/), SIGGRAPH 2018.

## Prerequisites
- Linux or macOS
- Python 2 or 3
- CPU or NVIDIA GPU + CUDA CuDNN

### Run

- Run the algorithm (demo example)
```bash
#!./script.sh
python3 main.py --datarootA ./images/original_A.png --datarootB ./images/original_B.png --name lion_cat --k_final 10
```
The option `--k_final` dictates the final number of returned points. The results will be saved at `./results/`. Use `--results_dir {directory_path_to_save_result}` to specify the results directory.

### Output
Sparse correspondence:
- correspondence_A.txt, correspondence_B.txt
- correspondence_A_top_k.txt, correspondence_B_top_k.txt

Dense correspondence (densifying based on [MLS](http://faculty.cse.tamu.edu/schaefer/research/mls.pdf)):
-  BtoA.npy, AtoB.npy

Warped images (aligned to their middle geometry):
- warp_AtoM.png, warp_BtoM.png

### Tips
- If you are running the algorithm on a bunch of pairs, we recommend to stop it at the second layer to reduce runtime (comes at the expense of accuracy), use the option `--fast`.

## Citation
If you use this code for your research, please cite our papers.
```
@article{aberman2018neural,
  author = {Kfir, Aberman and Jing, Liao and Mingyi, Shi and Dani, Lischinski and Baoquan, Chen and Daniel, Cohen-Or},
  title = {Neural Best-Buddies: Sparse Cross-Domain Correspondence},
  journal = {ACM Transactions on Graphics (TOG)},
  volume = {37},
  number = {4},
  pages = {69},
  year = {2018},
  publisher = {ACM}
}

```
