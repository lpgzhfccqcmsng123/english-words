# -*- coding: utf-8 -*-
"""
单词本 · 命令行版

一个在终端里用的背单词工具，数据存在同目录的 words.json。
支持加词、查词、列全部三个功能，删词和抽考待实现。
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
    word = input()
    if word in words:
        del words[word]
        print(f"已删除 {word}")
        return True
    else:
        print("没有这个词")
        return False


def list_all(words):
    """打印「共 N 个词」，再逐行打印 单词: 释义。"""
    print(f"共 {len(words)} 个词")
    for word,meaning in words.items():
        print(f"{word}: {meaning}")

def quiz(words):
    """从字典里随机抽一个词，打印单词，让用户输释义，对错都给提示。
    词表为空时打印「单词本是空的」。"""
    if not words:
        print("单词本是空的")
        return
    
    word = random.choice(list(words.keys()))
    print(f"{word}的意思是？")
    answer = input()
    if answer == words[word]:
        print("回答正确")
        return True
    else:
        print(f"回答错误，正确答案应该是{words[word]}")
        return False


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
            delete_word(words)
            save_words(words)
        elif choice == "4": 
            list_all(words)
        elif choice == "5": 
            quiz(words)
        else: 
            print("没有这个选项")
main()




