# launchcontrol
My Novation controller tool

## Alsa issues
If you get alsa errors, run:
```sh
cd /usr/lib/x86_64-linux-gnu/
sudo ln -s alsa-lib/libasound_module_conf_pulse.so libasound_module_conf_pulse.so
```