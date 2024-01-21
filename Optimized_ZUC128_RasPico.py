"""
Copyright (c) 2024 Toshihiko Watanabe
Released under the MIT License
https://github.com/kwdlab/2403-Watanabe.Toshihiko/blob/kuwakado.hidenori/LICENSE
Reference Program: https://blog.csdn.net/weixin_44189363/article/details/110662381
"""

import time
from machine import I2C, Pin
from I2C_LCD import I2CLcd

i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
devices = i2c.scan()

S0=[[0x3e, 0x72, 0x5b, 0x47, 0xca, 0xe0, 0x00, 0x33, 0x04, 0xd1, 0x54, 0x98, 0x09, 0xb9, 0x6d, 0xcb], [0x7b, 0x1b, 0xf9, 0x32, 0xaf, 0x9d, 0x6a, 0xa5, 0xb8, 0x2d, 0xfc, 0x1d, 0x08, 0x53, 0x03, 0x90], [0x4d, 0x4e, 0x84, 0x99, 0xe4, 0xce, 0xd9, 0x91, 0xdd, 0xb6, 0x85, 0x48, 0x8b, 0x29, 0x6e, 0xac], [0xcd, 0xc1, 0xf8, 0x1e, 0x73, 0x43, 0x69, 0xc6, 0xb5, 0xbd, 0xfd, 0x39, 0x63, 0x20, 0xd4, 0x38], [0x76, 0x7d, 0xb2, 0xa7, 0xcf, 0xed, 0x57, 0xc5, 0xf3, 0x2c, 0xbb, 0x14, 0x21, 0x06, 0x55, 0x9b], [0xe3, 0xef, 0x5e, 0x31, 0x4f, 0x7f, 0x5a, 0xa4, 0x0d, 0x82, 0x51, 0x49, 0x5f, 0xba, 0x58, 0x1c], [0x4a, 0x16, 0xd5, 0x17, 0xa8, 0x92, 0x24, 0x1f, 0x8c, 0xff, 0xd8, 0xae, 0x2e, 0x01, 0xd3, 0xad], [0x3b, 0x4b, 0xda, 0x46, 0xeb, 0xc9, 0xde, 0x9a, 0x8f, 0x87, 0xd7, 0x3a, 0x80, 0x6f, 0x2f, 0xc8], [0xb1, 0xb4, 0x37, 0xf7, 0x0a, 0x22, 0x13, 0x28, 0x7c, 0xcc, 0x3c, 0x89, 0xc7, 0xc3, 0x96, 0x56], [0x07, 0xbf, 0x7e, 0xf0, 0x0b, 0x2b, 0x97, 0x52, 0x35, 0x41, 0x79, 0x61, 0xa6, 0x4c, 0x10, 0xfe], [0xbc, 0x26, 0x95, 0x88, 0x8a, 0xb0, 0xa3, 0xfb, 0xc0, 0x18, 0x94, 0xf2, 0xe1, 0xe5, 0xe9, 0x5d], [0xd0, 0xdc, 0x11, 0x66, 0x64, 0x5c, 0xec, 0x59, 0x42, 0x75, 0x12, 0xf5, 0x74, 0x9c, 0xaa, 0x23], [0x0e, 0x86, 0xab, 0xbe, 0x2a, 0x02, 0xe7, 0x67, 0xe6, 0x44, 0xa2, 0x6c, 0xc2, 0x93, 0x9f, 0xf1], [0xf6, 0xfa, 0x36, 0xd2, 0x50, 0x68, 0x9e, 0x62, 0x71, 0x15, 0x3d, 0xd6, 0x40, 0xc4, 0xe2, 0x0f], [0x8e, 0x83, 0x77, 0x6b, 0x25, 0x05, 0x3f, 0x0c, 0x30, 0xea, 0x70, 0xb7, 0xa1, 0xe8, 0xa9, 0x65], [0x8d, 0x27, 0x1a, 0xdb, 0x81, 0xb3, 0xa0, 0xf4, 0x45, 0x7a, 0x19, 0xdf, 0xee, 0x78, 0x34, 0x60]]
S1=[[0x55, 0xc2, 0x63, 0x71, 0x3b, 0xc8, 0x47, 0x86, 0x9f, 0x3c, 0xda, 0x5b, 0x29, 0xaa, 0xfd, 0x77], [0x8c, 0xc5, 0x94, 0x0c, 0xa6, 0x1a, 0x13, 0x00, 0xe3, 0xa8, 0x16, 0x72, 0x40, 0xf9, 0xf8, 0x42], [0x44, 0x26, 0x68, 0x96, 0x81, 0xd9, 0x45, 0x3e, 0x10, 0x76, 0xc6, 0xa7, 0x8b, 0x39, 0x43, 0xe1], [0x3a, 0xb5, 0x56, 0x2a, 0xc0, 0x6d, 0xb3, 0x05, 0x22, 0x66, 0xbf, 0xdc, 0x0b, 0xfa, 0x62, 0x48], [0xdd, 0x20, 0x11, 0x06, 0x36, 0xc9, 0xc1, 0xcf, 0xf6, 0x27, 0x52, 0xbb, 0x69, 0xf5, 0xd4, 0x87], [0x7f, 0x84, 0x4c, 0xd2, 0x9c, 0x57, 0xa4, 0xbc, 0x4f, 0x9a, 0xdf, 0xfe, 0xd6, 0x8d, 0x7a, 0xeb], [0x2b, 0x53, 0xd8, 0x5c, 0xa1, 0x14, 0x17, 0xfb, 0x23, 0xd5, 0x7d, 0x30, 0x67, 0x73, 0x08, 0x09], [0xee, 0xb7, 0x70, 0x3f, 0x61, 0xb2, 0x19, 0x8e, 0x4e, 0xe5, 0x4b, 0x93, 0x8f, 0x5d, 0xdb, 0xa9], [0xad, 0xf1, 0xae, 0x2e, 0xcb, 0x0d, 0xfc, 0xf4, 0x2d, 0x46, 0x6e, 0x1d, 0x97, 0xe8, 0xd1, 0xe9], [0x4d, 0x37, 0xa5, 0x75, 0x5e, 0x83, 0x9e, 0xab, 0x82, 0x9d, 0xb9, 0x1c, 0xe0, 0xcd, 0x49, 0x89], [0x01, 0xb6, 0xbd, 0x58, 0x24, 0xa2, 0x5f, 0x38, 0x78, 0x99, 0x15, 0x90, 0x50, 0xb8, 0x95, 0xe4], [0xd0, 0x91, 0xc7, 0xce, 0xed, 0x0f, 0xb4, 0x6f, 0xa0, 0xcc, 0xf0, 0x02, 0x4a, 0x79, 0xc3, 0xde], [0xa3, 0xef, 0xea, 0x51, 0xe6, 0x6b, 0x18, 0xec, 0x1b, 0x2c, 0x80, 0xf7, 0x74, 0xe7, 0xff, 0x21], [0x5a, 0x6a, 0x54, 0x1e, 0x41, 0x31, 0x92, 0x35, 0xc4, 0x33, 0x07, 0x0a, 0xba, 0x7e, 0x0e, 0x34], [0x88, 0xb1, 0x98, 0x7c, 0xf3, 0x3d, 0x60, 0x6c, 0x7b, 0xca, 0xd3, 0x1f, 0x32, 0x65, 0x04, 0x28], [0x64, 0xbe, 0x85, 0x9b, 0x2f, 0x59, 0x8a, 0xd7, 0xb0, 0x25, 0xac, 0xaf, 0x12, 0x03, 0xe2, 0xf2]]
D=[ 0x44d7, 0x26bc, 0x626b, 0x135e, 0x5789, 0x35e2, 0x7135, 0x09af, 0x4d78, 0x2f13, 0x6bc4, 0x1af1, 0x5e26, 0x3c4d, 0x789a, 0x47ac]

