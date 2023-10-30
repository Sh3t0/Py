# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Users/Karol-PC/PycharmProjects/pythonProject/venv/AMIGO/amigo_(un)install_services.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='amigo_(un)install_services',
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
    icon=['C:\\Users\\Karol-PC\\PycharmProjects\\pythonProject\\venv\\AMIGO\\build\\amigo.ico'],
    hide_console='hide-early',
)
