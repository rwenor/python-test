from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('axs_serv.ini') # 'simple.ini')

print parser.get('bug_tracker', 'url')