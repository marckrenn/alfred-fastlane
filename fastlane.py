# encoding: utf-8

import os
import sys
import re
import hashlib
from workflow import Workflow3

# Uff
def clean(string):
	illegal_xml_re = re.compile(u'[\x00-\x08\x0b-\x1f\x7f-\x84\x86-\x9f\ud800-\udfff\ufdd0-\ufddf\ufffe-\uffff]')
	clean = illegal_xml_re.sub('', string)
	return clean

def get_platform(line):
	return re.search('platform :(.*) do', line)

def main(wf):

	cache_path = os.getenv('alfred_workflow_cache')
	default_path = os.getenv('defaultPath')
	path = ''

	# Determine if this script was 'entered' via File Filter or with set defaultPath
	if len(sys.argv) > 1:
		# File Filter or xcode magic
		path = sys.argv[1].decode('utf-8')
	else:
		# defaultPath
		path = os.getenv('defaultPath')

	wf.setvar('path', path) # set for downstream use

	hash = hashlib.md5(path).hexdigest()
	name = os.path.basename(os.path.normpath(path))
	path_copy = path
	sub_paths = [path + '/fastfile', path + '/fastlane/fastfile']
	lanes = []
	fastfile_path = ""

	if wf.update_available:
	    wf.add_item(title='Update Fastlane workflow',
	                subtitle='Action this item to install the update',
	                autocomplete='workflow:update',
					valid=False)

	for path in sub_paths:
		if os.path.isfile(path):

			fastfile_path = path
			platform = ""

			with open(path) as myfile:
				for line in myfile.readlines():

					# Platform prefix
					if get_platform(line) is not None:
						platform = get_platform(line).group(1)

					result = re.search('(?<!_)lane :(.*) do', line)

					if result is not None:
						lane = result.group(1)

						if platform == "":
							lanes.append(lane)
						else:
							lanes.append(platform + ' ' + lane)

	if path_copy != '':

		# Check if selected path contains fastlane folder
		if os.path.isdir(path_copy + '/fastlane'):

			# Get cached lanes
			if os.path.isfile(cache_path + '/projects/' + hash) is True:

				# Is cached
				if path_copy != default_path:

					# Is not default
					i = wf.add_item(title="'" + name + "' lanes:",
								subtitle='Set as default ↩︎ • Re-cache remote lanes ⌘ / ⇧ • Open Fastfile ⌥ • Show path ⌃',
								arg='_default_path,' + path_copy,
								valid=True)

					i.add_modifier('cmd',
							subtitle='Re-cache remote lanes (via bundle exec fastlane lanes)',
							arg='_cache_bundle_exec',
							valid=True)

					i.add_modifier('shift',
							subtitle='Re-cache remote lanes (via fastlane lanes)',
							arg='_cache_fastlane',
							valid=True)

					i.add_modifier('ctrl',
							subtitle=path_copy,
							arg='_open_path, ' + path_copy,
							valid=True)

					i.add_modifier('alt',
							subtitle='Open Fastfile',
							arg='_open_fastfile, ' + fastfile_path,
							valid=True)

				else:
					# Is default
					i = wf.add_item(title="'" + name + "' lanes:",
								subtitle='Default path ✔ • Re-cache remote lanes ⌘ / ⇧ • Open Fastfile ⌥ • Show path ⌃',
								valid=False)

					i.add_modifier('cmd',
							subtitle='Re-cache remote lanes (via bundle exec fastlane lanes)',
							arg='_cache_bundle_exec',
							valid=True)

					i.add_modifier('shift',
							subtitle='Re-cache remote lanes (via fastlane lanes)',
							arg='_cache_fastlane',
							valid=True)

					i.add_modifier('ctrl',
							subtitle=path_copy,
							arg='_open_path, ' + path_copy,
							valid=True)

					i.add_modifier('alt',
							subtitle='Open Fastfile',
							arg='_open_fastfile, ' + fastfile_path,
							valid=True)

				with open(cache_path + '/projects/' + hash) as cached_lanes_file:

					for line in cached_lanes_file.readlines():

						result = re.search('----- fastlane (.*)\[', line)

						if result is not None:

							lane = clean(result.group(1))
							lanes.append(lane)

			else:

				# Is cached
				if path_copy != default_path:

					# Is not default
					i = wf.add_item(title="'" + name + "' lanes:",
								subtitle='Set as default ↩︎ • Cache remote lanes ⌘ / ⇧ • Open Fastfile ⌥ • Show path ⌃',
								arg='_default_path,' + path_copy,
								valid=True)

					i.add_modifier('cmd',
							subtitle='Cache remote lanes (via bundle exec fastlane lanes)',
							arg='_cache_bundle_exec',
							valid=True)

					i.add_modifier('shift',
							subtitle='Cache remote lanes (via fastlane lanes)',
							arg='_cache_fastlane',
							valid=True)

					i.add_modifier('ctrl',
							subtitle=path_copy,
							arg='_open_path, ' + path_copy,
							valid=True)

					i.add_modifier('alt',
							subtitle='Open Fastfile',
							arg='_open_fastfile, ' + fastfile_path,
							valid=True)

				else:
					# Is default
					i = wf.add_item(title="'" + name + "' lanes:",
								subtitle='Default path ✔ • Cache remote lanes ⌘ / ⇧ • Open Fastfile ⌥ • Show path ⌃',
								valid=False)

					i.add_modifier('cmd',
							subtitle='Cache remote lanes (via bundle exec fastlane lanes)',
							arg='_cache_bundle_exec',
							valid=True)

					i.add_modifier('shift',
							subtitle='Cache remote lanes (via fastlane lanes)',
							arg='_cache_fastlane',
							valid=True)

					i.add_modifier('ctrl',
							subtitle=path_copy,
							arg='_open_path, ' + path_copy,
							valid=True)

					i.add_modifier('alt',
							subtitle='Open Fastfile',
							arg='_open_fastfile, ' + fastfile_path,
							valid=True)

		else:

			wf.add_item(title="'" + name + "' doesn't contain a '/fastlane' folder",
						subtitle='Init Fastlane first (goto https://docs.fastlane.tools/)',
						arg='_init',
						valid=True)

	# Output lanes
	for lane in list(dict.fromkeys(lanes)):

		i = wf.add_item(title=lane,
					subtitle='/' + name + '   bundle exec fastlane ' + lane,
					arg='bundle exec fastlane ' + lane,
					valid=True)

		i.add_modifier('cmd',
					subtitle='/' + name + '   fastlane ' + lane,
					arg='fastlane ' + lane,
					valid=True)

		i.add_modifier('alt',
					subtitle='/' + name + '   bundle exec fastlane ' + lane + ' [Add parameters]',
					arg='_withParameters, bundle exec fastlane ' + lane,
					valid=True)

		i.add_modifier('shift',
					subtitle='/' + name + '   fastlane ' + lane + ' [Add parameters]',
					arg='_withParameters, fastlane ' + lane,
					valid=True)

	wf.send_feedback()

if __name__ == u"__main__":
	wf = Workflow3(update_settings={
    'github_slug': 'marckrenn/alfred-fastlane',
    'frequency': 1})
	sys.exit(wf.run(main))
