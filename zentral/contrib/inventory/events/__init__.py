import logging
from zentral.core.events import BaseEvent, EventMetadata, event_cls_from_type, register_event_type

logger = logging.getLogger('zentral.contrib.inventory.events')


class InventoryMachineAdded(BaseEvent):
    event_type = 'inventory_machine_added'


register_event_type(InventoryMachineAdded)


# Inventory update events
for attr in ('reference',
             'machine',
             'link',
             'business_unit',
             'group',
             'os_version',
             'system_info',
             'osx_app_instance',
             'teamviewer'):
    event_type = 'inventory_{}_update'.format(attr)
    event_class_name = "".join(s.title() for s in event_type.split('_'))
    event_class = type(event_class_name, (BaseEvent,), {'event_type': event_type})
    register_event_type(event_class)


def post_inventory_events(msn, events, uuid, index):
    for event_type, data in events:
        event_cls = event_cls_from_type(event_type)
        metadata = EventMetadata(event_cls.event_type,
                                 machine_serial_number=msn,
                                 uuid=uuid,
                                 index=index,
                                 tags=['inventory_update'])
        event = event_cls(metadata, data)
        event.post()
        index += 1
    return index
