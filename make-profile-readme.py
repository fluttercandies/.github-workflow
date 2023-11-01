#!/usr/bin/env python3

import os
from os.path import join

target_file = os.environ['TARGET_FILE']

template_file_name = 'README.template.md'

with open(join(target_file, '..', template_file_name), 'r') as f:
    template = f.read()

with open('/tmp/TABLE.md', 'r') as f:
    table = f.read()


dest_text = template.replace('<!-- REPO-LIST -->', table)


with open(target_file, 'w') as f:
    f.write(dest_text)
