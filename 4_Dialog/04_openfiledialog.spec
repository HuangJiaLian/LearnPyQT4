# -*- mode: python -*-

block_cipher = None


a = Analysis(['04_openfiledialog.py'],
             pathex=['E:\\MEGA\\GitHub\\pyqt\\4_Dialog'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='04_openfiledialog',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
