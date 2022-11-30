# -*- coding: utf-8 -*-
import yaml
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('/home/kdv/pyneng/examples/20_jinja2/2_example/templates'))
template = env.get_template('router_template.txt')

with open('/home/kdv/pyneng/examples/20_jinja2/2_example/routers_info.yml') as f:
    routers = yaml.safe_load(f)

for router in routers:
    r1_conf = router['name'] + '_r1.txt'
    with open(r1_conf, 'w') as f:
        f.write(template.render(router))
    print(template.render(router))
