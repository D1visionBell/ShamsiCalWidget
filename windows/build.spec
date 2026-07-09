# -*- mode: python ; coding: utf-8 -*-
# Build with:  pyinstaller build.spec
# Output:      dist\ShamsiCalWidget.exe

block_cipher = None

a = Analysis(
    ['app/main.py'],
    pathex=['app'],
    binaries=[],
    datas=[
        ('app/resources/fonts/vazirmatn_medium.ttf', 'resources/fonts'),
        ('app/resources/fonts/vazirmatn_bold.ttf', 'resources/fonts'),
        ('app/resources/icon.ico', 'resources'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ShamsiCalWidget',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,          # windowed app, no console popup
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='app/resources/icon.ico',
)
