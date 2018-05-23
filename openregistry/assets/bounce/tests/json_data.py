# -*- coding: utf-8 -*-
from copy import deepcopy
from openregistry.assets.core.tests.blanks.json_data import (
    test_organization_loki,
    schema_properties,
    test_loki_item_data
)
from openregistry.assets.core.utils import (
    get_now
)

test_item_data = deepcopy(test_loki_item_data)
del test_item_data['id']

# test_loki_item_data['schema_properties'] = schema_properties

test_asset_bounce_data = {
    "title": u"Земля для космодрому",
    "description": u"Опис землі для космодрому",
    "assetType": "bounce",
    "items": [test_item_data, test_item_data],
    "assetCustodian": deepcopy(test_organization_loki),
    "decisions": [{
        'decisionDate': get_now().isoformat(),
        'decisionID': '1111-4'
    }]
}


