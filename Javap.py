import sublime, sublime_plugin, subprocess, platform, urllib, os




class JavapCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		filename = self.view.file_name()
		decompiled, errormessages = self.decompile(filename)
		print errormessages
		self.push_to_new_window(edit, decompiled, filename)

	def decompile(self, filename):
		executable = self.get_javap_exec()
		filepath, extension =  os.path.splitext(filename)
		print 'Detected extension:'
		print extension
		basename = os.path.basename(filepath)
		dirname = os.path.dirname(filepath)
		command = [executable, '-c', '-l', '-private', '-verbose', '-classpath', dirname, basename]
		print 'Executing:'
		print command
		return self.exec_command(command)

	def exec_command(self, command):
		p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = p.communicate()
		return (out, err)

	def push_to_new_window(self, edit, contents, filename):
		new_view = self.view.window().new_file()
		new_view.set_name(self.get_new_filename(filename))
		new_view.insert(edit, 0, contents)
		new_view.set_syntax_file('Packages/Java/Java.tmLanguage')

	def get_new_filename(self, filename):
		return filename.replace("class", "java")

	def get_javap_exec(self):
		os_alias = platform.system().lower()
		if 'win32' in os_alias:
			return 'javap.exe'
		elif 'linux' in os_alias:
			return 'javap'
		elif 'darwin' in os_alias:
			return 'javap'
