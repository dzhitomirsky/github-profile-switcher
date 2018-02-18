#!/usr/bin/python

import io
import argparse
from os.path import expanduser, exists
from os import remove, environ
from subprocess import Popen, PIPE

HOME_DIR = expanduser("~")

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
    print "Clearing keychain for github account..."
    if exists(HOME_DIR + '/.git-credentials'):
        remove(HOME_DIR + '/.git-credentials')
    p = Popen(['git credential-osxkeychain erase'], stdin=PIPE, shell=True)
    p.communicate(input='host=github.com\nprotocol=https\n')

def get_git_credentians_from_env(profile):
    print "Checking env variables..."
    if profile == 'work':
        if 'WORK_GIT_USER' not in environ:
            raise ValueError('WORK_GIT_USER missing in env variables.')
        if 'WORK_GIT_EMAIL' not in environ:
            raise ValueError('WORK_GIT_EMAIL missing in env variables.')
        return (environ.get('WORK_GIT_USER'), environ.get('WORK_GIT_EMAIL'))
    elif profile == 'home':
        if 'HOME_GIT_USER' not in environ:
            raise ValueError('HOME_GIT_USER missing in env variables.')
        if 'HOME_GIT_EMAIL' not in environ:
            raise ValueError('HOME_GIT_EMAIL missing in env variables.')
        return (environ.get('HOME_GIT_USER'), environ.get('HOME_GIT_EMAIL'))
    else:
        raise ValueError('Invalid git profile, only work|home are supported')


def generate_git_config(profile_type):
    user, email =  get_git_credentians_from_env(profile_type)
    print "Generating new ~/.gitconfig file..."
    with io.FileIO(HOME_DIR + "/.gitconfig", "w") as file:
        file.write(gitconfig_template.format(user=user, email=email))

    print "Git config (~/.gitconfig) was successfully generated for {user}({email})".format(user=user, email=email)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="The script generates " +
    "'.gitconfig' file depending on prfile (job by default), and clears up mac keychain")

    parser.add_argument('text', type=str, help='Profile name (work|home) options are supported', nargs='?', default="work")

    args = parser.parse_args()
    crear_git_cache()
    generate_git_config(args.text)
