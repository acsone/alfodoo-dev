# -*- coding: utf-8 -*-
# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import mock
from odoo.tests import common
from odoo.tools import SUPERUSER_ID
from . import models


class BaseTestCmis(common.SavepointCase):

    @classmethod
    def _init_test_model(cls, model_cls):
        registry = cls.env.registry
        cr = cls.env.cr
        inst = model_cls._build_model(registry, cr)
        model = cls.env[model_cls._name].with_context(todo=[])
        model._prepare_setup()
        model._setup_base(partial=False)
        model._setup_fields(partial=False)
        model._setup_complete()
        model._auto_init()
        model.init()
        model._auto_end()
        return inst

    @classmethod
    def setUpClass(cls):
        super(BaseTestCmis, cls).setUpClass()
        # mock commit since it"s called in the _auto_init method
        cls.cr.commit = mock.MagicMock()
        cls.cmis_test_model = cls._init_test_model(models.CmisTestModel)
        cls.cmis_backend = cls.env['cmis.backend'].create({
            'name': "cmis.test",
            'location': "http://localhost:8081/alfresco/s/cmis",
            'username': 'admin',
            'password': 'admin',
            'initial_directory_write': '/odoo',
        })
