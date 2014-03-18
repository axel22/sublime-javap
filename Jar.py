import sublime, sublime_plugin, subprocess, platform, urllib, os




class JarCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		filename = self.view.file_name()
		print(filename)
		decompiled, errormessages = self.decompile(filename)
		print(errormessages)
		self.edit_window(edit, decompiled, filename)

	def decompile(self, filename):
		executable = self.get_jar_exec()
		filepath, extension = os.path.splitext(filename)
		print('Detected extension:')
		print(extension)
		basename = os.path.basename(filepath)
		dirname = os.path.dirname(filepath)
		command = [executable, 'tfv', filename]
		print('Executing:')
		print(command)
		return self.exec_command(command)

	def exec_command(self, command):
		os_alias = platform.system().lower()
		if 'windows' in os_alias:
			startupinfo = subprocess.STARTUPINFO()
			startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
			p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupinfo)
			out, err = p.communicate()
			print('Command executed')
			fixed = out.decode("utf-8").replace('\r\n', '\n')
			return (fixed, err)
		else:
			p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			out, err = p.communicate()
			print('Command executed')
			fixed = out.decode("utf-8")
			return (fixed, err)

	def edit_window(self, edit, contents, filename):
		view = self.view
		view.erase(edit, sublime.Region(0, view.size()))
		view.insert(edit, 0, contents)
		view.set_scratch(True)
		#view.set_syntax_file('Packages/Java/Java.tmLanguage')

	def get_new_filename(self, filename):
		return filename.replace("class", "java")

	def get_jar_exec(self):
		os_alias = platform.system().lower()
		print(os_alias)
		if 'windows' in os_alias:
			return 'jar.exe'
		elif 'linux' in os_alias:
			return 'jar'
		elif 'darwin' in os_alias:
			return 'jar'


class OpenClassFileCommand(sublime_plugin.EventListener):

	def on_load(self, view):
		filename = view.file_name()
		if filename is not None:
			extension = os.path.splitext(filename)[1]
			if extension == ".jar":
				view.run_command("jar")

	def on_activated(self, view):
		self.on_load(view)


