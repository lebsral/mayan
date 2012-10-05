from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from .permissions import (PERMISSION_BOOTSTRAP_VIEW, PERMISSION_BOOTSTRAP_CREATE,
    PERMISSION_BOOTSTRAP_EDIT, PERMISSION_BOOTSTRAP_DELETE,
    PERMISSION_BOOTSTRAP_EXECUTE, PERMISSION_BOOTSTRAP_DUMP,
    PERMISSION_NUKE_DATABASE)

link_bootstrap_setup_tool = {'text': _(u'bootstrap'), 'view': 'bootstrap_setup_list', 'icon': 'lightning.png', 'permissions': [PERMISSION_BOOTSTRAP_VIEW]}
link_bootstrap_setup_list = {'text': _(u'bootstrap setup list'), 'view': 'bootstrap_setup_list', 'famfam': 'lightning', 'permissions': [PERMISSION_BOOTSTRAP_VIEW]}
link_bootstrap_setup_create = {'text': _(u'create new bootstrap setup'), 'view': 'bootstrap_setup_create', 'famfam': 'lightning_add', 'permissions': [PERMISSION_BOOTSTRAP_CREATE]}
link_bootstrap_setup_edit = {'text': _(u'edit'), 'view': 'bootstrap_setup_edit', 'args': 'object.pk', 'famfam': 'edit', 'permissions': [PERMISSION_BOOTSTRAP_EDIT]}
link_bootstrap_setup_delete = {'text': _(u'delete'), 'view': 'bootstrap_setup_delete', 'args': 'object.pk', 'famfam': 'lightning_delete', 'permissions': [PERMISSION_BOOTSTRAP_DELETE]}
link_bootstrap_setup_view = {'text': _(u'details'), 'view': 'bootstrap_setup_view', 'args': 'object.pk',  'famfam': 'lightning', 'permissions': [PERMISSION_BOOTSTRAP_VIEW]}
link_bootstrap_setup_execute = {'text': _(u'execute'), 'view': 'bootstrap_setup_execute', 'args': 'object.pk', 'famfam': 'lightning_go', 'permissions': [PERMISSION_BOOTSTRAP_EXECUTE]}
link_bootstrap_setup_dump = {'text': _(u'dump current setup'), 'view': 'bootstrap_setup_dump', 'famfam': 'arrow_down', 'permissions': [PERMISSION_BOOTSTRAP_DUMP]}
link_erase_database = {'text': _(u'erase database'), 'view': 'erase_database_view', 'icon': 'radioactivity.png', 'permissions': [PERMISSION_NUKE_DATABASE]}
