#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2013 Develer S.r.l. (http://www.develer.com/)
# All rights reserved.
#
# Author: Lorenzo Villani <lvillani@develer.com>
# Author: Riccardo Ferrazzo <rferrazz@develer.com>
#

import sys
from os import path as ospath
from ctypes import c_uint, \
    Structure, \
    c_wchar, \
    c_wchar_p, \
    c_char_p, \
    cdll, \
    create_unicode_buffer, \
    create_string_buffer

TA_SYSTEM = 1
TA_USER = 2

TA_OK = 0x00000000
TA_FAIL = 0x00000001
TA_E_PKEY = 0x00000002
TA_E_ACTIVATE = 0x00000003
TA_E_INET = 0x00000004
TA_E_INUSE = 0x00000005
TA_E_REVOKED = 0x00000006
TA_E_GUID = 0x00000007
TA_E_PDETS = 0x00000008
TA_E_TRIAL = 0x00000009
TA_E_TRIAL_EUSED = 0x0000000C
TA_E_TRIAL_EEXP = 0x0000000D
TA_E_EXPIRED = 0x0000000D
TA_E_REACTIVATE = 0x0000000A
TA_E_COM = 0x0000000B
TA_E_INSUFFICIENT_BUFFER = 0x0000000E
TA_E_PERMISSION = 0x0000000F
TA_E_INVALID_FLAGS = 0x00000010
TA_E_IN_VM = 0x00000011
TA_E_EDATA_LONG = 0x00000012
TA_E_INVALID_ARGS = 0x00000013
TA_E_KEY_FOR_TURBOFLOAT = 0x00000014
TA_E_INET_DELAYED = 0x00000015
TA_E_FEATURES_CHANGED = 0x00000016
TA_E_ANDROID_NOT_INIT = 0x00000017

TA_SKIP_OFFLINE = 0x00000001
TA_OFFLINE_SHOW_INET_ERR = 0x00000002

String = c_wchar_p if sys.platform == "win32" else c_char_p

def wbuf(size):
    return create_unicode_buffer(size) if sys.platform == "win32" else create_string_buffer(size)

class GENUINE_OPTIONS(Structure):
    _fields_ = [
        ("nLength", c_uint),
        ("flags", c_uint),
        ("nDaysBetweenChecks", c_uint),
        ("nGraceDaysOnInetErr", c_uint),
    ]

class ACTIVATE_OPTIONS(Structure):
    _fields_ = [
        ("nLength", c_uint),
        ("sExtraData", String),
    ]

def load_library(path):
    LIBRARIES = {
        'linux2': ospath.join(path, 'libTurboActivate.so'),
        'darwin': ospath.join(path, 'libTurboActivate.dylib'),
        'win32': ospath.join(path, 'TurboActivate.dll'),
    }
    return cdll.LoadLibrary(LIBRARIES[sys.platform])


