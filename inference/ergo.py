#!/usr/bin/env python3
# coding=utf-8
# Version:0.1
# Author: ysicing
# file: ergo.py
# time: 2017/7/18 23:24
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

import collections
import os
import sys
import re
import numpy as np
import tensorflow as tf
#from models.model import rnn_model
#from dataset.chat import process_caht,generate_batch



def main(is_train):
    if is_train:
        print('[INFO] train chat...')
        from . import train
        print('[INFO] train end...')
    else:
        print('[INFO] chat with it...')
        from . import chat


