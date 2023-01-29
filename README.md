## A script to change KVM outputs on the Kceve KC-KVM401CR 4 Port via IR

# Requirements
* Python modules ```os``` and ```sys```
* LIRC installed and configured to expose virtual ir device on ```/dev/lirc0```

# Usage
```python3 main.py <display number>```
eg:
```python3 main.py 1```

# PiKVM Support
Put ```kvm.yaml``` into ```/etc/kvmd/override.d/```

Result:

![Screenshot_20230129_202335](https://user-images.githubusercontent.com/52742690/215317142-99dc6937-fa0d-43ed-8a66-0878c1858af5.png)
