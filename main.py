import json
import yaml
from pathlib import Path
from config.constants import *
from config.exclude import *
from config.include import *
from config.correct import *
import subprocess


class Sources(object):

    def __init__(self, *args, mkdir_mode=0o777):
        """Generate ethnicity lists in output folder based on ethnicity lists
        obtained by subclasses SourcesLocal and SourcesRemote.
        """
        self.input = args
        self.output = None
        self.mkdir_mode = mkdir_mode

    @staticmethod
    def get(path):
        """Used by subclasses for getting local and remote source files."""
        p = Path('.')
        if path == PATH_SOURCES_REMOTE:
            return list(p.glob(f'{PATH_SOURCES_REMOTE}/*.py'))
        return list(p.glob(f'{PATH_SOURCES_LOCAL}/*.txt'))

    def finalize(self, output_txt=True, output_csv=True, output_json=True,
                 output_yaml=True):
        """Overall cleanup and then file output."""
        # Concatenate
        ethnicities = []
        for i in self.input:
            ethnicities.extend(i)
        # Correct
        for i, e in enumerate(ethnicities):
            if e in correct:
                ethnicities[i] = correct[e]
        # Remove duplicates
        ethnicities = list(set(ethnicities))
        # Exclude
        ethnicities = list(set(ethnicities) - set(exclude))
        # Include
        ethnicities = list(set(ethnicities) | set(include))
        # Alphabetize
        ethnicities.sort()

        # Output
        p = Path(PATH_OUTPUT)
        p.mkdir(mode=self.mkdir_mode, exist_ok=True)
        if output_txt:
            with open(f'{PATH_OUTPUT}/{FILE_OUTPUT}.txt', 'w') as f:
                for e in ethnicities:
                    f.write(f'{e}\n')
            print(f'Success: wrote {FILE_OUTPUT}.txt')
        if output_csv:
            with open(f'{PATH_OUTPUT}/{FILE_OUTPUT}.csv', 'w') as f:
                f.write(',\n'.join(ethnicities))
            print(f'Success: wrote {FILE_OUTPUT}.csv')
        if output_json:
            with open(f'{PATH_OUTPUT}/{FILE_OUTPUT}.json', 'w') as f:
                f.write(json.dumps(ethnicities))
            print(f'Success: wrote {FILE_OUTPUT}.json')
        if output_yaml:
            with open(f'{PATH_OUTPUT}/{FILE_OUTPUT}.yaml', 'w') as f:
                f.write(yaml.dump(ethnicities, explicit_start=True,
                                  default_flow_style=False))
            print(f'Success: wrote {FILE_OUTPUT}.yaml')


class SourcesLocal(Sources):

    def __init__(self):
        self.path = PATH_SOURCES_LOCAL
        assert(Path(self.path).exists()), f'Path not found: {self.path}'
        super().__init__()
        self.input = super().get(self.path)

    def process(self):
        """Get a list of ethnicities from local sources."""
        ethnicities = []
        for source in self.input:
            with open(str(source), 'r') as f:
                for line in f:
                    ethnicities.append(line.strip())
        self.output = ethnicities


class SourcesRemote(Sources):

    def __init__(self, execute=False):
        self.execute = execute
        self.path = PATH_SOURCES_REMOTE
        assert(Path(self.path).exists()), f'Path not found: {self.path}'
        super().__init__()
        self.input = super().get(self.path)

    def process(self):
        """Get a list of ethnicities from remote sources."""
        ethnicities = []
        if self.execute:
            for py in self.input:
                result = subprocess.Popen(f'python {py.name}',
                                          cwd=Path(str(py.parent)))
                result.communicate()[0]
                assert (result.returncode == 0), f'Script error: {py.name}'
        p = Path('.')
        self.input = list(p.glob(f'{PATH_SOURCES_REMOTE}/*.txt'))
        for source in self.input:
            with open(str(source), 'r') as f:
                for line in f:
                    ethnicities.append(line.strip())
        self.output = ethnicities


def main():
    """Generate ethnicity lists in various formats in output folder."""
    # Get ethnicities stored locally
    sources_local = SourcesLocal()
    sources_local.process()

    # Get ethnicities stored remotely
    sources_remote = SourcesRemote(execute=True)
    sources_remote.process()

    # Combine local and remote ethnicities and output master file
    sources = Sources(sources_local.output, sources_remote.output)
    sources.finalize()


if __name__ == '__main__':
    main()
