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

def main(wf):

	cache_path = os.getenv('alfred_workflow_cache')
	default_path = os.getenv('defaultPath')
	path = ''

	# Determine if this script was 'entered' via File Filter or with set defaultPath
	if len(sys.argv) > 1:
		# File Filter
		path = sys.argv[1].decode('utf-8')
	else:
		# defaultPath
		path = os.getenv('defaultPath')

	wf.setvar('path', path) # set for downstream use

	hash = hashlib.md5(path).hexdigest()
	name = os.path.basename(os.path.normpath(path))

	if wf.update_available:
	    wf.add_item(title='Update Fastlane workflow',
	                subtitle='Action this item to install the update',
	                autocomplete='workflow:update',
					valid=False)

	if path != '':

		# Check if lanes were already cached for selected path
		if os.path.isfile(cache_path + '/projects/' + hash) is False: # f py string interpolation

			# Check if selected path contains a fastlane-folder
			if os.path.isdir(path + '/fastlane'):

				i = wf.add_item(title="Cache lanes for '" + name + "'",
							subtitle='bundle exec fastlane lanes',
							arg='_cache_bundle_exec',
							valid=True)

				i.add_modifier('cmd',
						subtitle='fastlane lanes',
						arg='_cache_fastlane',
						valid=True)

				wf.send_feedback()
				return

			else:

				wf.add_item(title="'" + name + " doesn't contain a '/fastlane' folder",
							subtitle='Init Fastlane first (goto https://docs.fastlane.tools/)',
							arg='_init',
							valid=True)

				wf.send_feedback()
				return

	else:
		return

	# Display available lanes
	with open(cache_path + '/projects/' + hash) as cached_fastlanes_file:

		if path != default_path:
			wf.add_item(title="Set '" + name + "' as default project path",
					subtitle='current: ' + default_path,
					arg='_defaultPath,' + path,
					valid=True)

		i = wf.add_item(title="Available lanes for '" + name + "':",
					subtitle='Select to re-cache lanes (via bundle exec fastlane lanes)',
					arg='_cache_bundle_exec',
					valid=True)

		i.add_modifier('cmd',
				subtitle='Select to re-cache lanes (via fastlane lanes)',
				arg='_cache_fastlane',
				valid=True)

		for line in cached_fastlanes_file.readlines():

			result = re.search('----- fastlane (.*)\[', line)

			if result is not None:

				lane = clean(result.group(1))

				i = wf.add_item(title=lane,
							subtitle='bundle exec fastlane ' + lane,
							arg='bundle exec fastlane ' + lane,
							valid=True)

				i.add_modifier('cmd',
							subtitle='fastlane ' + lane,
							arg='fastlane ' + lane,
							valid=True)

				i.add_modifier('alt',
							subtitle='bundle exec fastlane ' + lane + ' (select to set args)',
							arg='_withArgs, bundle exec fastlane ' + lane,
							valid=True)

				i.add_modifier('shift',
							subtitle='fastlane ' + lane + ' (select to set args)',
							arg='_withArgs, fastlane ' + lane,
							valid=True)

	wf.send_feedback()

if __name__ == u"__main__":
	wf = Workflow3(update_settings={
    'github_slug': 'marckrenn/alfred-fastlane',
    'frequency': 1})
	sys.exit(wf.run(main))
