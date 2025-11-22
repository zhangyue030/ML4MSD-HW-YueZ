# ML4MSD - Homework 5
*Created By*: Prof. Peter Schindler<br>
*Due*: Monday, 11/24/2025, 11:59 pm

## Overview

The fifth (and last) homework covers three major topics: deep learning, computational materials science, and large-language models. As this is a larger homework, you will be given double the amount of time of a regular homework and it will **count the same as two homework assignments**.

## Generative AI Usage and Setting up and Submitting Your Homework Submission

Same as homework 1.

## Assignments

### Assignment 0-s, Group Project [Splitter]

If you are a **splitter**, please check the [Google Sheets](https://docs.google.com/spreadsheets/d/1t5ng06gqtRehIXX5sPPvjQBLRUJYs8R08H5M7KeGByw/) for your assigned dataset. Follow these steps:
1. Load the dataset with `MatMiner` (see lecture 12 notebook in week 7 folder). 
```Python
from matminer.datasets.dataset_retrieval import load_dataset
import pandas as pd
from MatFold import MatFold

df = load_dataset('YOUR_DATASET')
```
2. Create a dictionary with the pymatgen structures:
```Python
df['mat_index'] = ['mat{}'.format(i) for i in range(len(df))]
df = df[['mat_index', 'structure', 'TARGET']]  # update the TARGET column label for your dataset and double-check that the `structure` column exists
df['composition'] = df.structure.apply(lambda x: x.composition)  # add composition column for structure-based datasets
mat_struct_dict = {
    row['mat_index']: row['structure'].as_dict() for _, row in df.iterrows()
}
```
3. Initialize the `MatFol` class `mf = MatFold(df, mat_struct_dict)` (no need to do any featurization before this step).
4. Look at all these split statistics: 
- `composition` (or `comp`)
- `chemsys` (or `chemicalsystem`)
- `sgnum` (or `spacegroup`, `spacegroupnumber`)
- `pointgroup` (or `pg`, `pointgroupsymbol`, `pgsymbol`)
- `crystalsys` (or `crystalsystem`)
- `elements` (or `elems`)
- `periodictablerows` (or `ptrows`)
- `periodictablegroups` (or `ptgroups`)<br><br>
For example, for spacegroup number split statistics run: `print(mf.split_statistics("sgnum"))`.

5. Summarize all these split statistics and assess which ones could be used to generate a **70-20-10 train-validation-test split**. For example, if the split statistics reveals that there are only 2 categories for `periodictablerows` with 40% and 60% of the dataset, then a 70-20-10 split would not be possible.

### Assignment 0-m, Group Project [Modeler]

If you are **modeler**, then please test your two models on the *Explorer HPC* on a random train/test split (e.g., 90/10) on any MatMiner dataset.


### Assignment 1

Finalize the exercises from lecture 14 (see the [Google Colab Notebook](https://colab.research.google.com/drive/1X2gGwKcUdosUApa7osLjsCSN8Ofbs4Y6)), fill in the results in this [Google Sheets](https://colab.research.google.com/drive/1X2gGwKcUdosUApa7osLjsCSN8Ofbs4Y6), and briefly summarize the observations for your picked transition metal in 1-2 sentences.

### Assignment 2

Please, watch videos 1, 2, 3, 5, and 6 in this [YouTube Playlist](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi). Take **screenshots** of the illustrations that you find most helpful during these explanations and summarize why these specific screenshots were helpful to you in a few sentences.

### Assignment 3

Please, go through the following [Google Colab Notebook](https://colab.research.google.com/drive/1AI0nQbIV7R5Axe8SQz-yUdVh_jyQukNs) that covers a few exercises related to large-language models, similar to what was covered in lecture 16.

### Assignment 4

Please, read a few chapters of the [Understanding Deep Learning](https://udlbook.github.io/udlbook/) textbook to solidify a few of the topics we discussed during class. Biefly summarize what you learned in the process and which chapters seemed most useful to you.

### Assignment 5

Lastly, please go through the two exercises in lecture 17 (notebook in week 9 folder or this [Google Colab Notebook](https://colab.research.google.com/drive/1_ByBimOZhDFWdwMkn9_KCzADVL7p4uxT)). Fill in the results in this [Google Sheet](https://docs.google.com/spreadsheets/d/1xyZJE2nErCL4HIT6vFfMY9oFyOXoBfHyBRVZDDbI3cA/) and briefly summarize your results for the chosen material (exercise 17.1) and your chosen surface/molecule (exercise 17.2) in a few sentences.<br>
In exercise 17.2, you can also play around with the `taut` parameter in the `NVTBerendsen` thermostat while increasing the number of MD steps, to see if you can approach the target temperature of 300 K.

## Evaluation

I will grade your homework submission based on how I perceive your effort:
- 0%: Very little or no effort
- 50%: Basic/average effort (tried to make an effort)
- 100%: Effort is evident