# -*- coding: utf-8 -*-
"""
单词本 · 命令行版（骨架，函数体要你自己填）

【这个文件要做什么】
一个能在终端跑的背单词工具，数据存在 words.json。
七个函数 + 一个菜单循环，函数名和签名已经给好，函数体是空的。

【要求】
1. 只填函数体，不许改函数名、不许改参数（改了 main 里调不通）
2. load_words / save_words 直接从 8-04 的代码里搬，改成函数
3. add_word 遇到已存在的词要提示，不要覆盖原释义
4. 查词、删词遇到不存在的词要提示，不能报错退出
5. 所有 open 都带 encoding="utf-8"
6. main() 是一个 while True 菜单，输入 0 退出

【输出/验收】
（第一次运行，words.json 不存在）

=== 单词本 ===
1. 加词  2. 查词  3. 删词  4. 列全部  5. 抽考  0. 退出
请选择: 1
单词: apple
释义: 苹果
已添加 apple

请选择: 4
共 1 个词
apple: 苹果

请选择: 2
单词: apple
苹果

请选择: 2
单词: banan
没有这个词

请选择: 0
再见

【注意】
三个坑提前说，踩了就是这三个：
- json.dump 写在 with 块外面 → I/O operation on closed file
- 用 "a" 模式写 JSON → 第二次运行 json.load 报 Extra data
- input 写成 input("单词: ") 会让终端多打一行，输出对不上就重跑一次看
"""

import json
import random

DATA_FILE = "words.json"


def load_words():
    """读 DATA_FILE，返回字典。文件不存在返回 {}。"""
    try:
        with open(DATA_FILE,"r",encoding = "UTF-8")as e:
            return json.load(e)
    except Exception as f:
        return{}


def save_words(words):
    """把字典写回 DATA_FILE。ensure_ascii=False, indent=2。"""
    with open(DATA_FILE,"w",encoding="UTF-8")as f:
        json.dump(words,f,ensure_ascii=False, indent=2)


def add_word(words):
    word = input()
    meaning = input()

    if word == "" or meaning == "":
        print("单词和释义不能为空")
        return False

    if word in words:
        print(f"{word} 已存在")
        return False

    words[word] = meaning
    print(f"已添加 {word}")
    return True




def find_word(words):
    """输入单词，打印释义。不存在打印「没有这个词」。"""
    word = input()
    if word in words:
        print(words[word])
    else:
        print("没有这个词")


def delete_word(words):
    """输入单词，删除并提示。不存在打印「没有这个词」。"""
    pass


def list_all(words):
    """打印「共 N 个词」，再逐行打印 单词: 释义。"""
    print(f"共 {len(words)} 个词")
    for word,meaning in words.items():
        print(f"{word}: {meaning}")

def quiz(words):
    """从字典里随机抽一个词，打印单词，让用户输释义，对错都给提示。
    词表为空时打印「单词本是空的」。"""
    pass


def main():
    """菜单循环。
    while True:
        打印菜单
        choice = input("请选择: ")
        按 choice 分发到上面的函数
        0 就打印「再见」然后 break
    """
    words = load_words() 
    while True:
        print("=== 单词本 ===")
        print("1. 加词  2. 查词  3. 删词  4. 列全部  5. 抽考  0. 退出")
        choice = input("请选择: ")

        if choice == "0":
            print("再见")
            break
        elif choice == "1":
            add_word(words) 
            save_words(words)
        elif choice == "2":
            find_word(words)
        elif choice == "3":
            print("未实现")
        elif choice == "4": 
            list_all(words)
        elif choice == "5": 
            print("未实现")
        else: 
            print("没有这个选项")
main()




