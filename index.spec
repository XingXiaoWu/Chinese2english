# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['/Users/xingwu/Desktop/1/py/chinese2english/src/index.py','/Users/xingwu/Desktop/1/py/chinese2english/src/fileedit.py','/Users/xingwu/Desktop/1/py/chinese2english/src/chinese2english.py'],
             pathex=['/Users/xingwu/Desktop/1/py/chinese2english/'],
             binaries=[],
             datas=[],
             hiddenimports=['/Users/xingwu/Desktop/1/py/chinese2english/src'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='index',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='index.app',
             icon=None,
             bundle_identifier=None)
