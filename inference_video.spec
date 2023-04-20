# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

a = Analysis(
    ['src\\inference_video.py'],
    pathex=['venv/Lib/site-packages'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='inference_video',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='inference_video',
)

import shutil

train_log_dist_path = '{0}/inference_video/train_log'.format(DISTPATH)

if os.path.exists(train_log_dist_path):
    shutil.rmtree(train_log_dist_path)

shutil.copytree('train_log', train_log_dist_path)
