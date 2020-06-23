import pickle
import json
from os import path, fsync
from glob import glob
from subprocess import check_call


exists = path.exists


def mkdir(dst: str):
    check_call('mkdir -p {dst}', shell=True)


def cp(src: str, dst: str):
    check_call(f'cp -r {src} {dst}', shell=True)


def mv(src: str, dst: str):
    check_call(f'mv {src} {dst}', shell=True)


def ln(src: str, dst: str = '.'):
    check_call(f'ln {src} {dst}', shell=True)


def ls(src: str, reg: str = '*', isdir=None):
    entries = []

    for entry in glob(path.join(src, reg)):
        # skip non-directory entries
        if isdir is True and not path.isdir(entry):
            continue
        
        # skip directory entries
        if isdir is False and path.isdir(entry):
            continue
        
        entries.append(entry.split('/')[-1])

    return entries


def echo(txt: str, dst: str, mode: str = 'w'):
    with open(dst, mode) as f:
        f.write(txt)
        f.flush()
        fsync(f.fileno())


def load(src: str):
    ext = path.splitext(src)[1]

    if ext == '.json':
        with open(src, 'r') as tf:
            return json.load(tf)
    
    elif ext == '.pickle':
        with open(src, 'rb') as bf:
            return pickle.load(bf)
    
    raise ValueError(f'Unrecognized file extension {ext}.')

def dump(obj, dst: str):
    ext = path.splitext(dst)[1]

    if ext == '.json':
        with open(dst, 'w') as tf:
            return json.dump(obj, tf)
    
    elif ext == '.pickle':
        with open(dst, 'wb') as bf:
            return pickle.dump(obj, bf)
    
    raise ValueError(f'Unrecognized file extension {ext}.')
