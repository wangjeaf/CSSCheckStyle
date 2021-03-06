#!/usr/bin/env python
#
# Copyright 2012 The CSSCheckStyle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

try:
    from setuptools import setup
except ImportError:
    print '[CKstyle] ERROR please install "easy_install" firstly'
    sys.exit(0)

from distutils.command.install_data import install_data
import os

cmdclasses = {'install_data': install_data} 

def fullsplit(path, result=None):
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)
ckstyle_dir = 'ckstyle'

for dirpath, dirnames, filenames in os.walk(ckstyle_dir):
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.') or dirname.startswith('_') : del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

setup(
    name = "CSSCheckStyle",
    version = '1.0.0',
    url = 'https://github.com/wangjeaf/CSSCheckStyle',
    author = 'wangjeaf',
    author_email = 'wangjeaf@gmail.com',
    description = 'Check Code Style and more, for CSS.',
    download_url = 'https://github.com/wangjeaf/CSSCheckStyle/archive/master.tar.gz',
    install_requires=['python-gflags'],
    packages = packages,
    cmdclass = cmdclasses,
    data_files = data_files,
    entry_points = {
        'console_scripts': [
            'ckstyle = ckstyle.command.index:ckstyle'
        ]
    },
    classifiers = ['Intended Audience :: Developers',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: CSS'
                   ],
)
