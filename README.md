# USB-Printer-Descriptors
收集整理市面上常见的USB打印机描述符。

[TOC]

#### 佳博ZH-380

小票、标签打印机

##### 照片
![](imgs/佳博-ZH-380-1.JPG)
![](imgs/佳博-ZH-380-2.JPG)


##### 描述符

```plain
DEVICE ID 6868:0500 on Bus 020 Address 026 =================
 bLength                :   0x12 (18 bytes)
 bDescriptorType        :    0x1 Device
 bcdUSB                 :  0x200 USB 2.0
 bDeviceClass           :    0x0 Specified at interface
 bDeviceSubClass        :    0x0
 bDeviceProtocol        :    0x0
 bMaxPacketSize0        :   0x40 (64 bytes)
 idVendor               : 0x6868
 idProduct              : 0x0500
 bcdDevice              :  0x400 Device 4.0
 iManufacturer          :    0x1 Printer
 iProduct               :    0x2 Printer
 iSerialNumber          :    0x3 6A6958721237
 bNumConfigurations     :    0x1
  CONFIGURATION 1: 100 mA ==================================
   bLength              :    0x9 (9 bytes)
   bDescriptorType      :    0x2 Configuration
   wTotalLength         :   0x20 (32 bytes)
   bNumInterfaces       :    0x1
   bConfigurationValue  :    0x1
   iConfiguration       :    0x0 
   bmAttributes         :   0xc0 Self Powered
   bMaxPower            :   0x32 (100 mA)
    INTERFACE 0: Printer ===================================
     bLength            :    0x9 (9 bytes)
     bDescriptorType    :    0x4 Interface
     bInterfaceNumber   :    0x0
     bAlternateSetting  :    0x0
     bNumEndpoints      :    0x2
     bInterfaceClass    :    0x7 Printer
     bInterfaceSubClass :    0x1
     bInterfaceProtocol :    0x2
     iInterface         :    0x0 
      ENDPOINT 0x84: Bulk IN ===============================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :   0x84 IN
       bmAttributes     :    0x2 Bulk
       wMaxPacketSize   :   0x40 (64 bytes)
       bInterval        :    0xa
      ENDPOINT 0x3: Bulk OUT ===============================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :    0x3 OUT
       bmAttributes     :    0x2 Bulk
       wMaxPacketSize   :   0x40 (64 bytes)
       bInterval        :    0xa

```

#### 佳博-58MBIII+

小票、标签打印机

##### 照片
![](imgs/佳博-58MBIII-1.JPG)
![](imgs/佳博-58MBIII-2.JPG)


##### 描述符

```plain
DEVICE ID 6868:0200 on Bus 020 Address 018 =================
 bLength                :   0x12 (18 bytes)
 bDescriptorType        :    0x1 Device
 bcdUSB                 :  0x200 USB 2.0
 bDeviceClass           :    0x0 Specified at interface
 bDeviceSubClass        :    0x0
 bDeviceProtocol        :    0x0
 bMaxPacketSize0        :   0x40 (64 bytes)
 idVendor               : 0x6868
 idProduct              : 0x0200
 bcdDevice              :  0x100 Device 1.0
 iManufacturer          :    0x1 GPrinter
 iProduct               :    0x2 GP-58
 iSerialNumber          :    0x0 
 bNumConfigurations     :    0x1
  CONFIGURATION 1: 100 mA ==================================
   bLength              :    0x9 (9 bytes)
   bDescriptorType      :    0x2 Configuration
   wTotalLength         :   0x20 (32 bytes)
   bNumInterfaces       :    0x1
   bConfigurationValue  :    0x1
   iConfiguration       :    0x0 
   bmAttributes         :   0xa0 Bus Powered, Remote Wakeup
   bMaxPower            :   0x32 (100 mA)
    INTERFACE 0: Printer ===================================
     bLength            :    0x9 (9 bytes)
     bDescriptorType    :    0x4 Interface
     bInterfaceNumber   :    0x0
     bAlternateSetting  :    0x0
     bNumEndpoints      :    0x2
     bInterfaceClass    :    0x7 Printer
     bInterfaceSubClass :    0x1
     bInterfaceProtocol :    0x2
     iInterface         :    0x0 
      ENDPOINT 0x81: Bulk IN ===============================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :   0x81 IN
       bmAttributes     :    0x2 Bulk
       wMaxPacketSize   :   0x40 (64 bytes)
       bInterval        :    0x0
      ENDPOINT 0x2: Bulk OUT ===============================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :    0x2 OUT
       bmAttributes     :    0x2 Bulk
       wMaxPacketSize   :   0x40 (64 bytes)
       bInterval        :    0x0
```



