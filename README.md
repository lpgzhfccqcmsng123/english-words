# english-words

命令行背单词工具，Python 写的，数据存本地 JSON。无第三方依赖。

## 功能

- 加词：输入单词和释义，已存在的词不会覆盖
- 查词：输入单词显示释义，词不存在会给出提示
- 列全部：显示词库里的所有词条

## 运行

需要 Python 3.10 以上。

```bash
git clone https://github.com/lpgzhfccqcmsng123/english-words.git
cd english-words
python main.py
```

## 数据格式

`words.json` 是一个字典，键是单词，值是释义：

```json
{
  "apple": "苹果",
  "banana": "香蕉"
}
```

想批量导入，直接编辑这个文件。

## 待实现

- 删词
- 抽考（随机抽词，检验记忆）
- 记录抽考答错的词
