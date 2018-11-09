from shutil import copyfile
import os
import stat
from pkg_resources import resource_filename

import click



def install_pre_commit_msg_hook():
    pass


def install_pre_push(hooks_path):
    filename = resource_filename('git_hooks.hooks', 'pre-push.py')
    hook_name = os.path.splitext(os.path.basename(filename))[0]
    destination = os.path.join(hooks_path, hook_name)
    copyfile(filename, destination)
    st = os.stat(destination)
    os.chmod(destination, st.st_mode | stat.S_IEXEC)


def install_prepare_commit_message(hooks_path):
    filename = resource_filename('git_hooks.hooks', 'prepare-commit-msg.py')
    hook_name = os.path.splitext(os.path.basename(filename))[0]
    destination = os.path.join(hooks_path, hook_name)
    copyfile(filename, destination)
    st = os.stat(destination)
    os.chmod(destination, st.st_mode | stat.S_IEXEC)

    
@click.command()
@click.argument('git_path', type=click.Path(), default='.git')
def install(git_path):
    cwd = os.getcwd()
    hooks_path = os.path.join(cwd, git_path, 'hooks')
    install_prepare_commit_message(hooks_path)
    install_pre_push(hooks_path)

if __name__ == '__main__':
    install()
