# Template-Based NER
Replication/Reproduction Source Code For
 [Template-Based Named Entity Recognition Using BART](https://aclanthology.org/2021.findings-acl.161.pdf)

# Training

Training Conll2003 ```train.py```

Inference Conll2003 ```inference.py```

Training MIT Restaurant w/o transfer learning ```train_restaurant_src.py```

Inference MIT Restaurant w/o transfer learning ```inference_restaurant_src.py```

Training MIT Movie w/o transfer learning ```train_movie_src.py```

Inference MIT Movie w/o transfer learning ```inference_movie_src.py```

Training MIT Restaurant with transfer learning Conll2003 base ```train_restaurant.py```

Inference MIT Restaurant with transfer learning Conll2003 base ```inference_restaurant.py```

Training MIT Movie with transfer learning Conll2003 base ```train_movie.py```

Inference MIT Movie with transfer learning Conll2003 base ```inference_movie.py```

# Corpus

Conll2003 ```conll2003```

MIT Restaurant Corpus (training unnamed entity not adjusted to 1.25x named entity, but all) ```mit-restaurant```

MIT Movie Corpus (training unnamed entity not adjusted to 1.25x named entity, but all) ```mit-movie```

```txttocsv.py``` was used to make the MIT Restaurant and MIT Movie training corpus in this repository.

# Contact

If you have any questions, please feel free to contact Leyang Cui
(<cuileyang@westlake.edu.cn>).

# Citation

```
@inproceedings{cui-etal-2021-template,
    title = "Template-Based Named Entity Recognition Using {BART}",
    author = "Cui, Leyang  and
      Wu, Yu  and
      Liu, Jian  and
      Yang, Sen  and
      Zhang, Yue",
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-acl.161",
    doi = "10.18653/v1/2021.findings-acl.161",
    pages = "1835--1845",
}
```