#### 佳博GP-R222C

小票打印机

##### 照片
![](imgs/佳博-GP-R222C-1.JPG)
![](imgs/佳博-GP-R222C-2.JPG)


##### 描述符

```plain
DEVICE ID 6868:0500 on Bus 020 Address 027 =================
 bLength                :   0x12 (18 bytes)
 bDescriptorType        :    0x1 Device
 bcdUSB                 :  0x200 USB 2.0
 bDeviceClass           :    0x2 Communications Device
 bDeviceSubClass        :    0x0
 bDeviceProtocol        :    0x0
 bMaxPacketSize0        :   0x40 (64 bytes)
 idVendor               : 0x6868
 idProduct              : 0x0500
 bcdDevice              :  0x100 Device 1.0
 iManufacturer          :    0x1 Zhuhai Howbest Label Printer Co.,Ltd.
 iProduct               :    0x2 Gprinter USB Printer
 iSerialNumber          :    0x3 0002A0000000
 bNumConfigurations     :    0x1
  CONFIGURATION 1: 100 mA ==================================
   bLength              :    0x9 (9 bytes)
   bDescriptorType      :    0x2 Configuration
   wTotalLength         :   0x20 (32 bytes)
   bNumInterfaces       :    0x1
   bConfigurationValue  :    0x1
   iConfiguration       :    0x0 
   bmAttributes         :   0x80 Bus Powered
   bMaxPower            :   0x32 (100 mA)
    INTERFACE 0: Printer ===================================
     bLength            :    0x9 (9 bytes)
     bDescriptorType    :    0x4 Interface
     bInterfaceNumber   :    0x0
     bAlternateSetting  :    0x0
     bNumEndpoints      :    0x2
     bInterfaceClass    :    0x7 Printer
     bInterfaceSubClass :    0x1
     bInterfaceProtocol :    0x2
     iInterface         :    0x0 
      ENDPOINT 0x81: Bulk IN ===============================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :   0x81 IN
       bmAttributes     :    0x2 Bulk
       wMaxPacketSize   :   0x40 (64 bytes)
       bInterval        :    0x0
      ENDPOINT 0x1: Bulk OUT ===============================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :    0x1 OUT
       bmAttributes     :    0x2 Bulk
       wMaxPacketSize   :   0x40 (64 bytes)
       bInterval        :    0x0
```

#### 芯烨-XP-T58H

小票打印机

##### 照片
![](imgs/芯烨-XP-T58H-1.JPG)
![](imgs/芯烨-XP-T58H-2.JPG)


##### 描述符

```plain
DEVICE ID 0483:5743 on Bus 020 Address 019 =================
 bLength                :   0x12 (18 bytes)
 bDescriptorType        :    0x1 Device
 bcdUSB                 :  0x200 USB 2.0
 bDeviceClass           :    0x0 Specified at interface
 bDeviceSubClass        :    0x0
 bDeviceProtocol        :    0x0
 bMaxPacketSize0        :   0x40 (64 bytes)
 idVendor               : 0x0483
 idProduct              : 0x5743
 bcdDevice              :  0x200 Device 2.0
 iManufacturer          :    0x1 Xprinter 
 iProduct               :    0x2 USB Printer P
 iSerialNumber          :    0x3 00000000051C
 bNumConfigurations     :    0x1
  CONFIGURATION 1: 32 mA ===================================
   bLength              :    0x9 (9 bytes)
   bDescriptorType      :    0x2 Configuration
   wTotalLength         :   0x20 (32 bytes)
   bNumInterfaces       :    0x1
   bConfigurationValue  :    0x1
   iConfiguration       :    0x0 
   bmAttributes         :   0xc0 Self Powered
   bMaxPower            :   0x10 (32 mA)
    INTERFACE 0: Printer ===================================
     bLength            :    0x9 (9 bytes)
     bDescriptorType    :    0x4 Interface
     bInterfaceNumber   :    0x0
     bAlternateSetting  :    0x0
     bNumEndpoints      :    0x2
     bInterfaceClass    :    0x7 Printer
     bInterfaceSubClass :    0x1
     bInterfaceProtocol :    0x2
     iInterface         :    0x0 
      ENDPOINT 0x2: Bulk OUT ===============================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :    0x2 OUT
       bmAttributes     :    0x2 Bulk
       wMaxPacketSize   :   0x40 (64 bytes)
       bInterval        :    0x0
      ENDPOINT 0x81: Bulk IN ===============================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :   0x81 IN
       bmAttributes     :    0x2 Bulk
       wMaxPacketSize   :   0x40 (64 bytes)
       bInterval        :    0x0

```
