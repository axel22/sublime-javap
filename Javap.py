import sublime, sublime_plugin, subprocess, platform, urllib, os




class JavapCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		filename = self.view.file_name()
		print filename
		decompiled, errormessages = self.decompile(filename)
		print errormessages
		self.edit_window(edit, decompiled, filename)

	def decompile(self, filename):
		executable = self.get_javap_exec()
		filepath, extension = os.path.splitext(filename)
		print 'Detected extension:'
		print extension
		basename = os.path.basename(filepath)
		dirname = os.path.dirname(filepath)
		command = [executable, '-c', '-l', '-private', '-verbose', '-classpath', dirname, basename]
		print 'Executing:'
		print command
		return self.exec_command(command)

	def exec_command(self, command):
		startupinfo = subprocess.STARTUPINFO()
		startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupinfo)
		out, err = p.communicate()
		return (out, err)

	def edit_window(self, edit, contents, filename):
		view = self.view
		view.erase(edit, sublime.Region(0, view.size()))
		view.insert(edit, 0, contents)
		view.set_scratch(1)
		view.set_syntax_file('Packages/Java/Java.tmLanguage')

	def get_new_filename(self, filename):
		return filename.replace("class", "java")

	def get_javap_exec(self):
		os_alias = platform.system().lower()
		print os_alias
		if 'windows' in os_alias:
			return 'javap.exe'
		elif 'linux' in os_alias:
			return 'javap'
		elif 'darwin' in os_alias:
			return 'javap'


class OpenClassFileCommand(sublime_plugin.EventListener):

	def on_load(self, view):
		filename = view.file_name()
		extension = os.path.splitext(filename)[1]
		if extension == ".class":
			view.run_command("javap")

	def on_activated(self, view):
		header = view.substr(sublime.Region(0, 9))
		if header == "cafe babe":
			self.on_load(view)


