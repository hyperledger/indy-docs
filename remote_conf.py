# DON'T MOVE ME, OTHER REPO'S READTHEDOCS BUILDS DEPEND ON ME STAYING IN THIS DIRECTORY
#
# This file was written to build a shared readthedocs sidebar on the indy.readthedocs.io website. 
# 
# In each of the indy-* repo's docs folers, there exists a conf.py to be used when building documenation 
# with sphinx. When our docs are build with readthedocs, the conf.py executes. There are a couple of lines 
# in the conf.py that will clone and use this file to generate a shared sidebar that includes all of the repos
# listed below on the readthedocs website. 
# 
# There is almost certainly a better way to do this, but I have yet to figure that out. Please submit a PR 
# against this repository if you would like to help make this process more elegant.
import os
def write_if_changed(fname, contents):
    
    try:
        with open(fname, 'r') as fp:
            old_contents = fp.read()
    except:
        old_contents = ''
        
    if old_contents != contents:
        with open(fname, 'w') as fp:
            fp.write(contents)

def generate_sidebar(conf, conf_api):
    
    # determine 'latest' or 'stable'
    # if not conf.do_gen:
    do_gen = os.environ.get('SIDEBAR', None) == '1' or conf['on_rtd']
    version = conf['rtd_version']
    
    lines = [
        '', '.. DO NOT MODIFY! THIS PAGE IS AUTOGENERATED!', ''
    ]

    def toctree(name, depth):
        lines.extend(['.. toctree::',
                        '    :caption: %s' % name,
                        '    :maxdepth: %d' % depth,
                        ''])

    def endl():
        lines.append('')

    def write_item(desc, link):
        if conf_api == 'indy':
            args = desc,  link
        else:
            args = desc, 'https://hyperledger-indy.readthedocs.io/en/%s/%s.html' % (version, link)
            
        lines.append('    %s <%s>' % args)

    def write_subproject(project, desc, link):
        if project != conf_api:
            args = desc, project, version, link
            lines.append('    %s <https://hyperledger-indy.readthedocs.io/projects/%s/en/%s/%s.html>' % args)
        else:
            lines.append('    %s <%s>' % (desc, link))
    

    toctree('Indy', 2)
    write_item('Introduction', 'index')

    toctree('Repositories', 2)
    write_subproject('node', 'Node', 'index')
    write_subproject('plenum', 'Plenum', 'index')
    write_subproject('hipe', 'HIPE', 'text/index')

    endl()

    write_if_changed('toc.rst', '\n'.join(lines))

def get_intersphinx_mapping(version):
    return {
        'indy': ('http://hyperledger-indy.readthedocs.io/en/%s/' % version, None),
        'indy-node': ('http://indy-node.readthedocs.io/en/%s/' % version, None),
        'indy-plenum': ('http://indy-plenum.readthedocs.io/en/%s' % version, None),
        'indy-hipe': ('http://indy-hipe.readthedocs.io/en/%s' % version, None),
    }