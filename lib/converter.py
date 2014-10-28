# -*- coding: utf-8 -*-

import re


def romaji_to_kana(romaji):
    h = {
        'a': 'あ', 'i': 'い', 'u': 'う', 'e':'え', 'o': 'お',
        'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ',
        'ga': 'が', 'gi': 'ぎ', 'gu': 'ぐ', 'ge': 'げ', 'go': 'ご',
        'sa': 'さ', 'shi': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ',
        'za': 'ざ', 'ji': 'じ', 'zu': 'ず', 'ze': 'ぜ', 'zo': 'ぞ',
        'ta': 'た', 'chi': 'ち', 'tsu': 'つ', 'te': 'て', 'to': 'と',
        'da': 'だ', 'dzi': 'ぢ', 'dzu': 'づ', 'de': 'で', 'do': 'ど',
        'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
        'ha': 'は', 'hi': 'ひ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ',
        'ba': 'ば', 'bi': 'び', 'bu': 'ぶ', 'be': 'べ', 'bo': 'ぼ',
        'pa': 'ぱ', 'pi': 'ぴ', 'pu': 'ぷ', 'pe': 'ぺ', 'po': 'ぽ',
        'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も',
        'ya': 'や', 'yu': 'ゆ', 'yo': 'よ',
        'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ',
        'wa': 'わ', 'wo': 'を', 'n': 'ん', "n'": 'ん',
        'sha': 'しゃ', 'shu': 'しゅ', 'sho': 'しょ',
        'ja': 'じゃ', 'ju': 'じゅ', 'jo': 'じょ',
        'cha': 'ちゃ', 'chu': 'ちゅ', 'cho': 'ちょ'
    }

    hy = {
        'a': 'ゃ', 'u': 'ゅ', 'o': 'ょ'
    }

    tokens = tokenize(romaji)
    result = ''
    for t in tokens:
        result += token_to_kana(t, h, hy)
    return result

def tokenize(s):
    return re.findall("(?![aeiou])[a-z][aeiou]|(?![aeiou])[a-z](?![aeiou])[a-z][aeiou]|[aeiou]|n'|n", s)

def token_to_kana(token, source, y):
    if token in source:
        return source[token]
    else:
        if token[0] == token[1]:
            return 'っ%s' % (source[token[1:]],)
        elif token[1] == 'y':
            return '%s%s' % (source[token[0] + 'i'], y[token[2]])

if __name__ == '__main__':
    print romaji_to_kana('taberu')
    print romaji_to_kana('kakkoii')
    print romaji_to_kana('shunchan')
    print romaji_to_kana("ten'in")
    print romaji_to_kana('wakaranai')
    print romaji_to_kana('urayamashii')