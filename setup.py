from distutils.core import setup
from distutils.command.install_data import install_data
import os
import sys

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
    packages = packages,
    cmdclass = cmdclasses,
    data_files = data_files,
    scripts = ['bin/ckstyle-admin.py', 'bin/ckstyle.bat'],
    classifiers = ['Intended Audience :: Developers',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: CSS'
                   ],
)
