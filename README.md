## A script to change KVM outputs on the Kceve KC-KVM401CR 4 Port via IR

# Requirements
* Python modules ```os``` and ```sys```
* LIRC installed and configured to expose virtual ir device on ```/dev/lirc0```

# Usage
```python3 main.py <display number>```
eg:
```python3 main.py 1```

# PiKVM Support
1. Install LIRC - Guide: https://github.com/crutonjohn/pikvm-ir
2. Create the file ```/etc/sudoers.d/custom_commands```
3. Put ```kvmd ALL=(ALL) NOPASSWD: ALL``` in the file
4. Put ```kvm.yaml``` into ```/etc/kvmd/override.d/```
5. Move ```switch.py``` into ```/opt/bin/```

Result:

![Screenshot_20230129_202335](https://user-images.githubusercontent.com/52742690/215317142-99dc6937-fa0d-43ed-8a66-0878c1858af5.png)
