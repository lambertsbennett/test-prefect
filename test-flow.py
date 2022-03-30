from prefect import task, Flow
from prefect.executors import DaskExecutor 
from prefect.run_configs import KubernetesRun
from prefect.storage import GitHub


@task
def get_value():
    return "Example!"


@task
def output_value(value):
    print(value)


with Flow("Test") as flow:
    value = get_value()
    output_value(value)

flow.run_config = KubernetesRun()
# flow.executor = DaskExecutor("10.2.36.44:8786")
flow.storage = GitHub(repo='lambertsbennett/prefect-test', path='test-flow.py')

