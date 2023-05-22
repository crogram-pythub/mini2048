# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

APP_ID = 'org.pythub.app.mini2048'
APP_APP = 'Mini2048.app'
APP_VERSION = '0.0.1'
APP_BUILD = '1'
APP_NAME = 'Mini2048'
APP_NAME_DISPLAY = 'Mini2048'
EXE_ICON = os.path.join('resources', 'favicon.ico')
APP_ICON = os.path.join('resources', 'app.icns')


a = Analysis(['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=APP_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=EXE_ICON)
coll = COLLECT(exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=APP_NAME)
app = BUNDLE(
    coll,
    name=APP_APP,
    icon=APP_ICON,
    bundle_identifier=APP_ID,
    info_plist={
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME_DISPLAY,
        'CFBundleGetInfoString': "CROGRAM INC.",
        'CFBundleIdentifier': APP_ID,
        'CFBundleVersion': APP_BUILD,
        'CFBundleShortVersionString': APP_VERSION,
        'CFBundleInfoDictionaryVersion': APP_VERSION,
        'CFBundlePackageType': 'APPL',
        'CFBundleSupportedPlatforms': ['MacOSX'],
        'LSMinimumSystemVersion': '11.0', # 最低系统版本
        'NSHumanReadableCopyright': "© 2023 CROGRAM INC. All Rights Reserved.",
        'NSHighResolutionCapable': True,
        'LSApplicationCategoryType': 'public.app-category.utilities'
    })
