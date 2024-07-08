# -*- coding: UTF-8 -*
'''
Created on 2020-07-10
'''

import time
import array
import usb.util

devs = usb.core.find(find_all=True)

# TSPL
tmpl = '''
CLS
SIZE 60 mm,40 mm
GAP 2 mm,0 mm
SPEED 4
TEXT 10,30,"TSS24.BF2",0,1,1,"卡罗拉 A|红"
BARCODE 10,80,"128",100,1,0,3,1,"SP0123456"
TEXT 10,230,"TSS24.BF2",0,1,1,"小唐鲜花"
TEXT 180,230,"TSS24.BF2",0,1,1,"中熟"
TEXT 250,230,"TSS24.BF2",0,1,1,"C012"
TEXT 380,230,"TSS24.BF2",0,1,1,"P9"
PRINT 1
'''

# CPCL
# tmpl = '''! 0 200 200 472 1
# TEXT 55 18 396 40 aaa
# TEXT 55 18 396 88 BBB
# B QR 176 60 M 1 U 6
# ENDQR
# BARCODE-TEXT 24 0 5
# BARCODE 128 1 1 50 216 250 {{obj.barcode}}
# BARCODE-TEXT OFF
# FORM
# PRINT
# '''

bts = tmpl.encode('gbk')
for d in devs:
    if d.idVendor not in [0x0055, 0x03f0, 0x2a5c, 0x0550, 0x067b, 0x10c4, 0x6868, 0x0471, 0x324f, 0x3533]:
        continue
    print(d)
    aci = (0, 1)
    itf = d.get_active_configuration().interfaces()[0]
    eps = itf.endpoints()
    oep = eps[0]
    iep = eps[1]

    dl = d.write(endpoint=oep, data=bts, timeout=1000 * 60 * 5)
    print('write', dl)
    time.sleep(4)
