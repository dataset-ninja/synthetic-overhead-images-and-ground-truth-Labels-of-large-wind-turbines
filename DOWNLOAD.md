Dataset **Wind Turbines 4** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/V/i/ph/LBp7VzqZt4ZJuTJUiZMsOzLnxOTOqhRznAPjECNlkQQbVPTWpL0p0sdqdINQSFOV93USnRHTcktp9HOFwkXYsEbelPzcGxzrVvBt8qnxUID0CT68IjooF6lEpGAk.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Wind Turbines 4', dst_path='~/dtools/datasets/Wind Turbines 4.tar')
```
The data in original format can be 🔗[downloaded here](https://figshare.com/ndownloader/files/24118220)