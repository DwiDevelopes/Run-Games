# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\User\\Documents\\Game Py Creat By Me\\Run Games\\Run Games.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\User\\Documents\\Game Py Creat By Me\\Run Games\\run games.ico', '.ico'), ('C:\\Users\\User\\Documents\\Game Py Creat By Me\\Run Games', 'Run Games/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Run Games',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\User\\Documents\\Game Py Creat By Me\\Run Games\\run games.ico'],
)
