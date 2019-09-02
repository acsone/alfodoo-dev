import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo9-addons-acsone-alfodoo-dev",
    description="Meta package for acsone-alfodoo-dev Odoo addons",
    version=version,
    install_requires=[
        'odoo9-addon-cmis_alf',
        'odoo9-addon-cmis_field',
        'odoo9-addon-cmis_web',
        'odoo9-addon-cmis_web_alf',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
