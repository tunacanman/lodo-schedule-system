from relatorio.templates.opendocument import Template
from data import sched

# basic = Template(source='', filepath='schedules-template.odt')
# basic_generated = basic.generate(o=sched).render()
# file('generated-schedules.odt', 'wb').write(basic_generated.getvalue())

basic = Template(source='', filepath='schedules-template-p-l.odt')
open('generated-iftest.odt', 'wb').write(basic.generate(o=sched).render().getvalue())

# from common import inv
# from relatorio.templates.opendocument import Template
# basic = Template(source='', filepath='basic.odt')
# open('bonham_basic.odt', 'wb').write(basic.generate(o=inv).render().getvalue())