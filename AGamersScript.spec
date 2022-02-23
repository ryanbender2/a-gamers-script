# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['src\\main.py'],
            pathex=[],
            binaries=[],
            datas=[
                ('./src/runners', 'runners/'),
                ('./src/__init__.py', '.'),
                ('./src/agamersscript.py', '.'),
                ('./src/ui.py', '.'),
                ('./src/logger.py', '.'),
                ('./images', 'images/')
            ],
            hiddenimports=[
                'PIL',
                'PIL.ImageTk',
                'tkinter',
                'selenium',
                'selenium.webdriver.remote.webelement',
                'selenium.webdriver.support.expected_conditions',
                'selenium.webdriver.support.ui',
                'webdriver_manager.chrome'
            ],
            hookspath=[],
            hooksconfig={},
            runtime_hooks=[],
            excludes=[],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            cipher=block_cipher,
            noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,  
    [],
    name='AGamersScript',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='images\\app.ico'
)
