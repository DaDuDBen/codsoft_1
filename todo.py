from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.scrollview import ScrollView
from kivy.config import Config
from kivy.core.window import Window
class ToDoApp(App):
    def build(self):
        Window.size = (500, 600)
        Window.title = 'My ToDo App'
        self.tasks = []
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.input_box = TextInput(hint_text='Enter a new task', size_hint=(1, None), height=40)
        self.layout.add_widget(self.input_box)
        add_button = Button(text='Add Task', size_hint=(1, None), height=40)
        add_button.bind(on_press=self.add_task)
        self.layout.add_widget(add_button)
        self.scroll_view = ScrollView(size_hint=(1, 1), do_scroll_x=False)
        self.tasks_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.tasks_layout.bind(minimum_height=self.tasks_layout.setter('height'))
        self.scroll_view.add_widget(self.tasks_layout)
        self.layout.add_widget(self.scroll_view)
        return self.layout
    def add_task(self, instance):
        task_text = self.input_box.text
        if task_text:
            task_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            task_checkbox = CheckBox(size_hint_x=None, width=40)
            task_checkbox.bind(active=self.complete_task)
            task_label = Label(text=task_text)
            delete_button = Button(text='Delete', size_hint_x=None, width=60)
            delete_button.bind(on_press=lambda instance, layout=task_layout: self.delete_task(layout))
            task_layout.add_widget(task_checkbox)
            task_layout.add_widget(task_label)
            task_layout.add_widget(delete_button)
            self.tasks_layout.add_widget(task_layout)
            self.tasks.append((task_layout, task_label))
            self.input_box.text = ''
    def complete_task(self, checkbox, value):
        tasks_to_complete = [(task_layout, task_label) for task_layout, task_label in self.tasks if task_layout.children[1] == checkbox]
        if tasks_to_complete:
            task_layout, task_label = tasks_to_complete[0]
            if value:
                task_label.color = (0, 1, 0, 1)  
            else:
                task_label.color = (1, 1, 1, 1)  
    def delete_task(self, layout):
        tasks_to_delete = [(task_layout, task_label) for task_layout, task_label in self.tasks if task_layout == layout]
        if tasks_to_delete:
            task_layout, task_label = tasks_to_delete[0]
            self.tasks_layout.remove_widget(task_layout)
            self.tasks.remove((task_layout, task_label))
if __name__ == '__main__':
    ToDoApp().run()
