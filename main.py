import datetime
import getpass 

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print("--- SMART STUDY PLANNER LOGIN ---")
        input_user = input("Kullanıcı Adı: ")
        
        input_pass = getpass.getpass("Şifre: ") 
        
        if input_user == self.username and input_pass == self.password:
            print(f"\n✅ Giriş Başarılı! Hoş geldin, {self.username}.\n")
            return True
        else:
            print("\n❌ Hatalı kullanıcı adı veya şifre!")
            return False

class Task:
    def __init__(self, title, is_completed=False):
        self.title = title
        self.is_completed = is_completed

class StudyPlan:
    def __init__(self, plan_name):
        self.plan_name = plan_name
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))

    def show_progress(self):
        if not self.tasks:
            print("Henüz görev eklenmemiş.")
            return
        completed = sum(1 for t in self.tasks if t.is_completed)
        progress = (completed / len(self.tasks)) * 100
        print(f"📊 {self.plan_name} İlerlemesi: %{progress:.1f}")


admin = User("admin", "12345")


if admin.login():
    
    my_plan = StudyPlan("Yazılım Mühendisliği Finali")
    my_plan.add_task("UML Diyagramı Çizimi")
    my_plan.add_task("GitHub Repo Hazırlığı")
    
    
    my_plan.tasks[0].is_completed = True
    
    
    my_plan.show_progress()
