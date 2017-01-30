b'from __future__ import print_function\n\nimport warnings\nfrom setuptools import setup, find_packages, Extension\nfrom setuptools.command.install import install\n\nclass angle_install(install):\n    def run(self):\n        print("please type `install`.\\n")\n        mode = None\n        return install.run(self)\n\ncmdclass = {}\next_modules = []\ncmdclass.update({\'install\': angle_install})\n\nsetup(\n    cmdclass=cmdclass,\n    ext_modules=ext_modules,\n    name=\'angle\',\n    version=\'0.1.4\',\n    author="Pannous",\n    author_email="info@pannous.com",\n    packages=find_packages(),\n    description=\'Angle : speakable programming language compiling to python bytecode\',\n    license=\'Apache2 license\',\n    long_description=open(\'README.md\', \'rb\').read().decode(\'utf8\'),\n    dependency_links=[\'git+http://github.com/pannous/context.git#egg=angle\'],\n    install_requires=[\'astor\', \'pyyaml\', \'argparse\', "stem"],\n    scripts=[\'bin/angle\'],\n    package_data={\n        # \'\': [\'*.cu\', \'*.cuh\', \'*.h\'],\n    },\n)\n'