#!usr/bin/env python3

import time
source = ['Books', 'Documents', 'Keys', 'Music', 'Pictures']
target = f"Backup/{time.strftime('%d_%m_%Y')}.zip"
zip_command = f'zip -qr {target} {" ".join(source)}'
