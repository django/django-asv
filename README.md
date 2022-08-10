# **Django ASV**

This repository contains the benchmarks for measuring Django's performance over time.

The benchmarking process is carried out by the benchmarking tool [airspeed velocity](https://asv.readthedocs.io/en/stable/) and the results can be viewed [here](https://django.github.io/django-asv/)

## **Running the benchmarks**
---

### **If you have installed Anaconda or miniconda**

`Conda` is being used to run the benchmarks against different versions of python

If you already have conda or miniconda installed,you can run the benchmarks by using the commands

```
pip install asv
asv run
```

to run the benchmarks against the latest commit.


### **If you have not installed Anaconda or miniconda**


If you do not have conda or miniconda installed, change the contents of the file `asv.conf.json` as follows to use `virutalenv` to run the benchmarks

```json
{
    "version": 1,
    "project": "Django",
    "project_url": "https://www.djangoproject.com/",
    "repo": "https://github.com/django/django.git",
    "branches": ["main"],
    "environment_type": "virtualenv",
    "show_commit_url": "http://github.com/django/django/commit/",
}
```

and run the benchmarks using the commands

```
pip install asv
asv run
```

**Note**: `ASV` prompts you to set a machine name on the first run, please do not set it to 'ubuntu-22.04', 'windows-2022' or 'macos-12' as the results for the machines with these names are currently being stored in the repository

## **Comparing Benchmarks Results Of Different Commits Or Branches**
---

Benchmarking results of differnt branches can be compared using the following method

```
asv run <commit1 SHA or branch1 name>
asv run <commit2 SHA or branch2 name>
asv compare <commit1 SHA or branch name> <commit2 SHA or branch name>
```

## **Writing New Benchmarks And Contributing**
---

- Fork this repository and create a new branch
- Install `pre-commit` and run `pre-commit install` to install pre-commit hooks which will be used to format the code
- Create a new directory with the name `benchmark_name` under the appropriate category of benchmarks
- Add the files `__init__.py` and `benchmark.py` to the directory
- Add the directory to the list of `INSTALLLED_APPS` in settings.py
- Use the following format to write your benchmark in the file `benchmark.py`

    ```python
        from ...utils import bench_setup()

        class BenchmarkClass:

            def setup():
                bench_setup()
                # if your benchmark makes use of models then use
                # bench_setup(migrate=True)
                ...

            def time_benchmark_name():
                ...
    ```
- Commit changes and create a pull request
