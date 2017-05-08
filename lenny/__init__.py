"""
Copyright (c) 2017 davidsluo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Credit to http://textsmili.es/ for lenny face symbols.
import random

mouths = [
    'v', 'ᴥ', 'ᗝ', 'Ѡ', 'ᗜ', 'Ꮂ', 'ᨓ', 'ᨎ', 'ヮ', '╭͜ʖ╮', ' ͟ل͜', ' ͜ʖ', ' ͟ʖ', ' ʖ̯', 'ω', ' ³', ' ε ', '﹏', '□', 'ل͜',
    '‿', '╭╮', '‿‿', '▾', '‸', 'Д', '∀', '!', '人', '.', 'ロ', '_', '෴', 'ꔢ', 'ѽ', 'ഌ', '⏠', '⏏', '⍊', '⍘', 'ツ', '益',
    '╭∩╮', 'Ĺ̯', '◡', ' ͜つ', '◞ ', 'ヘ'
]
eyes = [
    ('⌐■', '■'),
    (' ͠°', ' °'),
    ('⇀', '↼'),
    ('´• ', ' •`'),
    ('´', '`'),
    ('`', '´'),
    ('ó', 'ò'),
    ('ò', 'ó'),
    ('⸌', '⸍'),
    ('<', '>'),
    ('Ƹ̵̡', 'Ʒ'),
    ('ᗒ', 'ᗕ'),
    ('⟃', '⟄'),
    ('⪧', '⪦'),
    ('⪦', '⪧'),
    ('⪩', '⪨'),
    ('⪨', '⪩'),
    ('⪰', '⪯'),
    ('⫑', '⫒'),
    ('⨴', '⨵'),
    ('⩿', '⪀'),
    ('⩾', '⩽'),
    ('⩺', '⩹'),
    ('⩹', '⩺'),
    ('◥▶', '◀◤'),
    ('◍', '◎'),
    ('/͠-', ' ͝-\\'),
    ('⌣', '⌣”'),
    (' ͡⎚', ' ͡⎚'),
    '≋', '૦ઁ', '  ͯ', '  ͌', 'ꗞ', 'ꔸ', '꘠', 'ꖘ', '܍', 'ළ', '◉', '☉', '・', '▰', 'ᵔ', ' ﾟ', '□', '☼', '*', '`', '⚆', '⊜',
    '>', '❍', '￣', '─', '✿', '•', 'T', '^', 'ⱺ', '@', 'ȍ', '  ', '  ', 'x', '-', '$', 'Ȍ', 'ʘ', 'Ꝋ', '', '',
    '⸟', '๏', 'ⴲ', '■', ' ﾟ', '◕', '◔', '✧', '■', '♥', ' ͡°', '¬', ' º ', '⨶', '⨱', '⏓', '⏒', '⍜', '⍤', 'ᚖ', 'ᴗ', 'ಠ',
    'σ', '☯', 'の', '￢ ', 'э'
]
ears = [
    ('q', 'p'),
    ('ʢ', 'ʡ'),
    ('⸮', '?'),
    ('ʕ', 'ʔ'),
    ('ᖗ', 'ᖘ'),
    ('ᕦ', 'ᕥ'),
    ('ᕦ(', ')ᕥ'),
    ('ᕙ(', ')ᕗ'),
    ('ᘳ', 'ᘰ'),
    ('ᕮ', 'ᕭ'),
    ('ᕳ', 'ᕲ'),
    ('(', ')'),
    ('[', ']'),
    ('¯\\_', '_/¯'),
    ('୧', '୨'),
    ('୨', '୧'),
    ('⤜(', ')⤏'),
    ('☞', '☞'),
    ('(╭☞', ')╭☞'),
    ('ᑫ', 'ᑷ'),
    ('ᑴ', 'ᑷ'),
    ('ヽ(', ')ﾉ'),
    ('\\(', ')/'),
    ('乁(', ')ㄏ'),
    ('└[', ']┘'),
    ('(づ', ')づ'),
    ('(ง', ')ง'),
    ('⎝', '⎠'),
    ('ლ(', 'ლ)'),
    ('ᕕ(', ')ᕗ'),
    ('(∩', ')⊃━☆ﾟ.*'),
    ('【', '】'),
    ('﴾', '﴿'),
    ('(╯', '）╯︵ ┻━┻'),
    '|'
]


def lenny():
    mouth = random.choice(mouths)
    eyes_ = random.choice(eyes)
    ears_ = random.choice(ears)

    if isinstance(eyes_, tuple):
        left_eye, right_eye = eyes_
    else:
        left_eye = right_eye = eyes_

    if isinstance(ears_, tuple):
        left_ear, right_ear = ears_
    else:
        left_ear = right_ear = ears_

    face = '{0}{1}{2}{3}{4}'

    return face.format(left_ear, left_eye, mouth, right_eye, right_ear)
