#!/usr/bin/env python3
# coding=utf-8
# Version:0.0.1
# Author: ysicing
# file: main.py
# time: 2017/7/18 23:09
# Copyright 2017 ysicing. All Rights Reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------

import argparse

def parse_args():
    parse = argparse.ArgumentParser(description='Intelligent robot based on TensorFlow.')

    help_ = 'you can set this value in terminal,but now only support chat.'
    parse.add_argument('-t','--target',default='chat',choices=['chat'],help=help_)

    help_ = 'choose to train or test.'
    parse.add_argument('--train',dest='train',action='store_true',help=help_)
    parse.add_argument('--no-train',dest='train',action='store_false',help=help_)
    parse.set_defaults(train=True)

    args_ = parse.parse_args()
    return args_

if __name__ == '__main__':
    args =parse_args()
    if args.target == 'chat':
        from inference import ergo
        if args.train:
            ergo.main(True)
        else:
            ergo.main(False)
    elif args.target == 'poem':
        print('[INFO] The next update may be supported')
        pass
    else:
        print('[INFO] Simple english communion right now.')
