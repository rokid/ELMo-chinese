### ELMo-chinese

Deep contextualized word representations 中文 汉语

只是输出 context-independent 的word embedding

### requirements

python3

tensorflow >= 1.10

jieba

### 使用方法

1, 准备数据，参考`data`文件夹和`vocab`文件夹，可用`pre_data`下的`vocab.py`处理出词典（每个data文件不要太大，否则内存不够）

2, 训练模型 `train_elmo.py`

3, 输出模型 `dump_weights.py`

4, 把`options.json`里的261改成262

5, 输出word embedding到hdf5文件 `usage_token.py`

### 实验结果

用可视化工具看合理

textmatch任务提升AUC 2-4

### License

MIT.
