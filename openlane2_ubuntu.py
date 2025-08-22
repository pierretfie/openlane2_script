print('*****************maina******************')
from time import sleep
from subprocess import run, check_output
from os import path

print('openlane2 installation starting..........\n\n')
sleep(2)

# install required Ubuntu dependencies
def install_prereqs():
    print("Checking and installing prerequisites for Ubuntu...\n\n")
    try:
        run(['sudo', 'apt', 'update'], check=True)
        run([
            'sudo', 'apt', 'install', '-y',
            'curl', 'git', 'build-essential', 'xz-utils', 'python3', 'python3-pip',
            'ca-certificates', 'libssl-dev', 'pkg-config'
        ], check=True)
    except Exception as e:
        print(f"Error installing prerequisites: {e}")
    else:
        print("Prerequisites installed successfully.\n\n")

# first setting up nix and cachix
def install_nix():
    while True:
        print('installing nix...checking for curl...\n\n')
        try:
            output = check_output(['curl', '--version']).decode('utf-8').strip()
            print(f'curl already installed \ncurrent curl version is {output})')
        except Exception as e:
            print('curl not installed\ninstalling curl.......')
            try:
                run(['sudo', 'apt', 'update'], check=True)
                run(['sudo', 'apt', 'install', '-y', 'curl'], check=True)
            except Exception as e:
                print(f'error occurred while installing curl\n {e}')
                continue
        break

    # install nix
    print('\n\n\nInstalling nix ....please be patient.....\n\n')
    command = '''curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix/pr/1145 | sh -s -- install --no-confirm --extra-conf "
    extra-substituters = https://openlane.cachix.org
    extra-trusted-public-keys = openlane.cachix.org-1:qqdwh+QMNGmZAuyeQJTH9ErW57OWSvdtuwfBKdS254E="
    '''
    while True:
        try:
            run(command, shell=True, check=True)
        except Exception as e:
            print(f'an error {e} occurred\nwhile installing nix')
        else:
            break

    while True:
        try:
            print('\n\n setting up nix and installing Cachix\n\n')
            cachix_commands = [
                'nix-env -f "<nixpkgs>" -iA cachix',
                'sudo env PATH="$PATH" cachix use openlane',
                'sudo pkill nix-daemon'
            ]
            for cmd in cachix_commands:
                run(cmd, shell=True, check=True)
        except Exception as e:
            print(f'an error {e} occurred while setting up cachix')
        else:
            break
    print('\n\n\nnix and cachix installation complete\n\n')


def openlane_install():
    openlanedir = path.expanduser('~/openlane2')
    print('\n\n cloning openlane2\n\n')
    git_command = f'git clone https://github.com/efabless/openlane2 {openlanedir}'
    clone_failure = True

    while clone_failure:
        try:
            run(git_command, shell=True, check=True)
        except Exception as e:
            print(f'error occurred while cloning openlane2 repo\n{e}\n\n')
        else:
            print('openlane successfuly cloned\n\n')
            clone_failure = False

    print('\n\nInvoke nix-shell, which will make all the packages bundled with OpenLane available to your shell.\n'
          'Some packages will be downloaded (about 3GiB) and afterwards\n\n')
    nixinvoke_failure = True
    while nixinvoke_failure:
        invokecmd = 'nix-shell --pure ~/openlane2/shell.nix'
        try:
            run(invokecmd, shell=True, check=True)
        except Exception as e:
            print(f'error occurred while invoking nix-shell\n{e}\n\n')
        else:
            print('nix-shell invoked successfully\n\n')
            nixinvoke_failure = False

    print('\n\nRun the smoke test to ensure everything is fine. This also downloads sky130 PDK.')
    while True:
        smoke_test_cmd = 'openlane --log-level ERROR --condensed --show-progress-bar --smoke-test'
        try:
            run(smoke_test_cmd, shell=True, check=True)
        except Exception as e:
            print(f'error occurred while running smoke test\n{e}\n\n')
        else:
            print('smoke test successful\n\n')
            break
    print("\n\n That’s it. Everything is ready. Now, let’s try OpenLane.\n\n")


# Run everything
install_prereqs()
install_nix()
openlane_install()
