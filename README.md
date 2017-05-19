# favaro_text_classification

* text classification test
* this project use python3

## keras example

official example from keras

## my test

under my_notebooks

## notes

```
文本的预处理，看起来处理方式都是先把每个词变成数字，最高频的是1，第二高频的是2，一句话经过分词变成底下的类似向量：

[ [1, 2, 2, 8, 43, 10, 447, 5, 25, 207, 270, 5, 2, 111, 16, 369, 186, 90, 67, 7, 89, 5, 19, 102, 6, 19, 124, 15] ]

但是每句话的这个向量长度是不一致的。

然后有两种方法，在keras中，可以用 tokenizer.sequences_to_matrix 把向量转换成变成定长的向量，和sklearn中的vectorizer一样

另一种方法是先padding，例如在前面补0，都变成定长向量。

然后用 embedding 把向量变成矩阵， 然后接卷积层。:sweat_smile: ( 又可以cnn装逼了 :smirk: :smirk: :smirk: )

关于 embedding 层的用法 http://keras-cn.readthedocs.io/en/latest/layers/embedding_layer/
```

reuters那个数据集，xgb很慢，rf很快，和mlp比较，最后结果差不多。:sweat_smile: