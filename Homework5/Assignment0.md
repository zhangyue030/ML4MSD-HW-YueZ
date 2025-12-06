### composition: 
Suitable. There are many unique compositions, and each one represents a very small fraction (<1%) of the dataset. It is easy to form the 70-20-10 split.

### chemsys:  
Suitable. Similar to composition, there are many unique chemical systems with a very flat distribution (max < 1%). This allows for an easy and precise 70-20-10 split.

### sgnum (Space Group): 
Suitable. Although the distribution is somewhat skewed (the group P-3m1 holds ~25% of the data), there are enough distinct categories. The largest group fits comfortably into the 70% training set, and the remaining smaller groups can form the validation and test sets.

### pointgroup: 
Suitable. There are fewer categories compared to space groups, and the distribution is more top-heavy (largest group -3m is ~29%). However, a 70-20-10 split is still possible by placing the large groups in the training set and combining smaller groups for the test set.

### crystalsys: 
Not Suitable. There are only 6 categories. The groups are too large and "chunky" (e.g., Trigonal is 36%, Monoclinic is 20%). It is mathematically difficult to form a 10% test set, and splitting by crystal system would likely cause poor generalization (the model wouldn't learn the excluded crystal systems).

### elements: 
Suitable. The distribution shows several large groups corresponding to anions (e.g., O is ~20%, S is ~17%). While these chunks are too large for the 10% test set, they fit perfectly into the 20% validation set or the training set. The test set can be formed by combining smaller element groups.

### periodictablerows: 
Not Suitable. The categories overlap significantly (sum > 100%), meaning materials contain elements from multiple rows. Furthermore, the main categories are too large (e.g., Row 4 and Row 5 are ~50% each), making it impossible to isolate a 10% test set or 20% validation set.

### periodictablegroups:
Not Suitable. Similar to rows, the groups overlap significantly (sum >> 100%). Group 16 alone is present in ~63% of the data, and Group 17 in ~44%. These chunks are far too large to form a balanced validation or test set.
