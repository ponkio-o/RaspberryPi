#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import binascii
import urllib
import urllib2

from time import sleep

sys.path.append('/usr/local/src/nfcpy')
import nfc

#Felicaのサービスコードの指定
service_code = 0x09cb

#学生証の読み取り
def connected(tag):

    if isinstance(tag, nfc.tag.tt3.Type3Tag):
        try:
            sc = nfc.tag.tt3.ServiceCode(service_code >> 6, service_code & 0x3f)
            bc = nfc.tag.tt3.BlockCode(0, service=0)
            
            #16進数を代入して文字列に変換
            id_temp = binascii.hexlify(tag.read_without_encryption([sc], [bc]))
            id = binascii.unhexlify(id_temp)

            #前後に不要な文字列があるので必要部分だけ表示
            id = id[2:10]
            print id

            #LINENotifyで学籍番号を通知する
            params = {"message":"%sが訪問にきました" % id}
            params = urllib.urlencode(params)

            req = urllib2.Request("https://notify-api.line.me/api/notify")
            req.add_header("Authorization","Bearer " + "LINE Notify Token")
            req.add_data(params)

            res = urllib2.urlopen(req)

        except Exception as e:                                                                                                                                                                                                                                              
            print "error: %s" % e
    else:   
        print "error: tag isn't Type3Tag"

clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': connected})
