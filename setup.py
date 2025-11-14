from distutils.core import setup
import py2exe
options = {
    'py2exe': {
        'includes': ['win32gui', 'win32process', 'win32api', 'tkinter', 'psutil', 're', 'json']
    }
}

setup(
    version="0.0.1a4",
    options=options,
    description="TorchFurry Torchlight Income Statistics Tool - English Version",
    console=['index.py'],
    data_files=[
        ('', [
            'full_table.json',
            'instructions.txt',
            'price.json',
            'id_table.json',
            'en_id_table.json',
            'id_table.conf',
            'en_id_table.conf',
            'config.json',
            'translation_mapping.json',
            'drops.txt'
        ])
    ]
)
