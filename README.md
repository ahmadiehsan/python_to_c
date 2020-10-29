# Python code to C code!

This project is a sample project for [MyPyC](https://github.com/python/mypy/tree/master/mypyc) performance testing

## Usage

### init

```
git clone --recurse-submodules <this repo url>
cd python-to-c
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run pure Python code

```
python example/program.py
```

### Convert Python code to C

ensure that MyPyC work correct on local machine

```
cd mypy
pytest mypyc
cd ..
```

run convert process

```
cd example
../mypy/scripts/mypyc program.py
```

### run converted C code!

```
python -c "import program"
```

## Conclusion

Python code elapsed time: 11.36

converted C code elapsed time: 2.49
