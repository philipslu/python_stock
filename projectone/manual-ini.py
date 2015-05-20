import ConfigParser,os
import StringIO

F=StringIO()
scp = SafeConfigParser()

sections=['listname','sectiontwo']
for s in sections:
    scp.add_section(s)
    scp.set(s,'codename','600848,600849,600850')
    scp.set(s,'othername','1,2,3,4,5')
    
scp.write(f)
print f.getvalue()