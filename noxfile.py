import nox
import sys
import os


sys.path.append(os.path.dirname(__file__))


def split_cmd(cmd: str):
    return cmd.strip().split(" ")


test_deps = [
    '.',
    'coverage'
]


class Tasks:
    test = lambda posargs='': 'python -m unittest discover'
    coverage = lambda posargs: f'coverage {posargs}'
    build_wheel = 'python -m setup sdist bdist_wheel bdist_egg'
    quality = 'flake8'


@nox.session()
def test(session: nox.Session):
    """Run unit tests under coverage (use `nocov` arg to run without coverage)"""
    session.install(*test_deps)
    if session.posargs:
        if 'nocov' in session.posargs:
            # run tests without coverage:
            session.run('python', '-m', *split_cmd(Tasks.test()), *session.posargs)
            return
    # run tests with coverage:
    session.run(*split_cmd(Tasks.coverage('erase')))
    session.run(
        *split_cmd(Tasks.coverage('run -m unittest discover')),
        *session.posargs
    )


@nox.session()
def package(session: nox.Session):
    session.install(
        'wheel',
        'setuptools',
        '.'
    )
    session.run(*split_cmd(Tasks.build_wheel))


@nox.session()
def cov_report(session: nox.Session):
    """Combine coverage.py files and generate an XML report"""
    session.install(
        'coverage'
    )
    session.run(*split_cmd(Tasks.coverage('xml')), '-i')


@nox.session()
def quality(session: nox.Session):
    session.install('flake8')
    session.run(Tasks.quality)
