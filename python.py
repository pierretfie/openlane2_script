print('*****************maina******************')
from time import sleep
from subprocess import run, check_output
print('openlane2 installation starting..........\n\n')
sleep(2)

#first setting up nix and cachix
def nix():
   print('installing nix...checking for curl...\n\n')
   try:
      output = check_output(['curl', '--version']).decode('utf-8').strip()

      #if 'curl' in output:
       #  output = output.split('curl')[-2] 
        # output = output.split(')')[0]
      print(f'curl already installed \ncurrent curl version is {output})')
     
           
   except Exception as e:
      try:
         print('curl not installed\ninstalling curl.......') 
         run(['sudo','dnf','install', '-y','curl'], check = True)   
  
   try:
      print('\n\n\nInstalling nix ....please be patient.....\n\n')
      command = ''' curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix/pr/1145 | sh -s -- install --no-confirm --extra-conf "
    extra-substituters = https://openlane.cachix.org
    extra-trusted-public-keys = openlane.cachix.org-1:qqdwh+QMNGmZAuyeQJTH9ErW57OWSvdtuwfBKdS254E=
" '''
      run(command, shell=True, check=True)
   except Exception as e:
      print(f'an error {e} occurred\nwhile installing nix')
   try:
      print('\n\n setting up nix and installing Cachix\n\n')
      cachix_commands = ['nix-env -f "<nixpkgs>" -iA cachix', 'sudo env PATH="$PATH" cachix use openlane', 'sudo pkill nix-daemon']
      for cmd in cachixcommand :
         run(cmd, shell=True, check=True)
   except Exception as e:
         print(f'an error {e} occurred while setting up cachix')
           
            
nix()
