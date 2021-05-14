from azureml.core import Workspace, Experiment, Environment, ScriptRunConfig

ws = Workspace.from_config(path='./.azureml', _file_name='config.json')

experiment = Experiment(workspace=ws, name='day1-experiment-testing-workspace')

config = ScriptRunConfig(source_directory='./src', script='test-workspace.py', compute_target='cpu-cluster')

run = experiment.submit(config)

aml_url = run.get_portal_url()

print(aml_url)
