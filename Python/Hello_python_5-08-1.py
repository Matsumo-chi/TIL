# -*- coding: utf-8 -*-
# 画像用辞書
items_img = {
    "剣" : "http://paiza.jp/learning/images/sword.png",
    "盾" : "http://paiza.jp/learning/images/shield.png",
    "回復薬" : "http://paiza.jp/learning/images/potion.png",
    "クリスタル" : "http://paiza.jp/learning/images/crystal.png"
}

# アイテムの並び順リスト
items_order = ["剣", "盾", "回復薬", "クリスタル"]

# ここから下を記述しよう
for items in items_order:
     print("<img src='" + items_img[items] + "'>")
     print("<br>")


