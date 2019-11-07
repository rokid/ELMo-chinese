# ELMo-chinese

> Deep contextualized word representations for Chinese.

本仓库只是输出上下文无关的 word embedding。

## 依赖

- python3
- tensorflow >= 1.10
- jieba

## 使用方法

1. 准备数据，参考 data 和 vocab 目录，可用 `pre_data/vocab.py` 处理出词典（每个 data 文件不能太大，否则内存不够）
2. 训练模型 `train_elmo.py`
3. 输出模型 `dump_weights.py`
4. 把 `options.json` 里的 261 改成 262
5. 输出 word embedding 到 hdf5 文件 `usage_token.py`

## 实验结果

用可视化工具看合理，`textmatch` 任务提升 AUC 1-2。

### License

MIT