S=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Key_result=[]
keylen=20
X=[0,0,0,0]
R1=0
R2=0
W=0

test_times = 1000

def BitReconstruction():
    X[0]=add2(S[15],S[14])
    X[1]=add(S[11],S[9])
    X[2]=add(S[7],S[5])
    X[3]=add(S[2],S[0])

def LFSRWithInitMode(u):
    v=(32768*S[15]+131072*S[13]+2097152*S[10]+1048576*S[4]+(257)*S[0])%(2147483647)
    S.append((v+u)%2147483647)
    if S[16] == 0:
        S[16]=2147483647
    S.pop(0)

def LFSRWithWorkMode():
    S.append((32768 * S[15] + 131072 * S[13] + 2097152 * S[10] + 1048576 * S[4] + (257) * S[0]) % (2147483647))
    if S[16] == 0:
        S[16] = 2147483647
    S.pop(0)

def F(X0,X1,X2):
    global R1, R2, W
    W=mod32(X0 ^ R1, R2)
    W1=mod32 (R1,X1)
    W2=R2 ^ X2
    R1=S_(L1(((W1<<16) | (W2>>16)) & 0xffffffff))
    R2=S_(L2(((W2<<16) | (W1>>16)) & 0xffffffff))

def L1(X):
    return X ^ rot(X,2) ^ rot(X,10)^ rot(X,18) ^ rot (X,24) & 0xffffffff
