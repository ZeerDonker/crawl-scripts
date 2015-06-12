import fnmatch
import os

import datetime

import hashlib

import errno
import itertools

import shutil

def filesWithEnd(gdir, fileend ):
    matches = []
    for root, dirnames, filenames in os.walk(gdir):
      for filename in fnmatch.filter(filenames, fileend ):
          matches.append(os.path.join(root, filename))
    return matches

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

def make_date(filename):
    t = os.path.getctime(filename)
    return datetime.datetime.fromtimestamp(t)



def retSave( path ):
    hsh = hashFile(path  )
    name = path.rpartition('/')[2]
    t = os.path.getctime(filename)
    newSave = Save(name=name, path = path, date_file=t)
    newSave.date_update = datetime.now()
    newSave.file_hash = hsh
    return newSave


def hashFile( fname):
    return hashlib.sha256(open(fname, 'rb').read()).digest()

gdir = os.getcwd()
print( gdir)

mtch = filesWithEnd(gdir+'/','*.cs' )


def hashedFiles(mtch):
    hashes = []
    fls = []
    changeDate = []

    for fs in mtch:
        #print fs, modification_date(fs), make_date(fs)
        hsh = hashFile( fs )
        if hsh not in hashes :
            hashes.append(  hsh)
            fls.append( fs )
            changeDate.append(  modification_date(fs))
            print (fs, modification_date(fs))
    return hashes, fls, changeDate


mtchS = filesWithEnd('saves/','*.cs' )
ha,fls,dte=  hashedFiles(mtchS)

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

mkdir_p('bsave/older/')

for fl, dt in zip( fls, dte):
    tmfolder = str(dt).replace(' ','_' ).replace(':','.')
    nfile = fl.replace( 'saves','bsave')
    nfile2 = fl.replace( 'saves','bsave/older/'+tmfolder)
    mkdir_p('bsave/older/'+tmfolder)
    print ( fl, nfile2)
    shutil.copy( fl,nfile)
    shutil.copy( fl,nfile2)


