# -*- mode: python -*-

block_cipher = None


a = Analysis(['custom_pomodoro.py'],
             pathex=['/Users/bliutwo/Dropbox/Daily Goals/pomodoro'],
             binaries=None,
             datas=None,
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
          name='custom_pomodoro',
          debug=False,
          strip=False,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='custom_pomodoro.app',
             icon=None,
             bundle_identifier=None)
