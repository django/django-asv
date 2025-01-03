# Django ASV

This repository contains the benchmarks for measuring Django's performance over time.

The benchmarking process is carried out by the benchmarking tool [Airspeed Velocity](https://asv.readthedocs.io/en/stable/) and the results can be viewed [Django ASV results page](https://django.github.io/django-asv/).

## Running the benchmarks

### Using Conda or Miniconda

**Conda** is being used to run the benchmarks against different versions of **Python**.

If you already have **Conda** or **Miniconda** installed, you can run the benchmarks by using the commands:

```console
python -m pip install asv
python -m asv run
```

to run the benchmarks against the latest commit.

### Using virtualenv

To use `virutalenv` to run the benchmarks _(e.g. if you do not have **Conda** or **Miniconda** installed)_ change the contents of the file `asv.conf.json` as follows:

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

```console
python -m pip install asv
python -m asv run
```

> [!NOTE]
> `ASV` prompts you to set a machine name on the first run, please do not set it to `ubuntu-22.04`, `ubuntu-latest`, `windows-2022` or `macos-12` as the results for the machines with these names are currently being stored in the repository

## Comparing benchmarks results

Benchmarking results of different commits or branches can be compared using the following method:

```console
python -m asv run <commit1 SHA or branch1 name>
python -m asv run <commit2 SHA or branch2 name>
python -m asv compare <commit1 SHA or branch name> <commit2 SHA or branch name>
```

## Writing new benchmarks and contributing

1. Fork this repository and create a new branch.
2. Install **pre-commit** and run `python -m pre_commit install` to install hooks which will be used to format the code.
3. Create a new directory with the name `benchmark_name` under the appropriate category of benchmarks.
4. Add the files `__init__.py` and `benchmark.py` to the directory.
5. Add the directory to the list of `INSTALLLED_APPS` in `settings.py`.
6. Use the following format to write your benchmark in the file `benchmark.py`:

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
7. Commit changes and create a pull request.
