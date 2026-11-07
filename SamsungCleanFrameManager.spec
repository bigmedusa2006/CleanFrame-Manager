# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['manager_window.py'],
    pathex=['D:/Samsung TV Project/SamsungCleanFrame/scripts', 'D:/Samsung TV Project/samsung-tv-root-release/samsung-tv-root-0.0.12-windows-x86_64/source/src'],
    binaries=[],
    datas=[('tv_manager_v3.html', '.'), ('web', 'web')],
    hiddenimports=['font_assets', 'local_config', 'private_files', 'samsung_tv_root', 'samsung_tv_root.archive_root', 'samsung_tv_root.resources', 'samsung_tv_root.root_agent', 'samsung_tv_root.sdb'],
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
    name='SamsungCleanFrameManager',
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
    icon=['D:/Samsung TV Project/CleanFrame Manager/app.ico'],
)
