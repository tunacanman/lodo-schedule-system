from relatorio.templates.opendocument import Template
from exdata import inv

# basic = Template(source='', filepath='schedules-template.odt')
# basic_generated = basic.generate(o=sched).render()
# file('generated-schedules.odt', 'wb').write(basic_generated.getvalue())

basic = Template(source='', filepath='from-basic-nfor.odt')
open('generated-ex-nfor.odt', 'wb').write(basic.generate(o=inv).render().getvalue())

# from common import inv
# from relatorio.templates.opendocument import Template
# basic = Template(source='', filepath='basic.odt')
# open('bonham_basic.odt', 'wb').write(basic.generate(o=inv).render().getvalue())