#!/usr/bin/env python3

from os.path import join

template_file_name = 'README.template.md'
repo_path = '/tmp/.github'

with open(join(repo_path, template_file_name), 'r') as f:
    template = f.read()

with open('/tmp/TABLE.md', 'r') as f:
    table = f.read()
    table += '\n'


dest_text = template.replace('<!-- REPO-LIST -->', table)


with open(join(repo_path, 'profile', 'README.md'), 'w') as f:
    f.write(dest_text)
