# IDA-RunLastScript
 IDA Pro plugin with a shortcut to run the most previously used script.

# Installation
Download runlastscript.py and extract it to your `%IDADIR%/plugins/` directory.

# Usage
- File -> Run previous script file

Or

- Ctrl+Shift+F7

# Caveats
If a python script entraps its code within a `__name__ == "__main__"`, it will not run correctly.

If a python script uses implicit IDA modules (e.g. ida_kernwin) without explicitly importing the module, it will fail. TLDR, make sure all module code invokations fall under `idaapi`.

Also retrying some scripts can randomly crash IDA. I'm not sure why, but I think it has to do with modifying global variables.