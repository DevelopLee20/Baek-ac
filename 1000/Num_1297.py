'''
D, H, W
대각선 길이 D
높이 비율 H
너비 비율 W

Hh = Ww
h = Ww / H
(Ww / H)^2 + w^2 = D^2
W**2 * w**2 / H**2 + w**2 = D**2
W**2 * w**2 + w**2 * H**2 = D**2 * H**2
w  = ((D**2 * H**2) / (W**2 + H**2))**0.5

출력 h w
'''
D, H, W = map(int, input().split())
w = ((D**2 * H**2) / (W**2 + H**2))**0.5
h = W * w / H

print(int(w), int(h))