def L2(X):
    return X ^ rot(X,8) ^ rot(X,14) ^ rot(X,22) ^ rot(X,30) & 0xffffffff
def S_(X):
    bit8=[0,0,0,0]
    result=[0,0,0,0]
    bit8[0]=X>>24
    bit8[1]=(X>>16)&0xff
    bit8[2]=(X>>8)&0xff
    bit8[3]=X&0xff
    row = bit8[0] >> 4
    nuw = bit8[0] & 0xf
    result[0] = S0[row][nuw]
    ans = (result[0] << 24) | (result[1] << 16) | (result[2] << 8) | result[3]
    row = bit8[1] >> 4
    nuw = bit8[1] & 0xf
    result[1] = S1[row][nuw]
    ans = (result[0] << 24) | (result[1] << 16) | (result[2] << 8) | result[3]
    row = bit8[2] >> 4
    nuw = bit8[2] & 0xf
    result[2] = S0[row][nuw]
    ans = (result[0] << 24) | (result[1] << 16) | (result[2] << 8) | result[3]
    row = bit8[3] >> 4
    nuw = bit8[3] & 0xf
    result[3] = S1[row][nuw]
    ans = (result[0] << 24) | (result[1] << 16) | (result[2] << 8) | result[3]

    return ans

def rot(X,i):
    return ((X<<i)& 0xffffffff)|(X>>(32-i))
def mod32 (R,X):
    return (R + X)&0xffffffff
def H(X):
    bits=(X>>15) & 0xffff
    return bits
def L(X):
    bits = X & 0xffff
    return bits

def add (W1, W2):
    W1l=L(W1) << 16 
    W2h=H(W2)
    all=W1l|W2h
    return all

def add2 (W1, W2):
    W1h = H(W1) << 16
    W2l = L(W2)
    all= W1h | W2l
    return all

def init(key,iv):
    global R1, R2, W,S
    for i in range(16):
        S[i] = (key[i] << 23) | (D[i] << 8) | iv[i]
    R1=0
    R2=0
    for i in range(32):
        BitReconstruction()
        F(X[0], X[1], X[2])
        LFSRWithInitMode (W >> 1)

def calc():
    BitReconstruction()
    F(X[0], X[1], X[2])
    LFSRWithWorkMode()
    for i in range(keylen):
        BitReconstruction()
        F(X[0], X[1], X[2])
        Key_result.append(W^X[3])
        LFSRWithWorkMode()

key=[0x3d,0x4c,0x4b,0xe9,0x6a,0x82,0xfd,0xae,0xb5,0x8f,0x64,0x1d,0xb1,0x7b,0x45,0x5b]
iv=[0x84,0x31,0x9a,0xa8,0xde,0x69,0x15,0xca,0x1f,0x6b,0xda,0x6b,0xfb,0xd8,0xc7,0x66]  

try:
    if devices != []:
        lcd = I2CLcd(i2c, devices[0], 2, 16)
        
        start = time.ticks_us()
        for i in range(test_times):
            Key_result = []
            init(key, iv)
            calc()
        end = time.ticks_us()
        timer = end - start
        if_success = False

        Success_Key_Result = [0x14f1c272,0x3279c419,0x4b8ea41d,0xcc80863,0xd28062e1,0xe71d3dda,0xe3c4d158,0xa7f067ac,0x94935056,0x8ee5c63d,0xf5a0cec3,0xd33da5a7,0x7de892ac,0xe8fd9b12,0xfb625a84,0xf15a5323,0xd93d3995,0x9a485a71,0xdab8ecd1,0x9d9b3e2e]            

        if Key_result == Success_Key_Result:
            if_success = True

        if if_success:
            str = "Success"
        else:
            str = "Failed"
        lcd.move_to(0, 0)
        lcd.putstr("Time:%d" %(timer))
        lcd.putstr(str)

    else:
        print("No address found")

except:
    pass