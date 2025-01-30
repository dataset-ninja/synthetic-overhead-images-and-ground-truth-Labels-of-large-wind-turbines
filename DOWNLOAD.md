Dataset **Large Wind Turbines (by Duke Dataplus2020)** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzExMDVfTGFyZ2UgV2luZCBUdXJiaW5lcyAoYnkgRHVrZSBEYXRhcGx1czIwMjApL2xhcmdlLXdpbmQtdHVyYmluZXMtKGJ5LWR1a2UtZGF0YXBsdXMyMDIwKS1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJ3RWIxR3dzenF3enIrRGNkN2NhUys5Y0hqUFNiZ0d3MWxpV2tiT2dXSmZjPSJ9)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Large Wind Turbines (by Duke Dataplus2020)', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://figshare.com/ndownloader/files/24118220).