import sublime, sublime_plugin, subprocess, platform, urllib, os



class JavapCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		filename = self.view.file_name()
		print(self)
		print(filename)
		decompiled, errormessages = self.decompile(filename)
		print(errormessages)
		print('Editing window')
		self.edit_window(edit, decompiled, filename)

	def decompile(self, filename):
		executable = self.get_javap_exec()
		filepath, extension = os.path.splitext(filename)
		print('Detected extension:')
		print(extension)
		basename = os.path.basename(filepath)
		dirname = os.path.dirname(filepath)
		command = [executable, '-c', '-l', '-private', '-verbose', '-classpath', dirname, basename]
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
		window = sublime.active_window()
		if view != window.transient_view_in_group(window.active_group()):
			view.set_scratch(True)
			view.set_syntax_file('Packages/Java/Java.tmLanguage')
			view.erase(edit, sublime.Region(0, view.size()))
			view.insert(edit, 0, contents)
			view.sel().clear()
			view.sel().add(sublime.Region(0))


	def get_new_filename(self, filename):
		return filename.replace("class", "java")

	def get_javap_exec(self):
		os_alias = platform.system().lower()
		print(os_alias)
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


