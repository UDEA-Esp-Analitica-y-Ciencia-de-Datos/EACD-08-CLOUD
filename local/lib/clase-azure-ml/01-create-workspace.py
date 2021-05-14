# tutorial/01-create-workspace.py
from azureml.core.authentication import InteractiveLoginAuthentication
from azureml.core import Workspace

interactive_auth = InteractiveLoginAuthentication(tenant_id="")
ws = Workspace.create(name='azure-ml',
            subscription_id='',
            resource_group='rg_machine_learning',
            create_resource_group=True,
            location='eastus2',
            auth=interactive_auth
            )
            
# write out the workspace details to a configuration file: .azureml/config.json
ws.write_config(path='.azureml')