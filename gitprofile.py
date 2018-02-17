#!/usr/bin/python

import io
import argparse
from os.path import expanduser, exists
from os import remove, environ
from subprocess import Popen, PIPE

HOME_DIR = expanduser("~")

HOME_USER = environ.get('HOME_GIT_USER')
HOME_EMAIL = environ.get('HOME_GIT_EMAIL')

WORK_USER = environ.get('WORK_GIT_USER')
WORK_EMAIL = environ.get('WORK_GIT_EMAIL')

gitconfig_template = """
[user]
        email = {email}
	      name =  {user}

[credential]
        helper = store

[push]
        default = current
"""

def crear_git_cache():
    if exists(HOME_DIR + '/.git-credentials'):
        remove(HOME_DIR + '/.git-credentials')
    p = Popen(['git credential-osxkeychain erase'], stdin=PIPE, shell=True)
    p.communicate(input='host=github.com\nprotocol=https\n')


def generate_git_config(profile_type):

    with io.FileIO(HOME_DIR + "/.gitconfig", "w") as file:
        if profile_type == 'work':
            file.write(gitconfig_template.format(email=WORK_EMAIL, user=WORK_USER))
        else:
            file.write(gitconfig_template.format(email=HOME_EMAIL, user=HOME_USER))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="The script generates " +
    "'.gitconfig' file depending on prfile (job by default), and clears up mac keychain")

    parser.add_argument('text', type=str, help='Profile name (work|home) options are supported', nargs='?', default="work")

    args = parser.parse_args()
    crear_git_cache()
    generate_git_config(args.text)
